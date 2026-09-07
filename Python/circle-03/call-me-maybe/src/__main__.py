"""Main entry point for the application."""

from src.cli import parse_args
from src.llm_client import (
    build_function_selection_prompt,
    build_parameter_prompt,
    constrain_regex_parameters,
    generate_json_text,
    load_model,
    parse_and_validate_parameters,
    select_function_name,
)
from src.loader import load_json_file
from src.models import FunctionCallResult, FunctionDefinition, PromptInput
from src.writer import write_results


def main() -> None:
    """Load inputs, generate function calls, and write the results."""
    args = parse_args()

    functions_data = load_json_file(args.functions_definition)
    prompts_data = load_json_file(args.input)

    functions = [
        FunctionDefinition.model_validate(function)
        for function in functions_data
    ]
    prompts = [
        PromptInput.model_validate(prompt)
        for prompt in prompts_data
    ]

    print(f"Loaded {len(functions)} functions")
    print(f"Loaded {len(prompts)} prompts")
    print(f"Output path: {args.output}")

    model = load_model()
    function_names = [function.name for function in functions]
    results: list[FunctionCallResult] = []

    for prompt in prompts:
        selection_prompt = build_function_selection_prompt(
            prompt.prompt,
            functions,
        )
        selected_name = select_function_name(
            model,
            selection_prompt,
            function_names,
        )

        selected_function = next(
            function
            for function in functions
            if function.name == selected_name
        )
        parameter_prompt = build_parameter_prompt(
            prompt.prompt,
            selected_function,
        )

        for _ in range(3):
            parameter_text = generate_json_text(
                model,
                parameter_prompt,
            )

            try:
                parameters = parse_and_validate_parameters(
                    parameter_text,
                    selected_function,
                )

                if selected_name == "fn_substitute_string_with_regex":
                    constrain_regex_parameters(
                        model,
                        prompt.prompt,
                        parameters,
                    )

                break
            except ValueError as error:
                parameter_prompt += (
                    f"\nPrevious answer was invalid: {error}\n"
                    "Generate a corrected JSON object:"
                )
        else:
            raise ValueError(
                f"Unable to generate valid parameters for: {prompt.prompt}"
            )

        result = FunctionCallResult(
            prompt=prompt.prompt,
            name=selected_name,
            parameters=parameters,
        )
        results.append(result)

        print(f"Prompt: {prompt.prompt}")
        print(f"Selected function: {selected_name}")
        print(f"Generated parameters: {parameters}")
        print()

    write_results(args.output, results)
    print(f"Results written to: {args.output}")


if __name__ == "__main__":
    main()
