import json

data={}
data['']=[]

def readJson(path, condition):
    try:
        file=open('auxiliar.json')
        with open('auxiliar.json', "r") as f:
            text=f.read()
            with open(path.replace("'", ""),"r") as f2:
                text2=f2.read()
                if condition == True:
                    text=text.replace(']',',')
                    text2=text2.replace('[',"")
                with open('auxiliar.json', "w") as f3:
                    f3.write(text+text2)
        
        data=json.load(file)
        print(path + ' se leyo correctamente')
        file.close()
    except:
        print('')
    return data

def printJson(finalData):
    for element in finalData:
        print(element)

def printJsonWC(data, registros, condition, find):
    text=''
    if registros == None and condition == None:
        printJson(data)
    elif registros == None and condition != None:
        for i in data:
            if str(i[condition]) == find:
                print(i)
    elif registros!= None and condition == None:
        for i in data:
            text=''
            for j in registros:
                text = text+ '---'+ j+': '+i[j]
            print(text)
    else:
        for i in data:
            text=''
            for j in registros:
                if (str(i[condition]) == find) or (condition == None):
                    text = text + '---' + j+': '+ str(i[j])
            print(text)
            