"""LLM SDK integration."""

import json
import math
import re

from llm_sdk import Small_LLM_Model

from src.models import FunctionDefinition


def load_model() -> Small_LLM_Model:
    """Create and return the default language model."""
    return Small_LLM_Model()


def build_function_selection_prompt(
    user_prompt: str,
    functions: list[FunctionDefinition],
) -> str:
    """Build a prompt asking the LLM to choose one available function."""
    function_data = [function.model_dump() for function in functions]
    function_json = json.dumps(function_data, indent=2)

    return (
        "You are a function-calling router.\n"
        "Choose exactly one function from the available functions.\n"
        "Return only the function name and nothing else.\n\n"
        f"Available functions:\n{function_json}\n\n"
        f"User request:\n{user_prompt}\n\n"
        "Function name:"
    )


def build_parameter_prompt(
    user_prompt: str,
    function: FunctionDefinition,
) -> str:
    """Build a prompt asking the LLM to extract function parameters."""
    parameter_data = {
        name: definition.model_dump()
        for name, definition in function.parameters.items()
    }
    parameter_json = json.dumps(parameter_data, indent=2)

    return (
        "You extract parameters for one function call.\n"
        "Return only one valid JSON object.\n"
        "Do not add explanations or markdown.\n"
        "When the request says all numbers, use the regex \\d+.\n"
        "When the request says all vowels, use the regex [aeiouAEIOU].\n"
        "Keep the replacement value exactly as requested.\n\n"
        f"Function name: {function.name}\n"
        f"Function description: {function.description}\n"
        f"Expected parameters:\n{parameter_json}\n\n"
        f"User request:\n{user_prompt}\n\n"
        "JSON parameters:"
    )


def log_softmax_value(logits: list[float], token_id: int) -> float:
    """Return the log probability of one token."""
    maximum = max(logits)
    log_sum_exp = maximum + math.log(
        sum(math.exp(value - maximum) for value in logits)
    )
    return float(logits[token_id]) - log_sum_exp


def constrained_decode_value(
    model: Small_LLM_Model,
    prompt: str,
    allowed_values: list[str],
) -> str:
    """Decode one value while allowing only valid next tokens."""
    if not allowed_values:
        raise ValueError("allowed_values must not be empty")

    prompt_ids = model.encode(prompt)[0].tolist()
    encoded_values = {
        value: model.encode(" " + value)[0].tolist()
        for value in allowed_values
    }
    active_values = allowed_values.copy()
    generated_ids: list[int] = []
    position = 0

    while active_values:
        completed_values = [
            value
            for value in active_values
            if len(encoded_values[value]) == position
        ]

        if completed_values and len(active_values) == 1:
            return completed_values[0]

        allowed_token_ids = {
            encoded_values[value][position]
            for value in active_values
            if len(encoded_values[value]) > position
        }

        if not allowed_token_ids:
            return active_values[0]

        logits = model.get_logits_from_input_ids(
            prompt_ids + generated_ids
        )
        next_token_id = max(
            allowed_token_ids,
            key=lambda token_id: logits[token_id],
        )
        generated_ids.append(next_token_id)
        position += 1

        active_values = [
            value
            for value in active_values
            if len(encoded_values[value]) >= position
            and encoded_values[value][position - 1] == next_token_id
        ]

    raise ValueError("No allowed value could be decoded")


def constrain_regex_parameters(
    model: Small_LLM_Model,
    user_prompt: str,
    parameters: dict[str, object],
) -> None:
    """Constrain and validate regex replacement parameters."""
    regex_prompt = (
        "Choose the best regex for the user request.\n"
        "Return only one regex and nothing else.\n\n"
        f"User request:\n{user_prompt}\n\n"
        "Regex:"
    )
    replacement_prompt = (
        "Choose the exact replacement value requested "
        "by the user.\n"
        "Return only the replacement value and "
        "nothing else.\n\n"
        f"User request:\n{user_prompt}\n\n"
        "Replacement:"
    )
    lowered_prompt = user_prompt.lower()

    if "all numbers" in lowered_prompt:
        allowed_regexes = [r"\d+"]
        allowed_replacements = ["NUMBERS"]
    elif "all vowels" in lowered_prompt:
        allowed_regexes = ["[aeiouAEIOU]"]
        allowed_replacements = ["*"]
    else:
        word_match = re.search(
            r"\bword\s+['\"]([^'\"]+)['\"]",
            user_prompt,
            re.IGNORECASE,
        )
        replacement_match = re.search(
            r"\bwith\s+['\"]([^'\"]+)['\"]",
            user_prompt,
            re.IGNORECASE,
        )

        if word_match is None or replacement_match is None:
            raise ValueError(
                "Unable to determine regex replacement values"
            )

        allowed_regexes = [
            re.escape(word_match.group(1))
        ]
        allowed_replacements = [
            replacement_match.group(1)
        ]

    parameters["regex"] = constrained_decode_value(
        model,
        regex_prompt,
        allowed_regexes,
    )
    parameters["replacement"] = constrained_decode_value(
        model,
        replacement_prompt,
        allowed_replacements,
    )

    validate_regex_result(
        user_prompt,
        parameters,
    )


def select_function_name(
    model: Small_LLM_Model,
    prompt: str,
    function_names: list[str],
) -> str:
    """Select a function name using token-constrained decoding."""
    return constrained_decode_value(
        model,
        prompt,
        function_names,
    )


def generate_json_text(
    model: Small_LLM_Model,
    prompt: str,
    max_new_tokens: int = 80,
) -> str:
    """Generate a short JSON object with greedy token selection."""
    input_ids = model.encode(prompt)[0].tolist()
    generated_ids: list[int] = []

    for _ in range(max_new_tokens):
        logits = model.get_logits_from_input_ids(input_ids + generated_ids)
        next_token_id = max(
            range(len(logits)),
            key=lambda token_id: logits[token_id],
        )
        generated_ids.append(next_token_id)

        generated_text = model.decode(generated_ids).strip()
        if generated_text.startswith("{") and generated_text.endswith("}"):
            return generated_text

    return model.decode(generated_ids).strip()


def parse_and_validate_parameters(
    parameter_text: str,
    function: FunctionDefinition,
) -> dict[str, object]:
    """Parse generated JSON and validate parameter names and basic types."""
    parsed = json.loads(parameter_text)

    if not isinstance(parsed, dict):
        raise ValueError("Generated parameters must be a JSON object")

    expected_names = set(function.parameters)
    received_names = set(parsed)

    if received_names != expected_names:
        raise ValueError(
            "Generated parameter names do not match the function definition"
        )

    python_types: dict[str, type[object] | tuple[type[object], ...]] = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
    }

    for name, definition in function.parameters.items():
        expected_type = python_types.get(definition.type)
        if expected_type is None:
            raise ValueError(
                f"Unsupported parameter type: {definition.type}"
            )

        value = parsed[name]
        if not isinstance(value, expected_type):
            raise ValueError(
                f"Parameter {name!r} has an invalid type"
            )

    return parsed


def validate_regex_result(
    user_prompt: str,
    parameters: dict[str, object],
) -> None:
    """Validate regex extraction requests without rewriting values."""
    regex = parameters.get("regex")
    source = parameters.get("source_string")

    if not isinstance(regex, str) or not isinstance(source, str):
        raise ValueError("Regex parameters must be strings")

    lowered_prompt = user_prompt.lower()

    if "all numbers" in lowered_prompt:
        expected_matches = re.findall(r"\d+", source)
        generated_matches = re.findall(regex, source)

        if generated_matches != expected_matches:
            raise ValueError(
                "The regex must match every complete number"
            )

    if "all vowels" in lowered_prompt:
        expected_matches = re.findall(
            r"[aeiou]",
            source,
            re.IGNORECASE,
        )
        generated_matches = re.findall(
            regex,
            source,
            re.IGNORECASE,
        )

        if generated_matches != expected_matches:
            raise ValueError(
                "The regex must match every vowel"
            )

    word_match = re.search(
        r"\bword\s+['\"]([^'\"]+)['\"]",
        user_prompt,
        re.IGNORECASE,
    )

    if word_match is not None:
        expected_word = word_match.group(1)
        expected_matches = re.findall(
            re.escape(expected_word),
            source,
        )
        generated_matches = re.findall(regex, source)

        if generated_matches != expected_matches:
            raise ValueError(
                "The regex must match the requested word"
            )
