import jsonReader
import xmlReader
import csvReader

condition = True

while condition:
    print('=================')
    print('[1]- Mostrar Json')
    print('[2]- Mostrar XML')
    print('[3]- Mostrar CVL')
    print('[4]- Salir')
    print('=================')

    option = int(input('Ingrese una opcion'))

    if option == 1:
        jsonReader.printJson(jsonReader.readJson())
    elif option == 2:
        xmlReader.printXML(xmlReader.readXML())
    elif option == 3:
        csvReader.printCSV()
    elif option == 4:
        condition = False
        print('/----------------------------------/')
        print('Hasta pronto!')
        print('Esdras Rodolfo Toc Hi, RA: 201807373')
        print('/----------------------------------/')
    else:
        print('Ingrese una opcion valida')