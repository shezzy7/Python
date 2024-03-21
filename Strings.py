#String
#   we can write a string in single quotes 'string' , and in double quotes "string" , and even in three quotos """string"""
str1 = 'Welcome strings! '
print(str1)

#concatination->it is the name of process of adding strings
str2 = "start learning strings from now"
print(str2)
print(str1+str2)

#to find the length of string we use len(stringName)
print(len(str1))

#we use \n for braking line
print("I'm a programmer \ntell me how can i assisit you")

#we can directly access any charactor of the string by writing string name and giving the index of that charctor in square braces.For example
name2 = "jawad hussain"
print(name2[2])

#note : we can't assign ny index of our sring a new valus.Like
#we can't write 
#   num2[2]="a"

"""Slicing
#it's method for geting parts of string 
#Syntax->   stringName[startingIndex:endingIndex] but ending index will not be included """
print(name2[0:5])

#if we pass only starting index then len(stringName)  will become ending index (last index)
print(name2[6:])

#if we provide ending index then 0 will bbecome its  starting index
print(name2[:8])
print(name2[:len(name2)])
print(name2[0:])

"""Negative index
in python we use negative indexing concept in this concept we take last index of our string as -1,second last -2,then -3 and so on 
so if we pass  negative -3 as starting value and and -1 as ending value the it will run from -3 to -1 """
print(name2[-3:-1])#here last index will not be included 
print(name2[-3:])#here last index will be taken 

"""
Furthur functions
let 
str = "i am a coder"
1-str.endswith("er") #returns true if string ends with er
2-str.capitalize()#capitalize 1st char
3-str.replace(old,new)#replace all occurences of old with new
4-str.find(word)#returns 1st index of 1st occurrence
5-str.count("am")#counts the occurence of substring
 """
str3 = "i am a coder"
print(str3.endswith("er"))#True
print(str3.endswith("vs"))#False
print(str3.capitalize())#this will not make changes to the original string ,original string will remain same ,lets print it again to check the original string
print(str3)
 #but if we want to modify our original string we can do this as
str3 = str3.capitalize()
print(str3)

#if we want to replace any part of string then we use replace function
#let i want to replace coder with programmer
print(str3.replace("coder","programmer"))
#lets check whether it have make changes to the original string
print(str3)
#no it has not maded any changes to the original string,so for making changes to the original string we can do this as before
str3 = str3.replace("coder","programmer")
print(str3)

#if we want to find any word in the string then then we can use the following function
print(str3.find("m"))#if the word is present multiple times in the string then it will give index of first occurence of word
print(str3.find("progr"))#this will give the starting index of word
print(str3.find("godd"))#if word is not present then it will return -1

#if we want to find number of ocurences of a substring in a string then we use count function
print(str3.count("a"))#a is present 3 times so it will return 3

"""So this is idea of input function . There is a variety of inbuilt but here we have discussed osm of them"""
"""Lets solve practice question on strings"""

#Q1
#input user first name and print its length
str4 = input("ENter your firstName : ")
print("Length of fistname is = ",len(str4))

#Q2
#write a programm to find the first occurence and count no of $ in a string
str5 = "this watch price is $200 and for that is $350"
print("first occurence of $ is ",str5.find("$"))
print("Total counts for $ is = ",str5.count("$"))

#Q3
