"""     Set        """
#set is the collection of unordered items.Mean there is no need of orderness in set
#each element in the set must be unique and immuteable
#As lists and dictionaries are muteable so we can not store them in our set .We can store int,string,float,tuple,boolean in set
#if we repeate elemnts in set then repeated elements will be ignored  
#   syntax
nums = {1,2,3,4}
print(nums)
#but as we have said repeated elements are taken as once
nums2 = {1,2,2,2,4,"word","word","shezzy"}  #lets print it .Its repeated elemnt will be ignored
print(nums2)
#Eveven if we check the length of our set then it will also not coun the repeated elements
print(len(nums2))

#an anothe rimportant thing is that we can't declare any empty set as   setName = {}    because our compiler will take it as dictioary
#so for creating an empty set we use following syntax
empty_set = set()

# here is main point which is that we can add and remove elements in set but we can't change any element which is already present in the set
#   so it means that sets are muteable but elements in the set are immuteable

"""         Set Methods         """
empty_set.add(6)  #adds given element and we can add list and tuple and others but we can't add dictionary bcz it's muteable
empty_set.add("Shahzad")
print(empty_set)
#as we have add elements we can also remove elements from the set
empty_set.remove(6)
print(empty_set)
#we can clear ou aaa
#dictName,pop() Third method is used to delete any random valu from the set
nums.pop()
print(nums)

#here some other interesting methods of set 
#syntax:  set1.union(set2)  this works same as like union function in math mean combines  both and return new 
# second method is    set1.insterection(set2)       this works same as like intersection function in math mean combines  common values and return new 
num2 = {1,3,6,7,8}
print(nums.union(num2))
print(nums.intersection(num2))
#we have covered main methods of set no lets solve some practice questions

"""         Practice Questions          """