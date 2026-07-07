# class Student():
#     college_name="Islamia College Peshawar"  # class attribute b/c it is same for every object 
#     name="NO name" # if no name is assign during object declaration, it is by default name, obj attri has a higher precedence over class attri
#     def __init__(self,name,marks=70):  # self can be any other name,  here name, marks are called object attributes
#         # as they are are different for every object of the class
#         self.name=name
#         self.marks=marks
#         print("New student is added to the class...")
#         print(self)
#     def welcome(self):
#         print("You are all welcome here, especially",self.name)
#     def get_marks(self):
#         print(self.name,", your marks are",self.marks)
    
# s1=Student("Atif",45)
# print(s1.name) 
# s1.welcome()

# s2=Student("Ihtisham")
# print(s2.name)

# s2.welcome()
# s2.get_marks()
