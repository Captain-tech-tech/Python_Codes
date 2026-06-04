"""
# Dictionaries are build in data type, dictionaries are used to store data values in key:value pairs
# They are unordered, mutable and don't allow duplicate keys
# Values can be any data type
# Keys must be immutable
# Tuples CAN be keys
# Lists CANNOT be keys
# in keys String,Integer,Float,Tuple are allowed but list dictionary and set are not allowed
dict={  
    "key":"value",
    12:"Muhammad Atif",
    455.3:"Artificial intelligence",
    "age":21,
    "Gpa":3.48,
    "marks":[67,86,67,87,56,87],
    "is_adult":True
}
print(type(dict),"\n",dict)
print(dict["key"],"\t",dict["age"])
# print(dict["hello"]) # as no such key is present, it will give us error
dict["key"]="Why not" # for overwriting value
print(dict)
dict["name"]="Bro how are you" # for adding new key:value pair
null_dict={} # creating null dictionary
#nested dictionary
student={
    "name":"Muhammad Atif",
    "marks":{
        "physics":90,
        "Chemistry":87,
        "Biology":78,
        4:65
    },
    "r_number":"25p0053"
}
print(student)
print(student["marks"])
print(student["marks"]["Chemistry"])
#dictionary methods
print(dict.keys()) # it return all the keys of the dictionaries
print(list(dict.keys()))    # it returns all keys in list form  
print(len(student),len(student.keys()))
# ===+===+===+===+===+===+===+===+===+===
print(student.values()) # return all values 
print(list(student.values()))
print(student.items()) #return all key:value pairs as tuples
# +===== Accessing each pair =====+
pairs=list(student.items())
print(pairs[0],"\t",pairs[2])
# ----+-----+------+------+------
print(student.get("marks")) # return the value according to the key
print(student["marks"])
print(student.get("hello"))  # as no "hello" key is present, it will not give us error, but return None
# print(student["hello"])  # it will give us error 
# -----+-----+------+------+-----
dict.update({"City":"Peshawar"})
dict.update(student)
print(dict)
"""


# sets in python
# set is the collection of unodered items
# each element in the set must be unique and immutable, set ignores repeated elements
# sets are mutable but set elements are immutable
# list and dictionary can't be stored inside set, as they are mutable 
collection={15,36,2,23,65,36,65,"Hello","world","world"} # only unique elements are stored
print(collection,"\n",type(collection))
print(len(collection))
col={} # this is an empty dictionary
coll=set() # now this is an empty set
print(type(col),type(coll))
# sets methods
coll.add(23)
coll.add(54)
coll.add(90)
coll.add(90)
print(coll)
coll.remove(90)
print(coll)
# coll.remove(43) # removing value from the set which is not present give us error
coll.add((23,53,"why",56.65)) # adding a tuple
print(coll)
# coll.add([940,53,23]) # it will give us error, as list is mutable
print(len(coll),"\t",coll.clear(),"\t",len(coll))  # coll.clear() does not return something, it only empties the set
collection1={"hello","world","how","are","you","what","are ","you","doing"}
print(collection1)
print(collection1.pop())  # it removes and returns a random element from the set
print(collection1)
print(type(collection1))
# +----+----+----+----+----+----+
set1={1,2,4,5,6,3,4}
set2={4,2,7,8,9}
print(set1.union(set2)) # it does not change the original set, it return a new set, combines both sets vales and returns new set 
print(set1.intersection(set2)) # combine common values and returns new set



# stroring 9 and 9.0 as separate elements in the set
values={9,"9.0"} # or {"9",9.0}
print(values)
value={
    ("float",9.0),
    ("int",9)
}
print(value)









