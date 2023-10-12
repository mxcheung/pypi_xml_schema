from xml_schema import XMLSchema

try:
    # Encode the dictionary into an XML document
    message = message_schema.encode(message_dict)
    # Convert the XML document to a string
    xml_string = message.toxml()
    # Print the XML string to the console
    print(xml_string)
except Exception as e:
    print(f"An error occurred: {e}")
