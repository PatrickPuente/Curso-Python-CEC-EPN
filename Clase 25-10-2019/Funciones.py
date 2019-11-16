def message():
    print("Enter a value: ")
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
print()

#FUNCIONES CON PARAMETROS

def hi(name):
    print("Hi,",name)
hi("Patrick")
print()

def hiAll(name1, name2):
    print("Hi,", name1)
    print("Hi,", name2)
hiAll("Sebastian","Konrad")


def address(street, city, postalCode):
    print("Your address is:", street, "St.,", city, postalCode)
s=input("Street: ")
pC=input("Postal Code: ")
c=input("City: ")

address(s, c, pC)
