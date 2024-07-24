import jsonschema

def validate_schema_fields(schema):
    """
    Validate that each field in the schema has either an 'enum' or a 'pattern' field.

    :param schema: The JSON schema to validate.
    :raises ValueError: If a field is found without either an 'enum' or a 'pattern'.
    """
    def validate_properties(properties):
        for field, details in properties.items():
            if "enum" not in details and "pattern" not in details:
                raise ValueError(f"Field '{field}' must have either an 'enum' or a 'pattern' field.")
            # If the field is an object, recursively validate its properties
            if details.get("type") == "object" and "properties" in details:
                validate_properties(details["properties"])

    if "properties" in schema:
        validate_properties(schema["properties"])

# Example schema
schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "enum": ["Alice", "Bob"]
        },
        "email": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
        },
        "age": {
            "type": "integer"
        }
    }
}

try:
    validate_schema_fields(schema)
except ValueError as e:
    print(e)
