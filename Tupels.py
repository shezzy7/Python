"""     Tuples      """
#Tuple is a buil-in data type that lets us create immuteable sequence of values.It works like list but it have some differences from lists
#Like tuples are immuteable mean we can't make any changes to tuple later in the code and we write their values in paranthesis ()
tup = (2,4,3,6)
print("Welcome to Tuples!");
print(type(tup))
#we can also access any index of a tuple
print("value at Index 1 of tup is : ",tup[1])

tup2 = ()#we can create an empty tuple
tup3 = (3,)#if we want to initialize a tuple with single value then we have to write comma after element otherwise it will be considered as simple variable

#slicing can also be done in tuples like list
print(tup[1:3])

""" Methods in tuples """
print("first occurence of 3 is at index : ",tup.index(3))    #this method returns the index of first index of given number if present
print("2 is presnt for ",tup.count(2)," times in the tuple")    #this method returns counts of given element
 