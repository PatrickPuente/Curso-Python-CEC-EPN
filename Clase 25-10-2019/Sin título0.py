print("Comienzo")
for i in range(10):
    print("Hola",end="")
print()
print("Final")

print()

print("Comienzo")
cuenta = 0
for i in range(1,6):
    if i % 2==0:
        cuenta = cuenta+1
print ("Desde 1 hasta 5 hay", cuenta, "multiplos de 2")

print()

veces=input("¿Cuantas veces quiere que le salude?\n")
for i in range(int(veces)):
    print("Hola", end="\n")
print()
print("Adiós")