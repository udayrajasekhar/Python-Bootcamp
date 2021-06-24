#day 12
#task 1 & 2
file1 = open("30 days 30 hour operations",'w')
L="I have completed 10 days successfully."
file1.writelines(L)
file1.close()

file1 = open("30 days 30 hour operations",'r')
print("Output of Readlines after writing")
print(file1.readlines()) 
print('')
file1.close() 

#task 3
file1 = open("30 days 30 hour operations",'a')
file1.write(" \nUdaya Rajasekhar")
#task 4
file1.close()

file1 = open("30 days 30 hour operations",'r')
print("Output of Readlines after appending")
print(file1.readlines()) 
print('')
file1.close() 

