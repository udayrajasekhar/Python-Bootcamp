from tkinter import *
import tkinter.messagebox

window = Tk()
#Declaring Window Title
window.title("Registration Screen")
#Declaring Window size
window.geometry('700x500')
#Declaring Window Color
window.configure(background = "azure");
#below four fields are declared

label1=Label(window ,text= "Employee Registration Form ", font=("bold", 20),bg='lavender',fg='red').grid(row =0, column=2)
Firstname = Label(window ,text = "First Name", font=("bold",10),bg='azure').grid(row = 1,column = 1)
LastName = Label(window ,text = "Last Name", font=("bold",10),bg='azure').grid(row = 2,column = 1)
Email = Label(window ,text = "Email Id", font=("bold",10),bg='azure').grid(row = 3,column = 1)
Mobile = Label(window ,text = "Contact Number", font=("bold",10),bg='azure').grid(row = 4,column = 1)
Address = Label(window,text = "Address",width=20,font=("bold", 10),bg='azure').grid(row =5,column = 1)
City = Label(window ,text = "City",width=20,font=("bold", 10),bg='azure').grid(row = 6,column = 1)
State= Label(window,text = "State",width=20,font=("bold", 10),bg='azure').grid(row = 7,column = 1)
Country = Label(window ,text = "Country",width=20,font=("bold", 10),bg='azure').grid(row = 9,column = 1)
list1 = ['India','Malaysia','Ireland','Switzerland','Australia','South Africa','New Zealand','England','Canada'];
c=StringVar()
droplist=OptionMenu(window,c, *list1)
droplist.config(width=20)
c.set('Select your country')
droplist.grid(row = 9,column = 2)
Gender =Label(window ,text = "Gender",width=20,font=("bold", 10),bg="azure").grid(row = 10,column = 1)
var = IntVar()
Radiobutton(window, text="Male",padx = 30, variable=var, value=1,bg="azure").grid(row = 10,column = 2)
Radiobutton(window, text="Female",padx = 20, variable=var, value=2,bg="azure").grid(row = 10,column = 3)
Dateofbirth =Label(window ,text = "Date Of Birth",width=20,font=("bold", 10),bg="azure").grid(row = 11,column = 1)
var1 = IntVar()
var2 = IntVar()

Firstname1 = Entry(window).grid(row = 1,column = 2)
Lastname1 = Entry(window).grid(row = 2,column = 2)
Email1 = Entry(window).grid(row = 3,column = 2)
Mobile1 = Entry(window).grid(row = 4,column = 2)
Adderss1=Entry(window).grid(row = 5,column = 2)
city1=Entry(window).grid(row = 6,column = 2)
state1=Entry(window).grid(row = 7,column = 2)
Dateofbirth1 = Entry(window).grid(row = 11,column = 2)

#fubction declaration
def clicked():
    tkinter.messagebox.showinfo("Welcome", "Yor Details Submitted  Successfully !")

btn = Button(window ,text="Submit",command=clicked,bg="green",fg="white").grid(row=12,column=2)
window.mainloop()
