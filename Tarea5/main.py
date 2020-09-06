import re

def automata(palabra):
    estado = 0
    indice = 0

    while indice < len(palabra):
        if estado == 0:
            if palabra[indice] == '_':
                estado = 1
            elif re.match('[a-z]|[A-Z]', palabra[indice]) != None:
                estado = 2
            else:
                break
        elif estado == 1:
            if palabra[indice] == '_':
                estado = 1
            elif re.match('[a-z]|[A-Z]', palabra[indice]) != None:
                estado = 3
            else:
                break
        elif estado == 2:
            if re.match('[a-z]|[A-Z]', palabra[indice]) != None:
                estado = 2
            elif re.match('[0-9]', palabra[indice]) != None:
                estado = 4
            else:
                break
        elif estado == 3:
            if re.match('[0-9]', palabra[indice]) != None:
                estado = 4
            else:
                break
        else:
            estado = 0
        indice += 1

    if estado == 4:
        return '========== ' + palabra + ' pertenece a esta gramatica =========='
    else:
        return '========== ' + palabra + ' NO pertenece a esta gramatica =========='

print(automata('__servidor1'))
print(automata('3servidor'))