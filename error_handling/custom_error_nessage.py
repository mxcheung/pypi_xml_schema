from jsonschema import validate, ValidationError
from jsonschema.exceptions import best_match

def extract_error_message(error, schema):
    path = list(error.path)
    sub_schema = schema

    for key in path:
        sub_schema = sub_schema.get("properties", {}).get(key, sub_schema)

    error_message = sub_schema.get("errorMessage")
    if isinstance(error_message, dict):
        error_message = error_message.get(error.validator)

    return error_message or error.message

def validate_order(data):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        custom_message = extract_error_message(best_match([e]), schema)
        return custom_message if custom_message else f"Validation error: {e.message}"
    return "Valid"

# Test data
data1 = {
    "order_type": "dvp",
    "settlement_amount": 100
}

data2 = {
    "order_type": "Rfp"
}

print(validate_order(data1))  # Should print: When order type is dvp, settlement amount must not be supplied.
print(validate_order(data2))  # Should print: When order type is Rfp, settlement amount is required.