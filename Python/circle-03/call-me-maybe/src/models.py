"""Data models used to validate input and output JSON."""

from typing import Literal
from pydantic import BaseModel

ParameterType = Literal["string", "integer", "number", "boolean"]


class ParameterDefinition(BaseModel):
    """Describe the expected type of one function parameter."""

    type: ParameterType


class FunctionDefinition(BaseModel):
    """Describe a function available to the language model."""

    name: str
    description: str
    parameters: dict[str, ParameterDefinition]
    returns: ParameterDefinition


class PromptInput(BaseModel):
    """Represent one natural-language request."""

    prompt: str


class FunctionCallResult(BaseModel):
    """Represent one structured function call result."""

    prompt: str
    name: str
    parameters: dict[str, object]
