

# Call Me Maybe

**Login: msornin**

## Project overview

Call Me Maybe is a Python project that converts natural-language requests into structured function calls.

The program receives:

- a JSON file containing function definitions;
- a JSON file containing user prompts;
- an output path where the generated function calls are written.

For each prompt, the application:

1. loads and validates the available functions;
2. loads and validates the user prompts;
3. builds a prompt describing the available functions;
4. asks the local language model to select exactly one function;
5. builds a second prompt for parameter extraction;
6. generates the function parameters;
7. validates the generated JSON, parameter names, and parameter types;
8. writes the final results to a JSON file.

The final output contains objects in this form:

```json
{
  "prompt": "Greet shrek",
  "name": "fn_greet",
  "parameters": {
    "name": "shrek"
  }
}
```

## Project structure

```text
.
├── data/
│   ├── functions_definition.json
│   ├── input/
│   │   └── prompts.json
│   └── output/
│       └── function_calling_results.json
├── llm_sdk/
├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── llm_client.py
│   ├── loader.py
│   ├── models.py
│   └── writer.py
├── tests/
│   └── test_llm_client.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Code explanation

### `src/__main__.py`

This is the main entry point of the application.

It coordinates the complete workflow:

- reads command-line arguments with `parse_args()`;
- loads the JSON files with `load_json_file()`;
- validates the raw JSON data with Pydantic models;
- loads the local language model;
- processes every user prompt;
- selects the correct function;
- generates and validates the parameters;
- creates a `FunctionCallResult` for each prompt;
- writes all results to the output JSON file.

The module is executed with:

```bash
uv run python -m src
```

Using `python -m src` tells Python to execute `src/__main__.py` as a module.

### `src/cli.py`

This file manages command-line arguments.

It defines the paths used by the application:

- the function-definition file;
- the prompt-input file;
- the output file.

It allows the program to use default paths while still accepting custom paths from the terminal.

Typical arguments are:

```text
--functions-definition
--input
--output
```

### `src/loader.py`

This module loads JSON files from disk.

Its responsibility is limited to:

- opening a file;
- reading its JSON content;
- returning the decoded Python object;
- reporting invalid paths or invalid JSON cleanly.

Keeping file loading in a separate module makes the main program easier to read and test.

### `src/models.py`

This file contains the Pydantic models used to validate all project data.

The main models are:

#### `ParameterDefinition`

Represents one function parameter.

Example:

```json
{
  "type": "string"
}
```

#### `FunctionDefinition`

Represents one callable function with:

- a name;
- a description;
- a dictionary of parameters;
- a return definition.

Example:

```json
{
  "name": "fn_greet",
  "description": "Greet one person",
  "parameters": {
    "name": {
      "type": "string"
    }
  }
}
```

#### `PromptInput`

Represents one natural-language prompt to process.

Example:

```json
{
  "prompt": "Greet shrek"
}
```

#### `FunctionCallResult`

Represents one final generated function call.

It stores:

- the original prompt;
- the selected function name;
- the validated parameters.

Pydantic ensures that malformed input data is rejected before the main logic continues.

### `src/llm_client.py`

This file contains the main language-model logic.

#### `load_model()`

Creates and returns the local `Small_LLM_Model` instance.

#### `build_function_selection_prompt()`

Builds a prompt containing:

- the user request;
- all available function definitions;
- an instruction to return only one function name.

Its purpose is to make the model act as a function router.

#### `build_parameter_prompt()`

Builds a prompt for the selected function.

It includes:

- the user request;
- the selected function name;
- the function description;
- the expected parameter names and types;
- an instruction to return only one JSON object.

#### `constrained_decode_value()`

Performs token-constrained decoding.

Instead of allowing the model to generate any text, it only permits tokens that can still form one of the allowed values.

For function selection, the allowed values are function names such as:

```text
fn_add_numbers
fn_greet
fn_reverse_string
fn_get_square_root
fn_substitute_string_with_regex
```

At every generation step, the function:

1. encodes all allowed values into tokens;
2. finds the token choices that are still valid;
3. gets model logits for the current sequence;
4. selects the valid token with the highest logit;
5. removes candidates that no longer match;
6. returns the last remaining valid value.

This guarantees that the selected function name belongs to the authorized list.

#### `select_function_name()`

Calls `constrained_decode_value()` with the list of available function names.

It returns exactly one valid function name.

#### `generate_json_text()`

Generates parameter text token by token.

It uses greedy decoding by selecting the token with the highest logit at each step.

Generation stops when:

- the decoded text starts with `{`;
- the decoded text ends with `}`.

If no complete JSON object is produced before the token limit, the partial text is returned and later rejected during validation.

#### `parse_and_validate_parameters()`

Parses the generated JSON and validates it against the selected function definition.

It checks that:

- the generated text is valid JSON;
- the result is a JSON object;
- the parameter names exactly match the function definition;
- every parameter has the expected Python type;
- only supported types are used.

Supported parameter types are:

```text
string  -> str
integer -> int
number  -> int or float
boolean -> bool
```

#### `constrain_regex_parameters()`

Handles the regex-specific function.

It constrains known requests to safe expected values:

- all numbers -> `\\d+`;
- all vowels -> `[aeiouAEIOU]`;
- a quoted word -> the escaped requested word.

It also extracts the requested replacement value.

#### `validate_regex_result()`

Validates regex parameters after generation.

It verifies that:

- number requests match complete numbers;
- vowel requests match every vowel;
- word replacement requests match the requested word exactly.

This prevents an incomplete or incorrect regex from being accepted.

#### `log_softmax_value()`

Calculates the log probability of one token from a list of logits.

It uses a numerically stable log-softmax calculation by subtracting the maximum logit before applying the exponential function.

### `src/writer.py`

This module writes the final results to the output JSON file.

It converts the validated result models into JSON-compatible dictionaries and writes a formatted JSON list.

Separating output logic from the main workflow keeps the application modular.

### `tests/test_llm_client.py`

This file contains automated tests for the LLM client logic.

The tests cover:

- regex validation for numbers, vowels, and words;
- invalid regex parameters;
- function selection;
- valid parameter parsing;
- invalid JSON;
- invalid parameter names;
- invalid parameter types;
- non-object JSON values;
- function-selection prompt creation;
- parameter prompt creation;
- empty constrained-decoding choices;
- token selection using fake model logits;
- JSON generation stopping on a complete object;
- JSON generation reaching the token limit;
- log-softmax calculation;
- the complete function-calling flow;
- constrained regex generation for numbers, vowels, and words.

Fake models and `monkeypatch` are used so tests remain fast and deterministic without loading the real model.

## Input files

### Function definitions

The function-definition file describes all available functions.

Example:

```json
[
  {
    "name": "fn_add_numbers",
    "description": "Add two numbers",
    "parameters": {
      "a": {
        "type": "integer"
      },
      "b": {
        "type": "integer"
      }
    }
  }
]
```

### Prompts

The input file contains natural-language requests.

Example:

```json
[
  {
    "prompt": "What is the sum of 2 and 3?"
  },
  {
    "prompt": "Greet shrek"
  }
]
```

## Output file

The output file contains one structured function call per input prompt.

Example:

```json
[
  {
    "prompt": "What is the sum of 2 and 3?",
    "name": "fn_add_numbers",
    "parameters": {
      "a": 2,
      "b": 3
    }
  }
]
```

## Installation

Synchronize the environment and install dependencies:

```bash
uv sync
```

## Useful commands

### Run the program

```bash
uv run python -m src
```

### Run with explicit paths

```bash
uv run python -m src \
  --functions-definition data/functions_definition.json \
  --input data/input/prompts.json \
  --output data/output/function_calling_results.json
```

### Display the generated JSON

```bash
cat data/output/function_calling_results.json
```

### Run all tests

```bash
uv run pytest
```

### Run tests with detailed output

```bash
uv run pytest -v
```

### Run one test file

```bash
uv run pytest tests/test_llm_client.py
```

### Run one specific test

```bash
uv run pytest tests/test_llm_client.py::test_function_calling_flow
```

### Check code style

```bash
uv run flake8 src tests
```

### Check type hints

```bash
uv run mypy src tests --follow-imports=skip
```

### Run all validation commands

```bash
uv run flake8 src tests
uv run mypy src tests --follow-imports=skip
uv run pytest
uv run python -m src
```

### Compile Python files to detect syntax errors

```bash
uv run python -m compileall src tests
```

### Show the project status before submission

```bash
git status
```

### Add files to the 42 repository

```bash
git add .
```

### Create the submission commit

```bash
git commit -m "Complete Call Me Maybe"
```

### Push to the 42 repository

```bash
git push
```

## Current validation status

The project currently passes:

```text
flake8: OK
mypy: OK
pytest: 22 passed
full execution: OK
11 prompts processed successfully
```

The application generates valid function names and parameters for:

- number addition;
- greetings;
- string reversal;
- square roots;
- regex substitutions for numbers, vowels, and words.