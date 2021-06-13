Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("30 days 30 hours challenge")
30 days 30 hours challenge
>>> print('30 days 30 hours challenge')
30 days 30 hours challenge
>>> Hours = "thirty"
print(Hours)
>>> Hours = "thirty"
>>> print(Hours)
thirty
>>> Days = "Thirty days"
>>> print(Days[0])
T
>>> Challenge = "I will win"
>>> print(Challenge[7:10])
win
>>> Challenge = "I will win"
>>> print(len(Challenge))
10
>>> Challenge = "I will win"
>>> print(Challenge.lower())
i will win
>>> Challenge = "I will win"
>>> print(Challenge.upper())
I WILL WIN
>>> a = "30 Days"
>>> b = "30 hours"
>>> c = a + b
>>> print(c)
30 Days30 hours
>>> a = "30 Days"
>>> b = "30 hours"
>>> c = a + " " + b
>>> print(c)
30 Days 30 hours
>>> text = "Thirty days and Thirty hours"
>>> x = text.casefold()
>>> print(x)
thirty days and thirty hours
>>> text = "Thirty days and Thirty hours"
>>> print(text.capitalize())
Thirty days and thirty hours
>>> text = "Thirty days and Thirty hours"
>>> print(text.find(d))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(text.find(d))
NameError: name 'd' is not defined
>>> text = "Thirty days and Thirty hours"
>>> x=text.find('d')
>>> print(x)
7
>>> text = "Thirty days and Thirty hours"
>>> print(text.isalpha())
False
>>> text = "Thirty days and Thirty hours"
>>> print(text.isalnum())
False
>>> 