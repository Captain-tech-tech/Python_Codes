# Assignment # 02
results = [("24P-0101", 14), ("24P-0102", 9), ("24P-0103", 18),("24P-0104", 11), ("24P-0105", 18), ("24P-0106", 6), ("24P-0107", 15)]


sums = 0
highest = 0

# finding the highest marks
for i in range(len(results)):
    sums += results[i][1]

    if(highest < results[i][1]):
        highest = results[i][1]

# finding students with the highest marks 
print("\nThe highest marks are :",highest)
print("Student(s) with the highest marks :",end="")
for i in range(len(results)):
    if(highest == results[i][1]):
        print(results[i][0],end="\t")

# calculating class average
class_average = 0
class_average = sums/len(results)
print("\nClass Average :",class_average)

# students below average
below_average = []
for i in range(len(results)):
    if(results[i][1]<class_average):
        below_average.append(results[i][0])

print("Student(s) with marks below average")
print(f"There are {len(below_average)} student below average: ",end="")
for i in range(len(below_average)):
    print(below_average[i])
        

marks = []
for i in range(len(results)):
    marks.append(results[i][1])


marks.sort(reverse=True)

print("Top 3 students marks:", marks[:3])
