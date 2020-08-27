import json

data={}
data['']=[]

def readJson(path):

    try:
        file=open(path.replace("'", ""))
        data=json.load(file)
        print(path + ' se leyo correctamente')
        file.close()
    except:
        print('')
    return data

def printJson(finalData):
    for element in finalData:
        print(element)