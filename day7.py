#day 7
#task 1

def func(a,b):
    addition = a+b
    subtraction = a-b
    multiplication = a*b
    division = a/b
    print("Addition of two numbers is :",addition)
    print("\nsubtraction of two numbers is :",subtraction)
    print("\nmultiplication of two numbers is :",multiplication)
    print("\ndivision of two numbers is :",division)

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
func(x,y)

#task 2

def covid(name,temp):
    print("\npatient is :",name,"\twith temperature :",temp)

name=input("\nEnter patient name:")
temperature=input("\nEnter patient's temperature:")
if temperature.isalpha()==True:
    temp=98
else:
    temp=temperature
covid(name,temp)
