"""
# there are two types of files
# Text file : .txt,.doc,.log etc
# Binary file : .mp4,.mov,.png,.jpeg etc 
r     is used for reading
w     is used to open file for writing, truncating the file first ---> overwriting
x     create a new file and open it for writing
a     open for writing, appending to the end of the file if it exists
b     binary mode
t     text mode(by default)
+     to open a disk file for updating(reading and writing)
r+    to overwrite something from first, not at end, for reading and writing data without truncating
w+    for reading and writing with truncating of data

"""


# READING A FILE

f=open("/home/atif/different_languages_codes/Python_Codes/practice.txt","r")#read mode is by default mode
# if practice.txt is not present in the same path, then complete path should be given
data=f.read()   # f.read   return the whole data in the form of a string
print(data)
print(type(data))
#------------------------
# data=f.read(5)  # for reading only 5 characters
# print(data)
#----------
# line1=f.readline()  # for reading only one line at a time
# print(line1)
# line2=f.readline()
# print(line2)
f.close()


# WRITING TO A FILE
# f=open("/home/atif/different_languages_codes/Python_Codes/practice.txt","w")
# f.write("I want to learn excel automation from tomorrow. 12344")
# f.close()
# APPENDING TO A FILE
# f=open("/home/atif/different_languages_codes/Python_Codes/practice.txt","a")
# f.write("\nI am want to do something amazing")
# f.close()

#   -------------- STSCK OVERFLOW Website for studing IO files instructions ---------



#  with syntax
# with open("/home/atif/different_languages_codes/hello.txt","r") as f:  #  with syntax automatically close the file, so no need to close it 
#     data=f.read()
#     print(data)
# with open("/home/atif/different_languages_codes/hello.txt","w") as f:  
#     f.write("Hello how are you brothers and sisters")
#     print(data)


#  using modules like os,tenserflow #pip or pip3 install tenserflow   for installing tenserflow
# module(like a code library) is a file written by another programmer that generally has functions we can use



# import os
# os.remove("hello.txt")   # for deleting file
#####################################  SOLVE YOUTUBE PRACTICE PROBLEMS ###############


# ------
# f=open("new.txt","a") 
# f.write("Hi everyone\nwe are learning file IO\nUsing java\nI love programming in Java\n")
# f.close() 


# ------ for replacing Java with Python in the file new.txt
# with open("new.txt","r") as f:
#     data=f.read()
# new_data=data.replace("Java","python") # as data is a string
# with open("new.txt","w") as f:
#     f.write(new_data)



# ------ finding a word in the file
# word="learning"
# with open("new.txt","r") as f:
#     data=f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")


# ------ finding the line number in which the word is present
# def check_for_line():
#     word="learning"
#     data=True
#     line_number=1
#     with open("new.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_number)
#                 return 
#             line_number+=1
#         return -1
# check_for_line()


# ------------- finding number of even number
# count=0;
# with open("why.txt","r") as f:
#     data=f.read()
#     print(data)
#     # 1 way 
#     # num=""
#     # for i in range(len(data)):
#     #     if(data[i]==","):
#     #         print(int(num))
#     #         num=""
#     #     else:
#     #         num+=data[i]
#     nums=data.split(",")
#     for val in nums:
#         if(int(val)%2==0):
#             count+=1
# print(count)

    










