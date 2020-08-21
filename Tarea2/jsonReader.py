import json

data={}
data['clientes']=[]

def readJson():
    file=open('data.json')
    data=json.load(file)
    print('<============= Tipo de dato=============>')
    print(type(data))
    print('<=======================================>')
    file.close
    print(data)
    return data

def printJson(dict):
    for element in dict:
        print(element)