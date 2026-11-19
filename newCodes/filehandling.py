# storing valid data in the list from raw data list
def set_marks(marks):
    if type(marks) != int and type(marks) != float:
        raise TypeError("Invalid type data is entered!")
    if marks < 0 or marks > 100:
        raise ValueError("Invalid value is entered")
    return marks

correct = []
mark = [3,7,"34","r"]

for i in mark:
    try:
        correct.append(set_marks(i))
    except (ValueError, TypeError) as e:
        print("oho : ",i," is invalid causing",type(e).__name__,":",e)


print("Valid marks : ",correct)




# data = []
# with open("items.csv","r") as f:
#     for line in f:
#         data.append(line.strip().split(","))

# for r in data[1:]:
#     for c in range(2,6):
#         r[c] = float(r[c])

# data[0].append("averages")

# for r in data[1:]:
#     length = len(r[2:])
#     s = 0
#     for c in range(2,6):
#         s += r[c]
#     aver = s/length
#     r.append(aver)

# newdata = []
# for r in data:
#     r = [str(c) for c in r]
#     newdata.append(r)

# # for r in newdata:
# #     print(','.join(r))

# # newfile = os.path.join("generalpracticeoncodes","updateddata.csv")

# # print(newfile)

# with open("updatedData.csv","w") as f:
#     for r in newdata:
#         out_line = ','.join(r)
#         f.write(out_line+"\n")











# while True:
#     try:
#         number = int(input("Enter a number : "))
#         break
#     except:
#         print("Brother you entered, wrong number, try again")

# print("bye bye, see you soon")





# x = 5     
# try:
#     z = calculator('div', 4, x)
#     y = 2 * z
#     f = open('missing-file.txt', 'r')
#     print(f.read())
# except ZeroDivisionError:
#     print("Do not ask me to divide by 0 please.")
# except FileNotFoundError:
#     print("File not found")
# print("Finished!")




# import os
# os.remove("/home/atif/different_languages_codes/generalpracticeoncodes/hello.txt")

# f=open("hello.txt","w")
# f.write("What are you doing here, are you gonna come to peshawar next month")
# f.close()


# f=open("hello.txt","a")
# f.write("\nWhat the heck are you doing here, are you out of your mind")
####    writelines()     for writing multiple lines at once

# f.close()

# f=open("hello.txt",'r')
# data=f.read()
# print(data)
# f.close()





################################### readlines()
# Reads all lines.
# Returns them as a list.
# Each line is a separate string (usually ending with \n, except possibly the last line).
# Use readlines() when you need all lines stored individually in a list, such as for looping or indexing.

################################ readline() concept 
# Reads only one line.
# Stops when it reaches a newline (\n).
# Moves the cursor to the beginning of the next line.


############################## showing cursor position
# print(file.tell())
# Example:
# 6



