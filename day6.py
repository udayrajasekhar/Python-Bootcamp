#DAY 6
#Write a Python script to merge two Python dictionaries

Batsmens={"Ruturaj Gaikwad":"Opener","Faf Duplesis":"Opener",
          "Suresh Raina":"Top Order","Ambati Rayudu":"Top/Middle Order",
          "MS Dhoni":"Middle Order/Wicket Keeper"}
All_Rounders={"Moeen Ali":"Top Order/Off Spin","Sam Curran":"Middle Order/Medium Fast",
              "Ravindra Jadeja":"Middle Order/Off Spin","Shardul Thakur":"Bottom Order/Medium Fast"}
Bowlers={"Deepak Charan":"Medium Fast","Imran Tahir":"Leg Spin"}
Bench={"Dwayne Bravo":"Middle Order/Medium Fast","Lungi Ngidi":"Medium fast",
       "Mitchell Santner":"Middle Order/Off Spin","Cheteswar Pujara":"Top Order",
       "Robin Uthappa":"Top Order/Wicket Keeper","Jason Behrendoff":"Medium Fast",
       "Krishnappa Goutham":"Bottom Order/Off Spin"}

#merging teo teo dictionaries
print("\n Batsmen are:",Batsmens)
print("\n All Rounders are:",All_Rounders)
print("\n Bowlers are:",Bowlers)
print("\n Bench Players are:",Bench)
Batting_Order={}
#using copy() method
Batting_Order=Batsmens.copy()
#using update() method
Batting_Order.update(All_Rounders)
print("\n Batting order is:",Batting_Order)

#Write a Python program to remove a key from a dictionary


#deleting a key(Dwayne Bravo,Krishnappa Goutham,Cheteswar pujara:Ruled out dua to injury)
#using del function
del Bench["Dwayne Bravo"]
#using pop function
Bench.pop("Krishnappa Goutham")
#using popitem function
Bench.popitem()
print("\n Updated Bench Players are:",Bench)

#Write a Python program to map two lists into a dictionary
Substitute=['Narayan Jagadeshan','Harishankar Reddy','Karn Shrama']
Role=['Top Order/Wicket Keeper','Fast Medium','Leg Spin']
print("\n Substitute list is:",Substitute)
print("\n Their role is:",Role)
Subs={}
for key in Substitute:
    for value in Role:
        Subs[key]=value
        Role.remove(value)
        break
print("\n The Sustitues are:",Subs)

#Write a Python program to find the length of a set

Openers={"Ruturaj Gaikwad","Faf Duplesis","Robin Uthappa","Chateswar Pujara","Moeen Ali","Ambati Rayudu"}
print("\n No of Openers are:",len(Openers))
print("\n", Openers)

# Write a Python program to remove the intersection of a 2nd set from the 1st set

Batting_Capability={"Ruturaj Gaikwad","Faf Duplesis","Suresh Raina","Ambati Rayudu","MS Dhoni",
                    "Moeen Ali","Sam Curran","Ravindra Jadeja","Shardul Thakur"}
All_Round_Capability={"Moeen Ali","Sam Curran","Ravindra Jadeja","Shardul Thakur"}
Bowling_Capability={"Moeen Ali","Sam Curran","Ravindra Jadeja","Shardul Thakur",
                    "Deepak Chahar","Imran Tahir"}
print("\n Players having Batting_Capability:",Batting_Capability)
print("\n Players having All_Round_Capability:",All_Round_Capability)
print("\n Players having Bowling_Capability:",Bowling_Capability)
Pure_Batsmens=Batting_Capability-All_Round_Capability
print("\n Pure Batsmens are:", Pure_Batsmens)
