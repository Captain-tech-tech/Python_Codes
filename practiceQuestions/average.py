class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        average=0
        sum=0
        for i in self.marks:
            sum+=i
        average=sum/len(self.marks)
        print("Your average ",average)

s1=Student("Muhammad Atif",[34,35,36])
s1.average()

