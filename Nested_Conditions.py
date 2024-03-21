#Nesting means using conditions inside another some condition
#let we have to find eligibility if a person can drive or not age limit is from 18 to 60
age = int(input("Enter your age : "))
if(age>=18):
    if(age<=60):#we can also write it in parent condition by using and operator between them
        print("You can drive")
    else:
        print("You can't drive,bcz you're too old")
else:
    print("Can't drive because you're too young!")

"""     Let's do some practice Questions on conditions      """
#Q1
#input a number and check whetehr is even or odd
num1 = int(input("Enter number : "))
if(num1%2==0):
    print("Even number")
else:
    print("Odd number")

#Q2
#input 3 numbers and find the greatest of them
print("Enter four numbers to find their greatest")
num2 = int(input("Enter num1: ")) 
num3 = int(input("Enter num2: ")) 
num4 = int(input("Enter num3: "))
num5 = int(input("Enter num4: "))
if(num2>=num3 and num2>=num4 and num2>=num5):
    print(num2," is greatest")
elif(num3>=num4 and num3>=num5):
    print(num3," is the greatest")
elif(num4>=num5):
    print(num4," is the greatest")
else:
    print(num5," is the greatest")
#Q3
#input a number and check whether it's multiple of 7 or not
num5 = int(input("Enter number : "))
if(num5%7==0):
    print("number is multiple of 7").
else:
    print("Number is not a multiple of 7")
