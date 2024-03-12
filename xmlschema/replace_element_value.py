import xml.etree.ElementTree as ET

# Example XML string
xml_string = '<data><item>This is the original value</item></data>'

# Parse the XML string
root = ET.fromstring(xml_string)

# Find the element you want to replace the value of
item_element = root.find('item')

# Replace the value of the element
item_element.text = 'This is the new value'

# Convert the modified XML tree back to a string
modified_xml_string = ET.tostring(root).decode()

print("Modified XML string:")
print(modified_xml_string)
