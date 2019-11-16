#Formas De Pasar Argumentos
#Ex 1

def subtra(a, b):
    print(a-b)
subtra(5,2)
subtra(2,5)
print()

#Ex 2

def subtra(a, b):
    print(a-b)
subtra(a=5, b=2)
subtra(a=2, b=5)
print()

#Ex 3
def subtra(a, b):
    print(a-b)
subtra(5, b=2)
subtra(5, 2)
print()

#RETORNO DE VALORES EN FUNCIONES
def multiply(a, b):
    return a*b
print(multiply(3, 4))
print()

def multiply(a, b):
    return      
print(multiply(3, 4))
print()

def wishes():
    return "HBD !"
w= wishes()
print(w)
print()

#EJEMPLOS
def wishes():
    print("My Wishes")
    return("HBD")
wishes()
print()

def wishes():
    print("My Wishes")
    return("HBD")
print(wishes())

#USAR UNA LISTA COMO ARGUMENTO DE UNA FUNCION

def hiEverybody(myList):
    for name in myList:
        print("Hi,", name)
hiEverybody(["Adam","John","Luxy"])
print()

#UNA LSITA TAMBIEN PUEDE SER EL RESULTADO DE UNA FUNCION

def createList(n):
    myList=[]
    for i in range(n):
        myList.append(i)
    return myList
print(createList(5))
