"""
# This is a sample Python script.
print("Hello Flavia")
print(2**2**2) # ** e la puterea
print(-2+3) #poti folosi - in fata la numere
print(20//6) # catul fara virgula
print(20/6) #catul cu virgula
print(20%6)  # asta e mod, celalat e div

print("flavia" *  2) # printezi un string de 2 ori
# cu del x dai delete la o variabila x
 # x=inpxut()tot ce cittesti e procesat ca string

name = input("Enter your name: ")
age = int(input("Enter your age: "))
# asa printam mesaj si variabile
print(f"Hello {name}, I can see you are {age} years old.")

print(type(age)) # asarintezi tipu de date


#OPERATORI IDENTITATE SI APARTENENTA, memberhip and identity
# Identity operators are used to compare object identities
# Example 1: 'is' operator
x = [1, 2, 3]
y = x  # y is assigned to the same object as x
print(x is y)  # True because x and y reference the same object

# Example 2: 'is not' operator
a = 5
b = 10
print(a is not b)  # True because a and b reference different objects

# Membership operators are used to test if a value is found in a sequence

# Example 1: 'in' operator
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)  # True because 'banana' is in the list

# Example 2: 'not in' operator
letters = 'abcdef'
print('z' not in letters)  # True because 'z' is not in the string



#in python nu declaram variabile, se creaza cand le folosim

andra_age=17
print(id(andra_age)) # printam adresa varibilei asa
"""
# STRINGS
from math import *
phrase="flavia e smart."
print (phrase + " i know")
print(phrase.upper())