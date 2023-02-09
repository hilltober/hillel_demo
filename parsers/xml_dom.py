# The xml.dom module in Python provides support for working with XML documents
# using the Document Object Model (DOM) approach.
# The DOM represents an XML document as a tree-like structure,
# where each element in the document is represented as a node in the tree.
#
# Here's an example of how to parse an XML document using the xml.dom module:
import xml.dom.minidom

# Parse the XML document
xml_file = "person.xml"
dom = xml.dom.minidom.parse(xml_file)

# Get the root element of the document
root = dom.documentElement

# Get the elements in the document
elements = root.getElementsByTagName("person")

# Iterate over the elements and print the values
for element in elements:
    name = element.getElementsByTagName("name")[0].firstChild.data
    age = element.getElementsByTagName("age")[0].firstChild.data
    address = element.getElementsByTagName("address")[0].firstChild.data
    print("Name:", name)
    print("Age:", age)
    print("Address:", address)

# In this example, the xml.dom.minidom.parse function is used to parse
# an XML file and create a DOM tree from the document.
# The documentElement property is used to get the root element of the document,
# and the getElementsByTagName method is used to get the elements
# in the document. The firstChild property is used to get the text value
# of the elements.
#
# The DOM approach to working with XML documents provides a way to manipulate
# the structure of an XML document in a hierarchical manner. However,
# it can be more memory-intensive than other approaches, such as SAX parsing,
# and may not be suitable for working with very large XML documents.
