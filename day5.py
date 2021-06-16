#DAY 5 TASK

#CREATION OF LIST AND APPLYING THE GIVEN OPERATIONS

new_list=[1,2,3,4,5,6]
print("initial list is",new_list)
print("Adding using append function")
new_list.append(8)
print(new_list)
print("Adding using insert function")
new_list.insert(6,7)
print(new_list)
print("Deleting using del function")
del new_list[0]
print(new_list)
print("deleting using pop function without index which deleted the last item")
new_list.pop()
print(new_list)
print("deleting using pop function with index which deleted the index item")
new_list.pop(1)
print(new_list)
min_value=min(new_list)
print("Minimum value in the list is",min_value)
max_value=max(new_list)
print("Maximum value in the list is",max_value)

#CREATING A TUPLE AND PRINTING THE REVERSE OF THE CREATED TUPLE

tuple=("a","b","c","d","e","f")
print("initial tuple is:",tuple)
tuple_rev=tuple[::-1]
print("Reversing the tuple")
print(tuple_rev)

#CREATING A TUPLE & CONVERTING IT INTO LIST

atuple=(1,2,3,4,5,6,7,8,9)
print("The tuple is", atuple)
alist=list(atuple)
print("Tuple is converted into List")
print(alist)
