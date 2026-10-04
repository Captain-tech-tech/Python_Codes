# question # 02

python_forms = ["24P-0101", "24P-0102", "24P-0103", "24P-0102","24P-0104", "24P-0101", "24P-0105"]
ml_forms = ["24P-0103", "24P-0106", "24P-0101", "24P-0107", "24P-0106","24P-0105"]

python_reg = set(python_forms)
ml_reg = set(ml_forms)

# the number of forms submitted and the number of unique students
print(f"There are {len(python_forms)} forms submitted for python course")
print(f"There are {len(python_reg)} unique students registered in python course")

print(f"There are {len(ml_forms)} forms submitted for machine learning course")
print(f"There are {len(ml_reg)} unique students registered in ml course")

# for students registered in both courses
print("Students registered in both courses :",end=" ")
register_in_both = python_reg & ml_reg
print(register_in_both)

# students registered only in python
print("Students registered in python only :",end=" ")
register_only_in_python = python_reg - ml_reg
print(register_only_in_python)

# total number of students
print("Total different students : ",len(ml_reg | python_reg))

ml_reg.remove("24P-0105")

print("ML students :",ml_reg)

if "24P-0105" in python_reg:
    print("'24P-0105' is also registered in python")
else:
    print("'24P-0105' is not registered in any other course")

# every group in a sorted form
print("python registertions: ",sorted(python_reg))
print("ml registertions: ",sorted(ml_reg))

