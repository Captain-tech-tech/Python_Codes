
class employee():
    def __init__(self,login_ID,login_password):
        self.login_ID = login_ID
        self.__login_password = login_password  # private attributes
    
    # private method
    def __no_show(self):
        print("It can't be call outside of class but can be call inside of class")
    
    def show_secret(self):
        print("\nIt user private login_password :",self.__login_password)
        print("\nNow accessing private method\n")
        self.__no_show()

e1 = employee("fjf34934vgn3f23","*N)B*%@#e34")
e1.show_secret()
