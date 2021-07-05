#Day 21
#Task 1
def listOfTuples(l1, l2):
    return list(map(lambda x, y:(x,y), l1, l2))

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(listOfTuples(list1, list2))
#Using Zip()
def merge(list1, list2):
      
    merged_list = list(zip(list1, list2)) 
    return merged_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))

#Task 2
list1=[1,2,3,4,5,6,7,8]
list2=['a','b','c','d','e','f','g','h']
result =tuple(zip(list1,list2))
print(result)

#Task 3
list1=[23,45,54,32,78,88,22]
list2=sorted(list1)
print(list2)

#Task 4
def filtereven(nums):
    if nums%2 !=0:
        return True
    else :
        return False

numbers =[23,11,44,34,23,25,26,27,28,34,35,36]
result=filter(filtereven,numbers)
for i in result:
    print(i)
