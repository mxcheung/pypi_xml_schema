import xmlschema
from xml.etree.ElementTree import Element

# Load the FIXML schema
schema = xmlschema.XMLSchema('path/to/fixml-main-4-4-FIA-1-1.xsd')

# Validate and convert the dictionary to an XML element
xml_element = schema.encode(fixml_order)

# Convert to XML string
xml_string = xmlschema.etree_tostring(xml_element, pretty_print=True)

print(xml_string)


