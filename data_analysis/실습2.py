from xml.etree.ElementTree import Element, SubElement, ElementTree


root = Element("Countries")
element1 = Element("Korea")
root.append(element1)

sub_element1 = SubElement(element1, "City")
sub_element1.text = "Seoul"

element2 = Element("Japanese")
root.append(element2)

sub_element2 = SubElement(element2, "City")
sub_element2.text = "Tokyo"

tree = ElementTree(root)

fileName = "example.xml"
with open(fileName, "wb") as file:
    tree.write(file, encoding='utf-8', xml_declaration=True)