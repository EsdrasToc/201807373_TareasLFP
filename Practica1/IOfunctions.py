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
                    print(text)
                    text2=text2.replace('[',"")
                    print(text2)
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