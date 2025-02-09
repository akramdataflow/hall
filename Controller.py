from viow import *
from model import Model


class Controller:
    def __init__(self):
        self.view = MyView(self)
        self.model = Model()
        
        
        
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



#################الحجوزات
 
    def del_reser_show(self):
        self.show_del_reser =  Delreser(self)
        self.show_del_reser.show()

    


    def add_reservations_to_model(self, cos_name, cos_phone, hall , date ,datetime ,services,deposit ,remaining_amount):
        self.model.add_reservations( cos_name, cos_phone, hall , date ,datetime ,services,deposit ,remaining_amount)

    def get_reservations_from_model(self):
        return self.model.get_reservations()


    def del_reservations_from_model(self,reservations_id):
        self.model.del_reservations(reservations_id)
        self.show_reservation()

    def update_reser_show(self):
        self.show_update_reser = Updatereser(self)
        self.show_update_reser.show()


    def update_reservations_to_model(self, reservations_id,  cos_name, cos_phone, hall , date ,datetime ,services,deposit ,remaining_amount):
        self.model.update_reservations(reservations_id, cos_name, cos_phone, hall , date ,datetime ,services,deposit ,remaining_amount)
        self.show_reservation()

################الخدمات



    def add_services_to_model(self,  food, refreshments, photography , others):
        self.model.add_services( food, refreshments, photography , others)

    def get_services_from_model(self):
        return self.model.get_services()



    def update_serv_show(self):
        self.show_update_serv = Updatserve(self)
        self.show_update_serv.show()


    def update_services_to_model(self, services_id,   food, refreshments, photography , others):
        self.model.update_services(services_id,  food, refreshments, photography , others)
        self.show_Services()


###############3القاغه


    def del_hall_show(self):
        self.show_del_hall =  Delhall(self)
        self.show_del_hall.show()

    

    def add_hall_to_model(self, hall_num, tabels):
        self.model.add_hall( hall_num, tabels)

    def get_hall_from_model(self):
        return self.model.get_hall()


    def del_hall_from_model(self,hall_id):
        self.model.del_hall(hall_id)
        self.show_Add()

    def update_hall_show(self):
        self.show_update_hall = Updathall(self)
        self.show_update_hall.show()


    def update_hall_to_model(self, hall_id,  hall_num, tabels):
        self.model.update_hall(hall_id, hall_num, tabels)
        self.show_Add()


#########المشتريات


    def add_purchases_to_model(self,mat, price ,date):
        self.model.add_purchases( mat, price ,date)

    def get_purchases_from_model(self):
        return self.model.get_purchases()



    def update_purch_show(self):
        self.show_update_purch = Updatepurch(self)
        self.show_update_purch.show()


    def update_purchases_to_model(self, purchases_id,  mat, price ,date):
        self.model.update_purchases(purchases_id, mat, price ,date)
        self.show_buying()

 ####الرواتب


 
    def add_salaries_to_model(self,employ, em_phone ,wage):
        self.model.add_salaries( employ, em_phone ,wage)

    def get_salaries_from_model(self):
        return self.model.get_salaries()



    def update_salar_show(self):
        self.show_update_salar = Updatesalar(self)
        self.show_update_salar.show()


    def update_salaries_to_model(self, salaries_id,  employ, em_phone ,wage):
        self.model.update_salaries(salaries_id, employ, em_phone ,wage)
        self.show_Salaries()

               