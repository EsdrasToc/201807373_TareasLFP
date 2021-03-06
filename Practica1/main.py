import re
import IOfunctions
import calcFunctions
import webbrowser

continue_condition = True
count_condition= False

with open('auxiliar.json', "w") as f:
    f.write("")

data = {}
data['']=['']

while continue_condition:
    texto = input("$")

    if re.match("(S|s)(E|e)(L|l)(E|e)(C|c)(T|t)", texto) != None:
        reader = texto.split()
        registros = []
        switch= False
        switch2 = False
        condition= None
        find=None
        for i in reader:

            if i == '*':
                registros=None
                continue
            
            if re.match("(D|d)(O|o)(N|n)(D|d)(E|e)",i) != None:
                switch= True
                find=''
                continue
            
            if re.match("(S|s)(E|e)(L|l)(E|e)(C|c)(T|t)", i) != None:
                continue

            if switch == False:
                registros.append(i.replace(',',""))
            else:
                if switch2==False:
                    condition = i
                    switch2=True
                else:
                    if i=='=':
                        continue
                    else:
                        print(find)
                        find=find+i.replace('"',"")
        try:
            IOfunctions.printJsonWC(data, registros, condition, find)
        except:
            print('Ha ocurrido un error')

    elif re.match("(C|c)(A|a)(R|r)(G|g)(A|a)(R|r)", texto) != None:
        for i in re.finditer("(( )+.*.json,)|(( )+.*json)", texto):
            path = '{!r}'.format(texto[i.start():i.end()])
            path=path.replace(',',"")
            path=path.replace(' ', "")
            try:
                data = IOfunctions.readJson(path, count_condition)
                count_condition = True
            except:
                print('OCURRIO UN ERROR CON '+path)

    elif re.match("(M|m)(A|a)(X|x)(I|i)(M|m)(O|o)", texto) != None:
        
        try:
            if re.search("(P|p)(R|r)(O|o)(M|m)(E|e)(D|d)(I|i)(O|o)",texto) != None:
                print('El promedio maximo es de: '+str(calcFunctions.maxPromedio(data)))
            elif re.search("(E|e)(D|d)(A|a)(D|d)", texto) != None:
                print('La edad maxima es de: '+str(calcFunctions.maxEdad(data)))
            else:
                print('El atributo solicitado no existe')
        except:
            print('OCURRIO UN ERROR')
    elif re.match("(M|m)(I|i)(N|n)(I|i)(M|m)(O|o)", texto) != None:
        
        try:
            if re.search("(P|p)(R|r)(O|o)(M|m)(E|e)(D|d)(I|i)(O|o)",texto) != None:
                print('El promedio minimo es de: '+str(calcFunctions.minPromedio(data)))
            elif re.search("(E|e)(D|d)(A|a)(D|d)", texto) != None:
                print('La edad minima es de: '+str(calcFunctions.minEdad(data)))
            else:
                print('El atributo solicitado no existe')
        except:
            print('OCURRIO UN ERROR')

    elif re.match("(S|s)(U|u)(M|m)(A|a)", texto) != None:
        
        try:
            if re.search("(P|p)(R|r)(O|o)(M|m)(E|e)(D|d)(I|i)(O|o)",texto) != None:
                print('La suma de promedios es: '+str(calcFunctions.sumPromedio(data)))
            elif re.search("(E|e)(D|d)(A|a)(D|d)", texto) != None:
                print('La suma de edades es: '+str(calcFunctions.sumEdad(data)))
            else:
                print('El atributo solicitado no existe')
        except:
            print('OCURRIO UN ERROR')
            
    elif re.match("(C|c)(U|u)(E|e)(N|n)(T|t)(A|a)", texto) != None:
        if count_condition==False:
            print('Numero de registros: 0')
        else:
            print('Numero de registros: '+str(calcFunctions.count(data)))

    elif re.match("(E|e)(X|x)(I|i)(T|t)", texto) != None:
        continue_condition = False
        with open('auxiliar.json', "w") as f:
            f.write("")
    elif re.match("(R|r)(E|e)(P|p)(O|o)(R|r)(T|t)(A|a)(R|r)", texto) != None:
        text = texto.split()
        j=0
        for i in text:
            j+=1
        
        try:
            if j<2:
                IOfunctions.reportHTML(data, None)
            else:
                IOfunctions.reportHTML(data, text[1])
            
            webbrowser.open_new('REPORTE.html')
        except:
            print('OCURRIO UN ERROR AL REPORTAR')
    else:
        print('comando no valido')