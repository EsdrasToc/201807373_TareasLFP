import json

def maxPromedio(data):
    max=0
    for i in data:
        if i['promedio']>max:
            max=i['promedio']
    return max

def maxEdad(data):
    max=0
    for i in data:
        if i['edad']>max:
            max=i['edad']
    return max

def minPromedio(data):
    min=999
    for i in data:
        if i['promedio']<min:
            min=i['promedio']
    return min

def minEdad(data):
    min=999
    for i in data:
        if i['edad']<min:
            min=i['edad']
    return min

def sumEdad(data):
    suma=0
    for i in data:
        suma+=i['edad']
    return suma

def sumPromedio(data):
    suma=0
    for i in data:
        suma+=i['promedio']
    return suma

def count(data):
    contador=0
    for i in data:
        contador+=1
    return contador