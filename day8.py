#Day 8
#Task 1
def merge(dict1,dict2):
    new={**dict1,**dict2}
    return new
dict1={'INDIA':'DELHI','AUSTRALIA':'SYDNEY','NEW ZEALAND':'WELLINGTON'}
dict2={'SOUTH AFRICA':'CAPETOWN','UNITED KINGDOM':'LONDON','CANADA':'OTTAWA'}
print('\n dict 1 is:',dict1)
print('\n dict 2 is:',dict2)
final_dict=merge(dict1,dict2)
print('\n final doct is:',final_dict)

#Task 2
def sort_list(list1):
    list1.sort(reverse=True)
    print('\n sorted list in descending order is:',list1)
    list1.sort()
    print('\n sorted list in ascending order is:',list1)
    set1=set(list1)
    print("\n converted set is:",set1)
list1=[1,5,9,7,6,4,2,3,8,10]
print("\n ,,initial list is:",list1),
sorted_list=sort_list(list1)

#Task 3
dict3={'Uday':[5,9,7,4],'Prem':[2,8,3,1],'Vamsi':[10,12,15,6]}
for k in sorted(dict3):
    result={k:sorted(dict3[k])}
    print(result)
def function1(dict3):
    res=dict()
    for key in sorted(dict3):
        res[key]=sorted(dict3[key])
    print('\n',res)
function1(dict3)

#Task 4
def string1():
    name=input("\n Enter the string:")
    sentence='string is the name given by the user!'
    updated=sentence.replace("string",name)
    print('\n',updated)
string1()
    
#Task 5
def function2():
    string2=input("\n Enter the string:")
    string2=string2.title()
    print('\n',string2)
function2()

#Task 6
from collections import Counter
l=[1,2,2,3,3,3,4,4,4,4]
d=Counter(l)
print(d)
n_list=list([item for item in d if d[item]>1])
print("\n",n_list)

#Task 7
a=int(input("\nEnter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
sum=a+b+c
denom=int(input("Enter denominator:"))
if sum%denom==0:
    print("Given value is divisible")
else:
    print("Given value is not divisible")

#Task 8
given_numbers = [1,2,2]
addition = 0
for i in given_numbers:
    addition = addition +i
print("addition",addition)
length = len(given_numbers)
mean = addition/length
print("mean :",mean)

given_numbers.sort()
if length%2==0:
    median1 = given_numbers[length//2]
    median2=given_numbers[length//2-1]
    median = (median1+median2)/2
else:
    median = given_numbers[length//2]
print("median is:",median)
import statistics
mode1=statistics.mode(given_numbers)
print("mode is :",mode1)

#Task 9
n1='uday'
n2='hi'
temp=n1
n1=n2
n2=temp
print(n1,n2)

#Task 10
def decimalToBinary(dec):
    if dec > 1:
        decimalToBinary(dec // 2)
    print(dec % 2, end='')
def decimaltoOctal(deciNum):
    octalNum = 0
    countval = 1
    dNo = deciNum
    while (deciNum != 0):
        remainder = deciNum % 8
        octalNum += remainder * countval
        countval = countval * 10
        deciNum //= 8
    print('\n',octalNum)
dec = int(input("Enter any integer number: "))
decimalToBinary(dec)
decimaltoOctal(dec)
