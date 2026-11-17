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



