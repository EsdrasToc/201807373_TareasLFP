import csv

def printCSV():
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            print(row)
        print('<============= Tipo de dato=============>')
        print(type(row))
        print('<=======================================>')
    