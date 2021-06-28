#Day 16
#Task 1
r = lambda x,y:x*y
print(r(6,5))

#Task 2
from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
 
print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))

#Task 3
nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

#Task 4
num_list = [45, 55, 60, 90, 100, 63, 220]
result = list(filter(lambda x: (x % 9 == 0), num_list))
print("Numbers divisible by 15 are",result)

#Task 5
list1 = [10, 21, 4, 45, 66, 93, 11]  
even_nos = list(filter(lambda x: (x % 2 == 0), list1))
print("Even numbers in the list: ", even_nos) 
