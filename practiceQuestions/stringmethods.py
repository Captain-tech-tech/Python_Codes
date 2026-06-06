# python is dynamically typed language 
# python is high level language 
# python is portable because same python code be used in different Operating System 
# python is case sensitive language


# practice question on string
"""
text = "i am here just for you, am i okay"
print(text[:5])
print(text[-4:])

# extracting "here" using slicing
a=text.find("here")
b=text[a:a+4]
print(b)

# extracting "here" using negative slicing
c=text[-(len(text)-a):-(len(text)-a)+4]
print(c)

# reverse the entire string using slicing
reverse_string=text[::-1]   #  start is omitted, as start from the end (because step is negative), end is omitted go all the way to the beginning, step = -1 move backwards one character at a tim
print(reverse_string)

# finding number of "am" in the string
print(text.count("am"))

# Find the index of the first occurrence of "just"
print(text.find("just"))
print("The string ends with okay : ",text.endswith("okay"))

# check whether the word "python" exists in the string using find()
if text.find("python")==-1:
    print("The word 'python' is not present in the string")
else :
    print("The word 'python' is present in the string")

# capitalize the first letter of the sentence
print(text.capitalize())

# replace every occurrence of "am" with "was"
print(text.replace("am","was"))
print(text.replace("you","me"))

# create a new string that contains only the first half of the original string 
text1=text[:int(len(text)/2)]
print("The length of the original string : ",len(text),"\nThe length of half of the string : ",len(text1),"\nThe half string : ",text1)

# without using split(), determine whether the word "you" occurs before "okay"
if text.find("you")<text.find("okay"):
    print("Yes, the word 'you' occurs before 'okay'")
else :
    print("No, the word 'you' does not occurs before 'okay'")
# print the substring between "just" and "okay"
print(text[text.find("just")+4:text.find("okay")])

# without using split(), calculate the total number of words in the sentence
count = 1
for i in range(len(text)-1):
    if text[i] == " " and text[i+1] not in [" ", "\t", "\n"]:
        count += 1
print("The number of words in the string are:", count)

# syntax 
# value not in collection
# it means: check whether value does NOT exist inside the collection
print('a' not in ['b','c','d','e'])
"""
