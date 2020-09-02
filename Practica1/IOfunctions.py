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
            if text != '':
                print(text)
    else:
        for i in data:
            text=''
            for j in registros:
                if (str(i[condition]) == find) or (condition == None):
                    text = text + '---' + j+': '+ str(i[j])
            if text != '':
                print(text)
            

def reportHTML(data, number):
    text1 = '<!DOCTYPE html><html><head><title>Reporte</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous"></head><body><table class="table table-dark"><thead><tr><th scope="col">#</th><th scope="col">Nombre</th><th scope="col">Edad</th><th scope="col">Activo</th><th scope="col">Promedio</th></tr></thead><tbody>'
    text3 = '</tbody></table></body></html>'
    text2 = ''
    j=1
    if number == None:
        for i in data:
            text2 = text2 + '<tr><th scope="row">' +str(j) +'</th><td>' + str(i['nombre'])+'</td><td>'+str(i['edad'])+'</td><td>'+str(i['activo'])+'</td><td>'+str(i['promedio'])+'</td></tr>'
            j+=1
    else:
        for i in data:
            if j<= int(number):
                text2 = text2 + '<tr><th scope="row">' +str(j) +'</th><td>' + str(i['nombre'])+'</td><td>'+str(i['edad'])+'</td><td>'+str(i['activo'])+'</td><td>'+str(i['promedio'])+'</td></tr>'
                j+=1
            else:
                break
    with open('REPORTE.html', "w") as report:
                    report.write(text1+text2+text3)
