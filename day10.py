#day 10
#Task 1
class Bank:
      def __init__(self,n,m,balance=500.0) :
             self.accno=accno
             self.name=name
             self.balance =balance
      def deposit(self,amt):
            self.balance+=amt
            return self.balance
      def withdraw(self,amt) :
            if amt>self.balance :
                print('Balance amt is less,so cannot withdraw')
            else :
                self.balance-=amt
            return self.balance
accno=input('Enter  Acct no.:   ')
name=input('Enter name  :   ')
b=Bank(accno,name)
choice = 'yes'
while choice=='yes':
  print('d - deposit,  w- withdrawl ' )
  ch = input('Enter choice  :  ')
  if ch == 'd':
       amt = float(input('Enter amount to be deposited  :   ') )
       print('Balance amount  :  ',b.deposit(amt))
  else :
       amt = float(input('Enter amount to be withdrawn  :  '))
       print('Balance amount  :  ',b.withdraw(amt)  )
  choice= input('Do you  want to continue yes/no   :  ')

#Task 2

class Shop:
      def __init__(self):
            self.categories= ['clothing','footwear ','accessories']        
      def display(self):
            print("Categories in our shop are:",self.categories)
class Clothes(Shop):
      def clothes(self,clothing):
            self.clothing=clothing
            return self.clothing
class Footwear(Shop):
      def footwear(self,footwear):
            self.footwear=footwear
            return self.footwear
class Accessories(Shop):
      def accessories(self,accessories):
            self.accessories=accessories
            return self.accessories
            
s=Shop()
print("Welcome to my shop")
s.display()
c=Clothes()
f=Footwear()
a=Accessories()
clothing=['Shirts','Jeans','T-Shirts','Trousers']
footwear=['Sneakers','Casuals','Sports']
accessories=['Glasses','Wallets','Watches']
choice='yes'
while choice == 'yes':
      print('1-clothing, 2-footwear, 3-accessories')
      option=input("Enter your choice of selection:")
      if option == '1':
            print('Here are the type of clothes we have:',c.clothes(clothing))
            select_1=input("What do you want?")
            if select_1 == 'Shirts':
                  print("These are the Shirts we have: blah blah blah")
            elif select_1 == 'Jeans':
                  print("These are the Jeans we have: blah blah blah")
            elif select_1 == 'T-Shirts':
                  print("These are the T-Shirts we have: blah blah blah")
            elif select_1 == 'Trousers':
                  print("These are the Trousers we have: blah blah blah")
            else:
                  print("We don't have any such kind of things")
      elif option == '2':
            print('Here are the type of clothes we have:',f.footwear(footwear))
            select_2=input("What do you want?")
            if select_2 == 'Sneakers':
                  print("These are the Sneakers we have: blah blah blah")
            elif select_2 == 'Casuals':
                  print("These are the Casuals we have: blah blah blah")
            elif select_2 == 'Sports':
                  print("These are the Sports shoes we have: blah blah blah")
            else:
                  print("We don't have any such kind of things")
      elif option == '3':
            print('Here are the type of clothes we have:',a.accessories(accessories))
            select_3=input("What do you want?")
            if select_3 == 'Glasses':
                  print("These are the Glasses we have: blah blah blah")
            elif select_3 == 'Wallets':
                  print("These are the Wallets we have: blah blah blah")
            elif select_3 == 'Watches':
                  print("These are the Watches shoes we have: blah blah blah")
            else:
                  print("We don't have any such kind of things")
      choice= input("do you want to continue(yes/no): ")
      
