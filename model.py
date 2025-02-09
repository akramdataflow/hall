import sqlite3
from datetime import datetime

class Model:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')  
        self.cursor = self.conn.cursor()



      ##############الحجوزات

    def add_reservations(self, cos_name, cos_phone, hall , date ,datetime ,services,deposit ,remaining_amount):
        self.cursor.execute("INSERT INTO reservations (cos_name, cos_phone, hall , date ,datetime ,services,deposit ,remaining_amount) VALUES (?, ?, ?, ?,?, ?, ?, ?)", (cos_name, cos_phone, hall , date ,datetime ,services,deposit ,remaining_amount))
        self.conn.commit()
        
        
    def get_reservations(self):
        self.cursor.execute('SELECT * FROM reservations')
        rows = self.cursor.fetchall()  
        reser_id = [col[0] for col in rows] 
        cos_name = [col[1] for col in rows] 
        cos_phone = [str(col[2]) for col in rows]  # Convert to string
        hall = [col[3] for col in rows] 
        date = [col[4] for col in rows]
        datetime = [col[5] for col in rows]
        services = [col[6] for col in rows]
        deposit = [col[7] for col in rows]
        remaining_amount = [col[8] for col in rows]
        print(reser_id,  cos_name, cos_phone, hall , date ,datetime ,services,deposit ,remaining_amount)
        return reser_id,  cos_name, cos_phone, hall , date ,datetime ,services,deposit ,remaining_amount
        
        
    
    
    def del_reservations(self, reservations_id):
        self.cursor.execute("DELETE FROM reservations WHERE id = ?", (reservations_id,))
        self.conn.commit()



    def update_reservations(self, reservations_id, cos_name, cos_phone, hall , date ,datetime ,services,deposit ,remaining_amount):
        self.cursor.execute('''
            UPDATE reservations
            SET cos_name = ?,  cos_phone = ?, hall = ?, date = ? , datetime = ?,  services = ?, deposit = ?, remaining_amount = ?
            WHERE id = ?
        ''', (cos_name, cos_phone, hall , date ,datetime ,services,deposit ,remaining_amount,reservations_id))
        self.conn.commit()    
########################الخدمات

    


    def add_services(self, food, refreshments, photography , others ):
        self.cursor.execute("INSERT INTO services (food, refreshments, photography , others) VALUES (?, ?, ?, ?)", (food, refreshments, photography , others))
        self.conn.commit()
        
        
    def get_services(self):
        self.cursor.execute('SELECT * FROM services')
        rows = self.cursor.fetchall()  
        serv_id = [col[0] for col in rows] 
        food = [col[1] for col in rows] 
        refreshments = [str(col[2]) for col in rows]  # Convert to string
        photography = [col[3] for col in rows] 
        others = [col[4] for col in rows]
        
        print(serv_id,  food, refreshments, photography , others)
        return serv_id,  food, refreshments, photography , others
        
        
    

    def update_services(self, services_id,food, refreshments, photography , others):
        self.cursor.execute('''
            UPDATE services
            SET food = ?,  refreshments = ?, photography = ?, others = ?
            WHERE id = ?
        ''', (food, refreshments, photography , others,services_id))
        self.conn.commit()

        #########قاعة


        
    def add_hall(self, hall_num, tabels):
        self.cursor.execute("INSERT INTO hall (hall_num, tabels) VALUES (?, ?  )", (hall_num, tabels))
        self.conn.commit()
        
        
    def get_hall(self):
        self.cursor.execute('SELECT * FROM hall')
        rows = self.cursor.fetchall()  
        hall_id = [col[0] for col in rows] 
        hall_num = [col[1] for col in rows] 
        tabels = [str(col[2]) for col in rows]  
        print(hall_id,  hall_num, tabels)
        return hall_id,  hall_num, tabels
       
    
    def del_hall(self, hall_id):
        self.cursor.execute("DELETE FROM hall WHERE id = ?", (hall_id,))
        self.conn.commit()



    def update_hall(self, hall_id, hall_num, tabels):
        self.cursor.execute('''
            UPDATE hall
            SET hall_num = ?,  tabels = ?
            WHERE id = ?
        ''', (hall_num, tabels ,hall_id))
        self.conn.commit() 


        #########المشتربات

        
    def add_purchases(self, mat, price ,date  ):
        self.cursor.execute("INSERT INTO purchases (mat, price ,date) VALUES (?, ? , ?  )", (mat, price ,date))
        self.conn.commit()

          
    def get_purchases(self):
        self.cursor.execute('SELECT * FROM purchases')
        rows = self.cursor.fetchall()  
        purch_id = [col[0] for col in rows] 
        mat = [col[1] for col in rows] 
        price = [str(col[2]) for col in rows]  # Convert to string
        date = [col[3] for col in rows] 
        
        
        print(purch_id,mat, price ,date)
        return purch_id, mat, price ,date
    

    
    def update_purchases(self, purchases_id,mat, price ,date):
        self.cursor.execute('''
            UPDATE purchases
            SET mat = ?,  price = ?, date = ?
            WHERE id = ?
        ''', (mat, price ,date,purchases_id))
        self.conn.commit()  


        ####الرواتب


    
    def add_salaries(self,employ, em_phone ,wage  ):
        self.cursor.execute("INSERT INTO salaries (employ, em_phone ,wage) VALUES (?, ? , ?  )", (employ, em_phone ,wage))
        self.conn.commit() 

          
    def get_salaries(self):
        self.cursor.execute('SELECT * FROM salaries')
        rows = self.cursor.fetchall()  
        salr_id = [col[0] for col in rows] 
        employ = [col[1] for col in rows] 
        em_phone = [str(col[2]) for col in rows]  # Convert to string
        wage = [col[3] for col in rows] 
        
        
        print(employ, em_phone ,wage)
        return salr_id, employ, em_phone ,wage
    

    
    def update_salaries(self, salaries_id,employ, em_phone ,wage):
        self.cursor.execute('''
            UPDATE salaries
            SET employ = ?,  em_phone = ?, wage = ?
            WHERE id = ?
        ''', (employ, em_phone ,wage,salaries_id))
        self.conn.commit()  


        ##########المستخدم
        

       
        




