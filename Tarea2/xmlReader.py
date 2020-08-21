import xml.etree.ElementTree as ET

def readXML():
    tree = ET.parse('data.xml')
    root = tree.getroot()
    print('<============= Tipo de dato=============>')
    print(type(tree))
    print('<=======================================>')
    return root
    

def printXML(root):
    for estudiante in root.findall('estudiante'):
        name = estudiante.find('nombre').text
        lastN = estudiante.find('apellido').text
        age = estudiante.find('edad').text
        idE = estudiante.find('carnet').text
        print('nombre: ', name,' apellido: ', lastN,' edad: ', age,' carnet: ', idE)
    