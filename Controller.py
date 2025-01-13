from viow import *


class Controller:
    def __init__(self):
        self.view = MyView(self)
        
        
        
    def show_reservation(self):
        self.show_reservation_add = reservation(self)
        self.show_reservation_add.show() 

    
    def show_Add(self):
        self.show_Add_add = Add(self)
        self.show_Add_add.show() 


            
    def show_Services(self):
        self.show_Services_add = Services(self)
        self.show_Services_add.show() 

    

    
    
        
    def show_Reports(self):
        self.show_Reports_add = Reports(self)
        self.show_Reports_add.show() 



            
    def show_Payments(self):
        self.show_Payments_add = Payments(self)
        self.show_Payments_add.show() 




        
            
    def show_buying(self):
        self.show_buying_add = buying(self)
        self.show_buying_add.show() 



            
    def show_Salaries(self):
        self.show_Salaries_add = Salaries(self)
        self.show_Salaries_add.show() 




              
   
   
   
   
   
   
   
   
    def show_Settings(self):
        self.show_Settings_add = Settings(self)
        self.show_Settings_add.show() 



        
    def show_user(self):
        self.show_user_add = user(self)
        self.show_user_add.show() 



        
    def show_password(self):
        self.show_password_add = password(self)
        self.show_password_add.show() 






