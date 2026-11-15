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



