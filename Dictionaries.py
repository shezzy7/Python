"""     Dictionaries       """
#   Dictionaries are used to store data in key:value pairs
#   They are unordered(mean we can write any key:value pair at any place ,their order doesn't effect it )
#   we can store any type of data in it (int,bool,string...etc)
#   These are muteable,so we can make any changes in it later in the code 
#   we give any name to keys also we can declare a integer/float/string as key
#   We separate each pair by a comma between them
#   name 
#   syntax:   dictionaryName = {  "kay1"  : value , "key2" : value....}
#   we can't declare multiple keys with same name  
info = {
    "name" : "shezzy",
    5 : "hussain",
    7.9 : 742
}
print(info)
# we can access each key by his name wriiten in [] as below
print(info["name"])
#we can declare any dictionary empty  and can add value in it later like
personal_info = {}
#no if we want to add any pair in it the we can do this as following
personal_info["name"] = "Shahzad"
personal_info["age"] = 25
print(personal_info)
#type of dictionary
print(type(info))

# we  can add any type of data in dictionary even lists and tuples
dict1 = {
    "name" : "gooda",
    "subjects" : ["python","MERN","OOP"],
    "marks" : (23,34,26),
    
}
#to access any value of list in dictionary we dictionaryName["listName"][index]
print(dict1["subjects"][0])
#we can also get any value tuple declared in it by using its index
print(dict1["marks"][0])
#we can also change any value in list  in dictionary
dict1["subjects"][2]="DSA"
# but we can change any value of tuples bcz tuples are immuteable
#we can change value of key late as
dict1["name"]="GOODA"
print(dict1)

""" Nested dictionaries """
#we can also create nested dictionaries mean like other key value pair we can also make key value pairs of dictionary in a dictionary
nested_dict = {
    
    "stu1" : {
        "name" : "Shezzy",
        "age" : 21,
        "height" : 5.6,
        "marks" : 1034
    },
    "stu2" : {
        "name" : "goodo",
        "age" : 20,
        "height" : 5.4,
        "marks" : 700
    }
}
print(nested_dict)
print("Name of student 1 = ",nested_dict["stu1"]["name"])
#adding another dictionary in nested_dict
#nested_dict["stu3"]["name"]="Hania"
#nested_dict["stu3"]["age"]=2
#nested_dict["stu3"]["height"]=2.1
#nested_dict["stu3"]["marks"]=


"""         Methods in dictionaries         """
#   dictName.keys()  #return all th keys of that dictionary ,lets print it
print(nested_dict.keys())

#   dictName.values()  #return all th value of that dictionary ,lets print it
print(nested_dict.values())

#   dictName.items()  #return all th (key,value) pairs as tuples,lets print it
print(nested_dict.items())

#we can also covert the returned value by these methods as follows we convert the keys of above dictionary in list form
print(list(nested_dict.keys()))
#we can also get length of dictionary
print(len(nested_dict))
#we can also get length of lists/tuples/dictionaries eeclared in a dictionary
print(len(list(nested_dict.values())))
#below variable will save all the key value pairs of our dictionary and will save it in the form of list 
pairs = list(nested_dict.items())
print(pairs[1])#here we have printed index 1 of pairs list

#another method is dic.get("key")  -> this return value of given key
print(nested_dict.get("stu2"))
#as above methods works same as we write nested_dict["stu2"]    but
# the difference is that if we write wrong name of key in above method then it will give any error it will just print none  but if we 
# write wrong name of key in simple way as writeen then it will generate an error msg so use this method that if we forgot the name of key 
#then it should not give us any error 

#dictName.update(newDict)       this method inserts the specified items to the dictionary
nested_dict.update( {"name":"kashii","age":21,"height":5.3,"marks":1024} )
#or second method is first we declare a dictionary and then place it in function
dict5 = {"name":"wasii","age":22,"height":5.4,"marks":1000} #here as we write "name","age","height","marks" as keys and there are keys 
 #present with these names already so it will overlap with values of previously present keys bcz keys with same name are not allowed in dictionary

nested_dict.update(dict5)
print(nested_dict)
#so if we want to add some other dictionary in this dictionary then the key of this new dictionary must be different then
# the  kayes already present dictionary
