# this function calculate percentage of a student and print grade based on percentage    
# and ask user repeatedly, if user want to calculate for another student


def Grade_Calculator(name): 
    sum=0
    num=int(input("Enter the number of paper : "))
    
    for i in range(num):
        # n=int(input("Enter marks of",i,"paper : "))  this is invalid format because input() accepts only one string argument
        n=int(input(f"Enter marks of {i+1} paper : "))   # correct way
        sum+=n    

    total=num*100
    percentage=(sum*100)/total 

    print("Your percentage is ",percentage)

    if(percentage>=90):
        grade='A'
    elif(percentage>=80 and percentage<90):
        grade='B'
    elif(percentage>=70 and percentage<80):
        grade='C'
    elif(60 <= percentage < 70):  # python allow chained comparisons
        grade='D'
    elif(percentage<60):
        grade='F'
    
    print(name,"is passed with percentage (",percentage,") and grade '",grade,"'")
    if(percentage>60):
        print(name,", excellent you are passed!")
    else:
        print(name,", unfortunatly, you are failed, try next time")

    ask=input("Do you wanna calculate some other student grade and percentage (y/n) : ")

    if(ask.lower()=='y'):
        name=input("Enter the name of the student : ")
        Grade_Calculator(name)
    else:
        print("Thanks for using our calculator!")
        return    



name=input("Enter the name of the student : ")

Grade_Calculator(name)
















































