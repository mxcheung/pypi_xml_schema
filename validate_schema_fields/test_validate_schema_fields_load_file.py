import unittest
import os

class TestValidateSchemaFields(unittest.TestCase):

    def setUp(self):
        # Define paths to the schema files
        self.valid_schema_path = "valid_schema.json"
        self.invalid_schema_path = "invalid_schema.json"
        
        # Create valid schema file
        valid_schema = {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "enum": ["Alice", "Bob"]
                },
                "email": {
                    "type": "string",
                    "pattern": "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
                }
            }
        }
        with open(self.valid_schema_path, 'w') as file:
            json.dump(valid_schema, file)

        # Create invalid schema file
        invalid_schema = {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "email": {
                    "type": "string"
                }
            }
        }
        with open(self.invalid_schema_path, 'w') as file:
            json.dump(invalid_schema, file)

    def tearDown(self):
        # Clean up the schema files
        os.remove(self.valid_schema_path)
        os.remove(self.invalid_schema_path)

    def test_valid_schema(self):
        schema = load_schema_from_file(self.valid_schema_path)
        try:
            validate_schema_fields(schema)
        except ValueError:
            self.fail("validate_schema_fields() raised ValueError unexpectedly!")

    def test_invalid_schema(self):
        schema = load_schema_from_file(self.invalid_schema_path)
        with self.assertRaises(ValueError) as context:
            validate_schema_fields(schema)
        self.assertIn("Field 'name' must have either an 'enum' or a 'pattern' field.", str(context.exception))
        self.assertIn("Field 'email' must have either an 'enum' or a 'pattern' field.", str(context.exception))

if __name__ == "__main__":
    unittest.main()
