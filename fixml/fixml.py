fixml_order = {
    "FIXML": {
        "@xmlns": "http://www.fixprotocol.org/FIXML-5-0-SP2",
        "Order": {
            "@TmInForce": "0",
            "@Side": "1",
            "Instrmt": {
                "@Sym": "AAPL",
                "@ID": "12345"
            },
            "OrdQty": {
                "@Qty": "100"
            },
            "Price": {
                "@Prx": "150.00"
            }
        }
    }
}

import xmlschema
from xml.etree.ElementTree import Element

# Load the FIXML schema
schema = xmlschema.XMLSchema('path/to/fixml-main-4-4-FIA-1-1.xsd')

# Validate and convert the dictionary to an XML element
xml_element = schema.encode(fixml_order)

# Convert to XML string
xml_string = xmlschema.etree_tostring(xml_element, pretty_print=True)

print(xml_string)
