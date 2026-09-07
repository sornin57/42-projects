"""Tests for LLM client validation helpers."""

import importlib
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
validate_regex_result = importlib.import_module(
    "src.llm_client"
).validate_regex_result


def test_validate_numbers_regex() -> None:
    """Accept a regex that matches every complete number."""
    parameters: dict[str, object] = {
        "source_string": "Hello 34 and 233",
        "regex": r"\d+",
        "replacement": "NUMBERS",
    }

    validate_regex_result(
        "Replace all numbers with NUMBERS",
        parameters,
    )


def test_validate_vowels_regex() -> None:
    """Accept a regex that matches every vowel."""
    parameters: dict[str, object] = {
        "source_string": "Programming is fun",
        "regex": "[aeiouAEIOU]",
        "replacement": "*",
    }

    validate_regex_result(
        "Replace all vowels with asterisks",
        parameters,
    )


def test_validate_requested_word_regex() -> None:
    """Accept a regex that matches the requested word."""
    parameters: dict[str, object] = {
        "source_string": "The cat sat with another cat",
        "regex": "cat",
        "replacement": "dog",
    }

    validate_regex_result(
        "Substitute the word 'cat' with 'dog'",
        parameters,
    )


def test_reject_invalid_numbers_regex() -> None:
    """Reject a regex that does not match complete numbers."""
    parameters: dict[str, object] = {
        "source_string": "Hello 34 and 233",
        "regex": r"\d",
        "replacement": "NUMBERS",
    }

    with pytest.raises(
        ValueError,
        match="The regex must match every complete number",
    ):
        validate_regex_result(
            "Replace all numbers with NUMBERS",
            parameters,
        )


def test_reject_non_string_regex_parameters() -> None:
    """Reject regex parameters that are not strings."""
    parameters: dict[str, object] = {
        "source_string": "Hello 34 and 233",
        "regex": 42,
        "replacement": "NUMBERS",
    }

    with pytest.raises(
        ValueError,
        match="Regex parameters must be strings",
    ):
        validate_regex_result(
            "Replace all numbers with NUMBERS",
            parameters,
        )


def test_select_function_name(monkeypatch: pytest.MonkeyPatch) -> None:
    """Return the function selected by constrained decoding."""

    def fake_constrained_decode_value(
        model: object,
        prompt: str,
        allowed_values: list[str],
    ) -> str:
        assert prompt == "Choose a function"
        assert allowed_values == ["fn_greet", "fn_add_numbers"]
        return "fn_greet"

    module = importlib.import_module("src.llm_client")
    monkeypatch.setattr(
        module,
        "constrained_decode_value",
        fake_constrained_decode_value,
    )

    result = module.select_function_name(
        object(),
        "Choose a function",
        ["fn_greet", "fn_add_numbers"],
    )

    assert result == "fn_greet"


def make_greet_function() -> object:
    """Build a function definition used by parameter parsing tests."""
    models = importlib.import_module("src.models")
    return models.FunctionDefinition.model_validate(
        {
            "name": "fn_greet",
            "description": "Greet one person",
            "parameters": {
                "name": {"type": "string"},
            },
            "returns": {"type": "string"},
        }
    )


def test_parse_valid_parameters() -> None:
    """Return parsed parameters when names and types are valid."""
    module = importlib.import_module("src.llm_client")
    function = make_greet_function()

    result = module.parse_and_validate_parameters(
        '{"name": "Shrek"}',
        function,
    )

    assert result == {"name": "Shrek"}


def test_reject_parameter_name_mismatch() -> None:
    """Reject JSON containing unexpected parameter names."""
    module = importlib.import_module("src.llm_client")
    function = make_greet_function()

    with pytest.raises(
        ValueError,
        match="Generated parameter names do not match",
    ):
        module.parse_and_validate_parameters(
            '{"username": "Shrek"}',
            function,
        )


def test_reject_invalid_parameter_type() -> None:
    """Reject a parameter value with the wrong Python type."""
    module = importlib.import_module("src.llm_client")
    models = importlib.import_module("src.models")
    function = models.FunctionDefinition.model_validate(
        {
            "name": "fn_add_numbers",
            "description": "Add two integers",
            "parameters": {
                "a": {"type": "integer"},
                "b": {"type": "integer"},
            },
            "returns": {"type": "integer"},
        }
    )

    with pytest.raises(
        ValueError,
        match="Parameter 'a' has an invalid type",
    ):
        module.parse_and_validate_parameters(
            '{"a": "2", "b": 3}',
            function,
        )


def test_reject_non_object_parameters() -> None:
    """Reject valid JSON that is not a JSON object."""
    module = importlib.import_module("src.llm_client")
    function = make_greet_function()

    with pytest.raises(
        ValueError,
        match="Generated parameters must be a JSON object",
    ):
        module.parse_and_validate_parameters(
            '["Shrek"]',
            function,
        )


def test_build_function_selection_prompt() -> None:
    """Include the request and available function data in the prompt."""
    module = importlib.import_module("src.llm_client")
    function = make_greet_function()

    result = module.build_function_selection_prompt(
        "Greet Shrek",
        [function],
    )

    assert "Greet Shrek" in result
    assert "fn_greet" in result
    assert "Greet one person" in result
    assert "Return only the function name" in result


def test_build_parameter_prompt() -> None:
    """Include the selected function and expected parameters."""
    module = importlib.import_module("src.llm_client")
    function = make_greet_function()

    result = module.build_parameter_prompt(
        "Greet Shrek",
        function,
    )

    assert "Greet Shrek" in result
    assert "fn_greet" in result
    assert "Greet one person" in result
    assert '"name"' in result
    assert '"type": "string"' in result
    assert "Return only one valid JSON object" in result


def test_constrained_decode_rejects_empty_values() -> None:
    """Reject constrained decoding when no value is allowed."""
    module = importlib.import_module("src.llm_client")

    with pytest.raises(
        ValueError,
        match="allowed_values must not be empty",
    ):
        module.constrained_decode_value(
            object(),
            "Choose a function",
            [],
        )


def test_constrained_decode_selects_highest_logit_value() -> None:
    """Select the allowed value whose token has the highest logit."""

    class FakeEncoded:
        """Provide the minimal tensor-like interface used by the client."""

        def __init__(self, token_ids: list[int]) -> None:
            self.token_ids = token_ids

        def __getitem__(self, index: int) -> "FakeEncoded":
            assert index == 0
            return self

        def tolist(self) -> list[int]:
            return self.token_ids

    class FakeModel:
        """Return deterministic token IDs and logits for the test."""

        def encode(self, text: str) -> FakeEncoded:
            token_map = {
                "Choose a function": [0],
                " fn_greet": [1],
                " fn_add_numbers": [2],
            }
            return FakeEncoded(token_map[text])

        def get_logits_from_input_ids(
            self,
            input_ids: list[int],
        ) -> list[float]:
            assert input_ids == [0]
            return [0.0, 1.0, 5.0]

    module = importlib.import_module("src.llm_client")

    result = module.constrained_decode_value(
        FakeModel(),
        "Choose a function",
        ["fn_greet", "fn_add_numbers"],
    )

    assert result == "fn_add_numbers"


def test_generate_json_text_stops_on_complete_object() -> None:
    """Stop generation as soon as a complete JSON object is produced."""

    class FakeEncoded:
        """Provide the minimal tensor-like interface used by the client."""

        def __init__(self, token_ids: list[int]) -> None:
            self.token_ids = token_ids

        def __getitem__(self, index: int) -> "FakeEncoded":
            assert index == 0
            return self

        def tolist(self) -> list[int]:
            return self.token_ids

    class FakeModel:
        """Generate a deterministic three-token JSON object."""

        def encode(self, text: str) -> FakeEncoded:
            assert text == "Generate parameters"
            return FakeEncoded([0])

        def get_logits_from_input_ids(
            self,
            input_ids: list[int],
        ) -> list[float]:
            next_token = len(input_ids)
            logits = [0.0, 0.0, 0.0, 0.0]
            logits[next_token] = 10.0
            return logits

        def decode(self, token_ids: list[int]) -> str:
            decoded_values = {
                (1,): "{",
                (1, 2): '{"name":',
                (1, 2, 3): '{"name": "Shrek"}',
            }
            return decoded_values[tuple(token_ids)]

    module = importlib.import_module("src.llm_client")

    result = module.generate_json_text(
        FakeModel(),
        "Generate parameters",
        max_new_tokens=10,
    )

    assert result == '{"name": "Shrek"}'


def test_generate_json_text_returns_partial_text_at_limit() -> None:
    """Return generated text when the token limit is reached."""

    class FakeEncoded:
        """Provide the minimal tensor-like interface used by the client."""

        def __init__(self, token_ids: list[int]) -> None:
            self.token_ids = token_ids

        def __getitem__(self, index: int) -> "FakeEncoded":
            assert index == 0
            return self

        def tolist(self) -> list[int]:
            return self.token_ids

    class FakeModel:
        """Generate text that never becomes a complete JSON object."""

        def encode(self, text: str) -> FakeEncoded:
            assert text == "Generate parameters"
            return FakeEncoded([0])

        def get_logits_from_input_ids(
            self,
            input_ids: list[int],
        ) -> list[float]:
            next_token = len(input_ids)
            logits = [0.0, 0.0, 0.0, 0.0]
            logits[next_token] = 10.0
            return logits

        def decode(self, token_ids: list[int]) -> str:
            decoded_values = {
                (1,): "{",
                (1, 2): '{"name":',
            }
            return decoded_values[tuple(token_ids)]

    module = importlib.import_module("src.llm_client")

    result = module.generate_json_text(
        FakeModel(),
        "Generate parameters",
        max_new_tokens=2,
    )

    assert result == '{"name":'


def test_log_softmax_value() -> None:
    """Return the log probability for the requested token."""
    module = importlib.import_module("src.llm_client")

    result = module.log_softmax_value(
        [1.0, 2.0, 3.0],
        2,
    )

    assert result == pytest.approx(-0.4076059644)


def test_function_calling_flow(monkeypatch: pytest.MonkeyPatch) -> None:
    """Validate the main function-calling flow with fake model outputs."""
    module = importlib.import_module("src.llm_client")
    models = importlib.import_module("src.models")
    function = make_greet_function()
    user_prompt = "Greet Shrek"

    selection_prompt = module.build_function_selection_prompt(
        user_prompt,
        [function],
    )

    def fake_constrained_decode_value(
        model: object,
        prompt: str,
        allowed_values: list[str],
    ) -> str:
        assert prompt == selection_prompt
        assert allowed_values == ["fn_greet"]
        return "fn_greet"

    monkeypatch.setattr(
        module,
        "constrained_decode_value",
        fake_constrained_decode_value,
    )

    selected_name = module.select_function_name(
        object(),
        selection_prompt,
        ["fn_greet"],
    )
    assert selected_name == "fn_greet"

    parameter_prompt = module.build_parameter_prompt(
        user_prompt,
        function,
    )
    assert "Greet Shrek" in parameter_prompt

    parameters = module.parse_and_validate_parameters(
        '{"name": "Shrek"}',
        function,
    )

    result = models.FunctionCallResult.model_validate(
        {
            "prompt": user_prompt,
            "name": selected_name,
            "parameters": parameters,
        }
    )

    assert result.prompt == "Greet Shrek"
    assert result.name == "fn_greet"
    assert result.parameters == {"name": "Shrek"}


def test_reject_invalid_json_parameters() -> None:
    """Reject malformed JSON before validating parameter names and types."""
    module = importlib.import_module("src.llm_client")
    function = make_greet_function()

    with pytest.raises(ValueError):
        module.parse_and_validate_parameters(
            '{"name": "Shrek"',
            function,
        )


def test_constrain_regex_parameters_for_numbers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Constrain number replacement parameters to the expected values."""
    module = importlib.import_module("src.llm_client")
    calls: list[list[str]] = []

    def fake_constrained_decode_value(
        model: object,
        prompt: str,
        allowed_values: list[str],
    ) -> str:
        calls.append(allowed_values)
        return allowed_values[0]

    monkeypatch.setattr(
        module,
        "constrained_decode_value",
        fake_constrained_decode_value,
    )

    parameters: dict[str, object] = {
        "source_string": "Hello 34 and 233",
    }

    module.constrain_regex_parameters(
        object(),
        "Replace all numbers with NUMBERS",
        parameters,
    )

    assert parameters == {
        "source_string": "Hello 34 and 233",
        "regex": r"\d+",
        "replacement": "NUMBERS",
    }
    assert calls == [[r"\d+"], ["NUMBERS"]]


# Additional tests for constrain_regex_parameters
def test_constrain_regex_parameters_for_vowels(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Constrain vowel replacement parameters to the expected values."""
    module = importlib.import_module("src.llm_client")
    calls: list[list[str]] = []

    def fake_constrained_decode_value(
        model: object,
        prompt: str,
        allowed_values: list[str],
    ) -> str:
        calls.append(allowed_values)
        return allowed_values[0]

    monkeypatch.setattr(
        module,
        "constrained_decode_value",
        fake_constrained_decode_value,
    )

    parameters: dict[str, object] = {
        "source_string": "Programming is fun",
    }

    module.constrain_regex_parameters(
        object(),
        "Replace all vowels with asterisks",
        parameters,
    )

    assert parameters == {
        "source_string": "Programming is fun",
        "regex": "[aeiouAEIOU]",
        "replacement": "*",
    }
    assert calls == [["[aeiouAEIOU]"], ["*"]]


def test_constrain_regex_parameters_for_word(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Extract the requested word and replacement value."""
    module = importlib.import_module("src.llm_client")
    calls: list[list[str]] = []

    def fake_constrained_decode_value(
        model: object,
        prompt: str,
        allowed_values: list[str],
    ) -> str:
        calls.append(allowed_values)
        return allowed_values[0]

    monkeypatch.setattr(
        module,
        "constrained_decode_value",
        fake_constrained_decode_value,
    )

    parameters: dict[str, object] = {
        "source_string": "The cat sat with another cat",
    }

    module.constrain_regex_parameters(
        object(),
        "Substitute the word 'cat' with 'dog'",
        parameters,
    )

    assert parameters == {
        "source_string": "The cat sat with another cat",
        "regex": "cat",
        "replacement": "dog",
    }
    assert calls == [["cat"], ["dog"]]
