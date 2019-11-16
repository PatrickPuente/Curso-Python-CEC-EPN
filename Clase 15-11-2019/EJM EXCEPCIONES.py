import math

'''try:
    y = 1/0
except ZeroDivisionError:
    print("Zero Division")
except ArithmeticError:
    print("Arithmetic Problem")
print("THE END")


#VAriantes

def badFun(n):
    try:
        return 1/n
    except ArithmeticError:
        print("Arithmetic Problem")
    return None
badFun(0)
print("THE END")'''


'''def badFun(n):
    try:
        return n/0
    except:
        print("I did it again")
        raise
    try:
        badFun(0)
    except ArithmeticError:
        print("dasdsa")'''
        
x = float(input("Enter a Number: "))
assert x>=0.0

x = math.sqrt(x)

print(x)