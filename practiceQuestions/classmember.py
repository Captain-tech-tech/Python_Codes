
class student():
    name="Muhammad Atif"
    clas="third semester"
    @classmethod
    def change(cls,name):
        cls.name = name

print(student.name)

student.change("Ihtisham")

print(student.name) 
