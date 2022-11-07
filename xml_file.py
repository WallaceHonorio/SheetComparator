import csv
matriz1 = []
matriz2 = []
matrizComp = []
aux = []
with open("Num1.csv","r") as arquivo1:
    arquivo_csv1 = csv.reader(arquivo1, delimiter=";")
    for l, linha1 in enumerate(arquivo_csv1):
        matriz1.insert(l,linha1) 
        maxLinha1 = l
        for c, celula1 in enumerate(linha1):
            maxcoluna1 = c

with open("Num2.csv","r") as arquivo2:
    arquivo_csv2 = csv.reader(arquivo2, delimiter=";")
    for l, linha2 in enumerate(arquivo_csv2):
        matriz2.insert(l,linha2) 
        maxLinha2 = l
        for c, celula2 in enumerate(linha2):
            maxcoluna2 = c

print("Matriz 1 = " + str(matriz1))
print("Matriz 2 = " + str(matriz2))

i=0
j=0

print("Matriz 2 = " + str(maxLinha1))
print("Matriz 2 = " + str(maxcoluna1))
while i <= maxLinha1:
    while j <= maxcoluna1:
        print("Valor = " + str(matriz1[i][j]))
        print("Valor = " + str(matriz2[i][j]))
        if matriz1[i][j] == matriz2[i][j]:
            aux.insert(j,"TRUE") 
        else:   
            aux.insert(j,"FALSE") 
        print("j - " + str(j))
        j +=1
    print("aux - " + str(aux))  
    matrizComp.insert(i,aux.copy()) 
    aux.clear()
    print("i - " + str(i))
    j = 0
    i +=1
     


print("Matriz Comp = " + str(matrizComp))