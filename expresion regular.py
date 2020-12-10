import re
import os
def pedirNumeroEntero():
     
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
    print()
    print("------------seleccione una opcion---------------")
    print ("1. Variables válidas. Ejemplo: suma, i, cont7, etc. ")
    print ("2. Enteros y decimales. 2.7, 3.1416, 0.2, etc.")
    print ("3. Operadores aritméticos (suma, resta, multiplicación, división, etc.)")
    print ("4. Operadores relacionales. (mayor, menor, igual, diferente, etc.)")
    print ("5. Palabras reservadas.")
    print ("6. salir")
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        
        print ("Las variables que estan declaradas son: ")
        
        textfile = open("ejemplo.txt","r")
        regex=r'(\b[A-Za-z0-9-_]+\s*[=])+'
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
        
        
    elif opcion == 2:
        print ("los numeros enteros y decimales son:")
        textfile = open("ejemplo.txt","r")
        regex=r'[+,-]?[0-9]+'
        patronDECIMAL = r'[+,-]?[[0-9]*[.]]?[0-9]+'
        reg = re.compile(regex)
        
        for line in textfile:
            lista = reg.findall(line)
            print(lista) 
                   
            resultadoDECIMAL = re.findall(patronDECIMAL,line)
            print(resultadoDECIMAL)
        textfile.close()
        
    elif opcion == 3:
        print("Los operadores aritmeticos son: ")
        textfile = open("ejemplo.txt","r")
        regex=r'[\d+]+\s*[\+|\-|\*|\/]+\s*[\d+]+'
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
        
        
    elif opcion == 4:
        print("los operadores relaicionales son: ")
        textfile = open("ejemplo.txt","r")
        regex=r'([A-Za-z0-9|a-z0-9]+\s*[|<|>|!=|<=|>=|==]+\s*[A-Za-z0-9|a-z0-9])+'
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
        
    elif opcion == 5:
        print ("las palabras reservadas son: ")
        textfile = open("ejemplo.txt","r")
        regex=r'\b(False|def|if|raise|None|del|import|return|True|elif|in|try|and|else|is|while|as|except|lambda|with|assert|finally|nonlocal|yield|break|for|not|class|from|or|continue|global|pass\s)+|\s[:]+'
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
         
    elif opcion == 6:
            salir = True
    else:
        print ("Introduce un numero entre 1 y 5")
 
print ("gracias por usar el programa UwU")