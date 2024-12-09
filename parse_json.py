import json
import re

from pydantic import BaseModel, ValidationError

from icecream import ic

def clean_string(input: str) -> str:
    """
    Cleans and parses JSON-like strings into a JSON-parsable format.
    """

    clean_input = input.strip() # Remove all starting and trailing whitespace
    clean_input = clean_input.replace("```json", "").replace("```", "") # Removes markdown if it's there
    clean_input = clean_input.replace("\\\"", "\"") # Replaces \" with "
    clean_input = clean_input.replace("\"\"", "\"") # Replaces potential "" with "
    clean_input = clean_input.strip()

    if not clean_input.startswith("{") and not clean_input.endswith("}"):
        clean_input = "{" + clean_input + "}"

    return clean_input

def validate_query_response(input:str, model:BaseModel) -> BaseModel:
    clean_response = clean_string(input)

    try:
        parsed_model = model.model_validate_json(json_data=clean_response)
        return parsed_model
    except ValidationError as e:
        print("Validation Error:", e)
        print(clean_response)
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        print(clean_response)
    except Exception as e:
        print("Unexpected Error:", e)
        print(clean_response)