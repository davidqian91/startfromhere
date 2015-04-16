import xml.etree.ElementTree as ET
tree = ET.parse('movie.xml')
root = tree.getroot()
for p in root.findall('row'):
    t = p.find('Writer')
    for newt in t.text.split(','):
        if newt.strip() != "":
            n = ET.Element('Writer')
            n.text = newt
        p.insert(3, n)
    p.remove(t)
tree.write('output.xml')
