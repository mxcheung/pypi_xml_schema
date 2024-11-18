import xmlschema
from xml.etree.ElementTree import Element

# Load the FIXML schema
schema = xmlschema.XMLSchema('path/to/fixml-main-4-4-FIA-1-1.xsd')

# Validate and convert the dictionary to an XML element
xml_element = schema.encode(fixml_order)

# Convert to XML string
xml_string = xmlschema.etree_tostring(xml_element, pretty_print=True)

print(xml_string)


```
xmlschema.validators.exceptions.XMLSchemaEncodeError: failed validating <class 'dict'> instance with XMLSchema10(name='fixml-main-4-4-FIA-1-1.xsd', namespace='http://www.fixprotocol.org/FIXML-4-4'):

Reason: unable to select an element for decoding data, provide a valid 'path' argument.

Instance type: <class 'dict'>

Instance:

  { 'FIXML': { '@xmlns': 'http://www.fixprotocol.org/FIXML-5-0-SP2',
               'Order': { '@Side': '1',
                          '@TmInForce': '0',
                          'Instrmt': {'@ID': '12345', '@Sym': 'AAPL'},
                          'OrdQty': {'@Qty': '100'},
                          'Price': {'@Prx': '150.00'}}}}
```
