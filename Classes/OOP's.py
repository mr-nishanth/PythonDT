'''
Like Web Base software log in and log out

User_name , Password --> it's Propertyes

User Painnara work irrukula Log in ,Log out ,comment etc..  --> Methods

'''
"""
class User:  # User is object

# Class la oru function vaintha yathaa method inu soilluvoim

   # def __init__(self):
# Double underscore etha internal usage or magic methods
# This method automatic ah invoke yakeruim , when this invoke means
# namaa (when we use this plan and create one object , tha time it invoke aautomaticlly) yapo plan ah use painne object ah create painnaromoo 

# Self vainthu yatha mean painnuthu naaa , user name irrukara object yoda user name inu solla

#-------x------x---------(USER name and password ah get painna )------------x----------x--

    def __init__(self, username, password):
        self.username = username
        self.password = password

# N is varaiable name , yatha hold painnuthu naa User Object ah
# User object ah call painne ("Nishanth","secret") inu string ah kudukaroim
# This  Expression User("Nishanth", "Secret")  automaticlly go to init constract method ah invoke painnukuim
# Apo "Nishanth" ,"secret" inu irrukara string vainthu , this method def __init__(self, username, password): ikku pass yakuim
# ethula irrukara username variable la nama kudukara name , password variable laium store yakuim

#then user object la irrukara username and password property la , store panna  string  assign yakeruim



N = User("Nishanth", "Secret")
print(N)  # It's display userobject inu

print(N.username) # N is user object , userobject la irrukara username ah display paiinu
print(N.password)

"""
# ==========( Log in and log out Logic  )================x========
"""

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False  # ref its told user (it's used to tall the user status alredy in or out)

    def login(self):
        if self.is_logged_in:
            print(f"{self.username} is already logged in ")
        else:
            self.is_logged_in=True  # ref 1 once log in yaketaa looged in status true inu yakeranuim
            print(f"{self.username} Logged In")

    def logout(self):
        if self.is_logged_in:
            self.is_logged_i= False
            print(f"{self.username} Logged Out")
        else:
            print(f"{self.username} is already a logged out user")        

'''
user1 = User("Nishanth", "PWD")
user1.login()
user1.logout()
user1.login()
user2 = User("Vasee", "Surya")
user2.login()

user2.logout()
'''
# ----Check the user already log in or not (ref top 1)



user1 = User("Nishanth", "PWD")
user1.login()
user1.logout()
user1.login()

user2 = User("Vasee", "Surya")
user2.logout()
user2.login()
user2.logout()

"""
#==================x===========( For Adim user -- Inhertince)===========x====================x=============x


class User:
    def __init__(self, username, password):

        
        username = input(" Enter your name : ").title()
        password = input(" Enter your Password : ").lower()        
        self.username = username
        self.password = password
        

        self.is_logged_in = False



    def login(self):
        if self.is_logged_in:
            print(f"{self.username} is already logged in ")
        else:
            self.is_logged_in = True
            print(f"{self.username} is logged in")

    def logout(self):
        if self.is_logged_in:
            self.is_logged_in=False
            print(f"{self.username} is logged out")
        else:
            print(f"{self.username} is already logged out")

class Admin(User):

    def __init__(self,username, password):

        '''super is used to call the base class... 
            .__init__ ---> base class irrukara init method ah call pannu
            then we pass 2 arg one is username , password
            
            can_edit parperty or attribut craete painnaroim
        
        '''

        super().__init__(username,password)
        self.can_edit = True
        
    def update_details(self):
        if self.is_logged_in:
            print("Upadting Details")
        else:
            print(f"{self.username} is not logged IN")


admin_user = Admin("", "")


admin_user.login()
admin_user.login()

admin_user.logout()
admin_user.update_details()


admin_user.login()
admin_user.logout()
admin_user.update_details()






