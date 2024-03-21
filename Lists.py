"""       Lists       """
"""A list is a built in data type that stores set of values.(Like arrays in java/cpp).
It can can store elements of different types(int,string,float,etc.)
syntax: listName = [ele1,ele2,....,eleN]
example: marks = [364,978,1034]
example2: price = [100,100.25,145.3,125]
example3: list1 = [100,"shezzy",10.2]

"""
marks = [100,25,16]
print(marks)
#for getting length of a list we use following syntax: len(listName)
print(len(marks))
#we can also check its type
print(type(marks))
#lists are muteable, mean we can change value of any index at anytime in the program
marks[0]="shezzy"
print(marks)
#it's allowed in python taht we can acces each index individually
print(marks[2])
#   Slicing(geting any part of list) is also present in lists
#   syntax: listName[start_idx:ending_idx]  #ending index is not included
items = [5,6,8,9,5.3,"shezyy",'C']
print(items[2:len(items)])
print(items[:6])#remeber like strings if we miss starting index then 0 will be taken as stating index
print(items[6:])#if ending index is missing then last index will be taken as ending index

print(items[-5:-1])#-ve indexing is also possible in list like string here -1 will be last index and will go on backward mean items[-1]='C', items[-2]="shezzy", items[-3]=5.3, and so on

"""     List Methods    """
#like methods in strings, list also have some methods.Some of these are following
#keep in mind these methods of list ,unlike string methods, don't return the value of list it just makes changes to the list .If we print these methods with list name then None will be printed 

meth = [2,1,3]
print(meth)
meth.append(6)#adds one element at the end and we can pass only one element in it.This will change the original list
print(meth)
print(meth.sort())#but if we print this function then this will print none bcz it makes changes to original list not return the list after sorting it
str2 = ["hello","shezzy","come in"]
print(meth)
str2.sort()#Sorting is also applied on strings according to the orders of alphabet
print(str2)

meth.sort(reverse=True)#sorts in descending order
print(meth)

meth.reverse()  #this will just reverse the array .Mean list = [2,5,6] after reversing will become [6,5,2]
meth.insert(1,10)   #this method is used to insert any value in the list.In this method fisrt value is the number of index at which we want to insert a value and second is the value to be inserted.So here 10 will be inserted at index 1 
print(meth)

meth.remove(1)  #this method will remove the first occurence of the given element from the list.Here we have write 1 int it so it will find the first occurence of 1 in the list and will remove it
print(meth)

meth.pop(2) #this method will removes the element at given index.Here as we entered 2 so it will remove element present at index 2
print(meth)


"""     Practice Questions      """
#Q1
#Ask user to input nsmes of three favourite books,store them in a list and then print them
books = []
book1 = input("Enter name of first fav book : ")
book2  = input("Enter name of 2nd fav book : ")
book3 = input("Enter name of 3rd fav book : ")
books.append(book1)
books.append(book2)
books.append(book3)
print(books)

#Q2
#WAP to check if a list contains a palindrome of elements.
pali = [1,2,3,2,1]
paliCopy = pali.copy() #this method will copy the whole list in new list
paliCopy.reverse()

if(pali==paliCopy):
    print("Given list ",pali,"  is a Palindrom list!")
else:
    print("Given list ",pali,"  is not a palindrome list")

#Q3
#WAP to count the number of students with "A" grade in the following tuple
grades = ["C","D","A","A","B","B","A"]
print("Total number of students with grade 'A' are : ",grades.count("A"))

#Q4
#Store these values in a list "C","D","A","A","B","B","A" and then sort it from "A"  to "D"
pList = ["C","D","A","A","B","B","A"]
pList.sort()    #this method only changes the list but not returb the values after sorting
print(pList.sort())