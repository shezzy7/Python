""" CONDITIONAL STATEMENT
if-elif-else(SYNTAX)

if(condition):
    statement
elif(condition):
    statement
else:
    statement
"""
#let age of a person is given check whether he is eligible to vote or not
#in conditional staements we make proper indentation mean if we write if condition then in tis staement we have to give some space
# from start to tell that this is the part of this if but if we dont give space then it will give error .Its just like  blocks {} in c++ 
#
age = 19
if(age>=18):
    print("ELigible to vote!")

#elif works like else if in c++ or java

#lets make a trafic signal 
light = input("Enter color of signal : ")
if(light == "red" or light=="RED"):
    print("Stop")
elif(light=="yellow" or light == "YELLOW"):
    print("Get ready")
elif(light=="green" or light=="GREEN"):
    print("Go")
else:
    print("Invalid color")

print("END of 2nd conditional statement")#Here space sre not given so it will be considered not a aprt of conditional staement and conitional staement will wend here

# Lets make geading system
marks = int(input("Enter marks : "))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")


