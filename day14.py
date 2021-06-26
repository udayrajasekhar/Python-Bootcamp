#Day 14
#Task 1
try:
    L1=[1,2,3]
    L1[3]
except IndexError:
    print("Index Error")
    
try:
    import notamodule
except ModuleNotFoundError:
    print("Module Not Found Error")

try:
    D1={'1':"aa",'2':"bb",'3':"cc"}
    D1['4']
except KeyError:
    print("Print Error")

try:
    from math import cube
except ImportError:
    print("Import Error")

try:
    '2'+2
except TypeError:
    print("Type Error")

try:
    int('xyz')
except ValueError:
    print("Value Error")

try:
    age
except NameError:
    print("Name Error")

try:
    x=100/0
except ZeroDivisionError:
    print("Zero Division Error")
    
#Task 2
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
try:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            a=int(input("Enter first number:"))
            b=int(input("Enter second number:"))
            if choice == '1':
                print(a, "+", b, "=", add(a, b))
            elif choice == '2':
                print(a, "-", b, "=", subtract(a, b))
            elif choice == '3':
                print(a, "*", b, "=", multiply(a, b))
            elif choice == '4':
                print(a, "/", b, "=", divide(a, b))
            break
        else:
            print("Invalid Input")

except TypeError:
    print("Type Error")
except ZeroDivisionError:
    print("Zero Division Error")
    

#Task 3
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


#Task 4
'''When there are no exceptions or errors in the program
   and we don't need to catch the exceptions then try-
   except scenario is not required'''


#Task 5
def joint(x,y):
    return x+" "+y
try:
    i=input("Enter anything(1):")
    j=input("Enter anything(2):")
    word=joint(i,j)
    print(word)
except TypeError:
    print("Type Error")
    
