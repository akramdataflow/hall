import sys 
from PySide6.QtWidgets import QSpinBox, QMainWindow, QPushButton, QGridLayout, QFrame, QVBoxLayout, QLabel , QLineEdit , QSizePolicy ,QTableWidget ,QHeaderView , QTableWidgetItem ,  QDateEdit 
from PySide6.QtGui import QIcon, QFont 
from PySide6.QtCore import Qt, QSize , QDate




class MyView(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller

        self.setGeometry(100, 200, 800, 1000)


        main_frame = QFrame()
        main_frame.setStyleSheet(
            """background-color: #fff"""
        )
        layout = QGridLayout(main_frame)

        label_frame = QFrame()
        label_frame_layout = QVBoxLayout(label_frame)
        label_frame.setStyleSheet("""
                                  background-color: #1A3654; 
                                  color: white;
                                  background-image: url('./static/Group 129.png');
                                  background-repeat: no-repeat;
                                  background-position: center;
                                  """)
        label_frame.setFixedHeight(100)
        label_frame.setGeometry(0, 0, 800, 1000)

        
        

        



        layout.addWidget(label_frame, 0, 0)

        self.setCentralWidget(main_frame)

        frame = QFrame()
        frame_layout = QGridLayout(frame)
        layout.addWidget(frame, 1, 0)

        icon = QIcon('./static/Untitled (4).png')


        # Button 1
        button1 = QPushButton()
        button1.clicked.connect(controller.show_reservation)
        button1.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 121 (1).png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button1.setIcon(icon)
        button1.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button1, 0, 0)



        # Button 2
        button2 = QPushButton()
        button2.clicked.connect(controller.show_Add)
        button2.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 122 (1).png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button2.setIcon(icon)
        button2.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button2, 0, 1)

       

        # Button 3
        button3 = QPushButton()
        button3.clicked.connect(controller.show_Services)
        button3.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 123.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button3.setIcon(icon)
        button3.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button3, 0, 2)

        
        # Button 
        button4 = QPushButton()
        button4.clicked.connect(controller.show_Settings)
        button4.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 125.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button4.setIcon(icon)
        button4.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button4, 1, 2)

        button5 = QPushButton()
        button5.clicked.connect(controller.show_Payments)
        button5.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 128.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button5.setIcon(icon)       
        button5.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button5, 1, 1)



        # Button 6
        button6 = QPushButton()
        button6.clicked.connect(controller.show_Reports)
        button6.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 126.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button6.setIcon(icon)       
        button6.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button6, 1, 0)

                                      
class reservation(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle(" الحجوزات  ")
        self.resize(500, 500) 

        self.showMaximized()

        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/Group 130.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)


         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_reservations_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(9)  # عدد الأعمدة (المادة، العدد، اسم الشركة، سعر الشراء ,سعر البيع ,تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels(['اسم الزبون', ' رقم الهاتف', 'القاعة', 'تاريخ الحجز ', ' وقت الحجز  ', 'العربون', ' المبلغ المتبقي  ', " الخدمات",'الترميز'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 8, QTableWidgetItem(str(data_tabel[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))
                self.table.setItem(row, 2, QTableWidgetItem(data_tabel[3][row]))   # إدخال اسم الشركة
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[4][row])))  # إدخال النوع
                self.table.setItem(row, 4, QTableWidgetItem(str(data_tabel[5][row])))
                self.table.setItem(row, 7, QTableWidgetItem(str(data_tabel[6][row])))  # إدخال العدد 
                self.table.setItem(row, 5, QTableWidgetItem(str(data_tabel[7][row]))) #الانتهاء
                self.table.setItem(row, 6, QTableWidgetItem(str(data_tabel[8][row]))) #الانتهاء
               
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 1, 0)
        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
       

       




        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)


           
   
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel(" اسم الزبون")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        self.cos_name = QLineEdit()
        self.cos_name.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget( self.cos_name, 0, 0)

        
        
   
        # البحث في فريم الجانبي لل (save frame layout)

        label_company = QLabel("رقم الزبون")
        label_company.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_company, 1, 1)

        self.cos_phone = QLineEdit()
        self.cos_phone.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget( self.cos_phone, 1, 0)



      
   
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("القاعة")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 2, 1)

        self.hall = QLineEdit()
        self.hall.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget( self.hall, 2, 0)

        ######
        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_number = QLabel(" تاريخ الحجز  ")
        label_number.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_number, 3, 1)

        self.date = QLineEdit()
        self.date.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.date, 3, 0)

 
    

        
        # البحث في فريم الجانبي لل (save frame layout)

        label_End_date = QLabel("وقت الحجز")
        label_End_date.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_End_date, 4, 1)

        self.datetime = QLineEdit()
        self.datetime.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget( self.datetime, 4, 0)

   
        label_age = QLabel("الخدمات")
        label_age.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_age, 5, 1)

        self.services = QLineEdit()
        self.services.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.services, 5, 0)


        
        label_age = QLabel("العربون")
        label_age.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_age, 6, 1)

        self.deposit = QLineEdit()
        self.deposit.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.deposit, 6, 0)

 
    
        label_age = QLabel("المبلغ المتبقي")
        label_age.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_age, 7, 1)

        self.remaining_amount = QLineEdit()
        self.remaining_amount.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.remaining_amount, 7, 0)



        





         #حفظ وتعديل 
       
        button1 = QPushButton()
        button1.clicked.connect(self.send_data_to_controller)
        button1.setStyleSheet("""
                   QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 29.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button1,8,0,1,2)



        button2 = QPushButton()
        button2.clicked.connect(self.controller.update_reser_show)
        button2.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 54 (2).png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button2,9,0,1,2)

        
        button3 = QPushButton()
        button3.clicked.connect(self.controller.del_reser_show)
        button3.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/Group 30 (1).png')  # تحميل الأيقونة
        button3.setIcon(icon)
        button3.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button3,10,0,1,2)

        
    def send_data_to_controller(self):
        # الحصول على البيانات من الواجهة
        cos_name = self.cos_name.text()
        cos_phone = self.cos_phone.text()
        hall = self.hall.text()
        date = self.date.text()
        datetime = self.datetime.text()
        services = self.services.text()
        deposit = self.deposit.text()
        remaining_amount = self.remaining_amount.text()

        # إرسال البيانات إلى الكونترولر لإضافتها للنموذج
        self.controller.add_reservations_to_model( cos_name, cos_phone, hall , date ,datetime ,services,deposit ,remaining_amount)

        # تحديث الجدول بعد الحفظ
        self.refresh_table()

    def refresh_table(self):
        # استرجاع البيانات من النموذج عبر الكونترولر
        data_table = self.controller.get_reservations_from_model()

        # مسح البيانات القديمة في الجدول
        self.table.setRowCount(0)

        # تعبئة الجدول بالبيانات الجديدة
        if data_table and len(data_table[0]) > 0:
            row_count = len(data_table[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)

            
            for row in range(row_count):
                self.table.setItem(row, 9, QTableWidgetItem(str(data_table[0][row])))  # إدخال الاسم
                self.table.setItem(row, 0, QTableWidgetItem(data_table[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_table[2][row]))  # إدخال النوع
                self.table.setItem(row, 2, QTableWidgetItem(str(data_table[3][row])))  # إدخال العدد
                self.table.setItem(row, 3, QTableWidgetItem(str(data_table[4][row])))
                self.table.setItem(row, 4, QTableWidgetItem(str(data_table[5][row])))  # إدخال الاسم
                self.table.setItem(row, 5, QTableWidgetItem(data_table[6][row]))  # إدخال الاسم
                self.table.setItem(row, 6, QTableWidgetItem(data_table[7][row]))  # إدخال النوع
                self.table.setItem(row, 7, QTableWidgetItem(str(data_table[8][row])))  # إدخال العدد
                self.table.setItem(row, 8, QTableWidgetItem(str(data_table[9][row])))

                                             
class Add(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle(" اضافة قاعة  ")
        self.resize(500, 500) 

        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/Group 131.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)


        
         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_hall_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(3)  
        self.table.setHorizontalHeaderLabels(['رقم القاعة', ' عدد الطاولات   ','الترميز'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 2, QTableWidgetItem(str(data_tabel[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))
                
              
               
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 1, 0)
        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)

        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        

       




        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)


        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel(" رقم القاعة ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        self.hall_num = QLineEdit()
        self.hall_num.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.hall_num, 0, 0)

        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_company = QLabel("عدد الطولات")
        label_company.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_company, 1, 1)

        self.tabels = QLineEdit()
        self.tabels.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.tabels, 1, 0)


        button1 = QPushButton()
        button1.clicked.connect(self.send_data_to_controller)
        button1.setStyleSheet("""
                   QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 29.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button1,2,0,1,2)



        button2 = QPushButton()
        button2.clicked.connect(self.controller.update_hall_show)
        button2.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 54 (2).png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button2,3,0,1,2)

        button3 = QPushButton()
        button3.clicked.connect(self.controller.del_hall_show)
        button3.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 30 (1).png')  # تحميل الأيقونة
        button3.setIcon(icon)
        button3.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button3,4,0,1,2)

          
    def send_data_to_controller(self):
        # الحصول على البيانات من الواجهة
        hall_num = self.hall_num.text()
        tabels = self.tabels.text()
        

        # إرسال البيانات إلى الكونترولر لإضافتها للنموذج
        self.controller.add_hall_to_model( hall_num, tabels)

        # تحديث الجدول بعد الحفظ
        self.refresh_table()

    def refresh_table(self):
        # استرجاع البيانات من النموذج عبر الكونترولر
        data_table = self.controller.get_hall_from_model()

        # مسح البيانات القديمة في الجدول
        self.table.setRowCount(0)

        # تعبئة الجدول بالبيانات الجديدة
        if data_table and len(data_table[0]) > 0:
            row_count = len(data_table[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)

            
            for row in range(row_count):
                self.table.setItem(row, 2, QTableWidgetItem(str(data_table[0][row])))  # إدخال الاسم
                self.table.setItem(row, 0, QTableWidgetItem(data_table[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_table[2][row]))  # إدخال النوع
              


                                       
class Services(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle(" الخدمات  ")
        self.resize(500, 500) 

        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/Group 132.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)

        ###


         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_services_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(5)  # عدد الأعمدة (المادة، العدد، اسم الشركة، سعر الشراء ,سعر البيع ,تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels(['المأكولات ', ' المرطبات  ', 'التصوير', 'أخرى  ','الترميز'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 4, QTableWidgetItem(str(data_tabel[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))
                self.table.setItem(row, 2, QTableWidgetItem(data_tabel[3][row]))   # إدخال اسم الشركة
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[4][row])))  # إدخال النوع
              
               
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 1, 0)
        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
       
        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        # save_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

       




        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)


        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel(" المأكولات ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        self.food = QLineEdit()
        self.food.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.food, 0, 0)

        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_company = QLabel("المرطبات")
        label_company.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_company, 1, 1)

        self.refreshments = QLineEdit()
        self.refreshments.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.refreshments, 1, 0)



        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("التصوير")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 2, 1)

        self.photography = QLineEdit()
        self.photography.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget( self.photography, 2, 0)


    
    
    
        


        label_history = QLabel("أخرى")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 3, 1)

        self.others = QLineEdit()
        self.others .setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.others , 3, 0)




         #حفظ وتعديل 
       
        button1 = QPushButton()
        button1.clicked.connect(self.send_data_to_controller)
        button1.setStyleSheet("""
                   QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 29.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button1,4,0,1,2)



        button2 = QPushButton()
        button2.clicked.connect(self.controller.update_serv_show)
        button2.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 54 (2).png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button2,5,0,1,2)

           
    def send_data_to_controller(self):
        # الحصول على البيانات من الواجهة
        food = self.food.text()
        refreshments = self.refreshments.text()
        photography = self.photography.text()
        others = self.others.text()
        

        # إرسال البيانات إلى الكونترولر لإضافتها للنموذج
        self.controller.add_services_to_model(  food, refreshments, photography , others)

        # تحديث الجدول بعد الحفظ
        self.refresh_table()

    def refresh_table(self):
        # استرجاع البيانات من النموذج عبر الكونترولر
        data_table = self.controller.get_services_from_model()

        # مسح البيانات القديمة في الجدول
        self.table.setRowCount(0)

        # تعبئة الجدول بالبيانات الجديدة
        if data_table and len(data_table[0]) > 0:
            row_count = len(data_table[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)

            
            for row in range(row_count):
                self.table.setItem(row, 4, QTableWidgetItem(str(data_table[0][row])))  # إدخال الاسم
                self.table.setItem(row, 0, QTableWidgetItem(data_table[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_table[2][row]))  # إدخال النوع
                self.table.setItem(row, 2, QTableWidgetItem(str(data_table[3][row])))  # إدخال العدد
                self.table.setItem(row, 3, QTableWidgetItem(str(data_table[4][row])))
               

                                      
class Reports(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle(" التقارير  ")
        self.resize(500, 500) 

        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)



        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0)  # الهيدر 

        ## 
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/Group 133.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)

        frame = QFrame()
        frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        
        new_layout.addWidget(frame,3,0)
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        #انشاء افريم للعلى من الابيض 
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        app_frame_layout = QGridLayout(save_frame)


        
        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        app_frame_layout.addWidget(label,1,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,2,0)


        label_history = QLabel("الى")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        app_frame_layout.addWidget(label_history, 0, 1)

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        app_frame_layout.addWidget(history_input, 0, 0)


        label_history = QLabel("  التاريخ من ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        app_frame_layout.addWidget(label_history, 0, 3)

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        app_frame_layout.addWidget(history_input, 0, 2)

                                      
class Payments(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle(" المدفوعات  ")
        self.resize(500, 500) 


        main_frame = QFrame()
        main_frame.setStyleSheet(
            """background-color: #1A3654"""
        )
        layout = QGridLayout(main_frame)

        label_frame = QFrame()
        label_frame_layout = QVBoxLayout(label_frame)
        label_frame.setStyleSheet("""
                                  background-color: #50F296; 
                                  color: white;
                                  background-image: url('./static/Group 134.png');
                                  background-repeat: no-repeat;
                                  background-position: center;
                                  """)
        label_frame.setFixedHeight(60)
        label_frame.setGeometry(0, 0, 800, 1000)

        
        layout.addWidget(label_frame, 0, 0)

        self.setCentralWidget(main_frame)

        frame = QFrame()
        frame_layout = QGridLayout(frame)
        layout.addWidget(frame, 1, 0)

        icon = QIcon('./static/Untitled (4).png')


        
        # Button 1
        button1 = QPushButton()
        button1.clicked.connect(controller.show_buying)
        button1.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 135.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button1.setIcon(icon)
        button1.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button1, 0, 0)



        # Button 2
        button2 = QPushButton()
        button2.clicked.connect(controller.show_Salaries)
        button2.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 136.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button2.setIcon(icon)
        button2.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button2, 0, 1)

                                     
class buying(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle(" المشتريات  ")
        self.resize(500, 500) 

        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/Group 138.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)


        #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_purchases_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(4)  # عدد الأعمدة (المادة، العدد، اسم الشركة، سعر الشراء ,سعر البيع ,تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels([' المادة', '  السعر', 'التاريخ','الترميز'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))
                self.table.setItem(row, 2, QTableWidgetItem(data_tabel[3][row]))   # إدخال اسم الشركة
               
               
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 1, 0)

        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        

       




        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)


        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("  المادة ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        self.mat = QLineEdit()
        self.mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.mat, 0, 0)

        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_company = QLabel(" السعر")
        label_company.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_company, 1, 1)

        self.price = QLineEdit()
        self.price.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.price, 1, 0)

        

        label_company = QLabel(" التاريخ")
        label_company.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_company, 2, 1)

        self.date = QLineEdit()
        self.date.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.date, 2, 0)



        button1 = QPushButton()
        button1.clicked.connect(self.send_data_to_controller)
        button1.setStyleSheet("""
                   QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 29.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button1,3,0,1,2)

        



        button2 = QPushButton()
        button2.clicked.connect(self.controller.update_purch_show)
        button2.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 54 (2).png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button2,4,0,1,2)

           
    def send_data_to_controller(self):
        # الحصول على البيانات من الواجهة
        mat = self.mat.text()
        price = self.price.text()
        date = self.date.text()
       

        # إرسال البيانات إلى الكونترولر لإضافتها للنموذج
        self.controller.add_purchases_to_model( mat, price, date )

        # تحديث الجدول بعد الحفظ
        self.refresh_table()

    def refresh_table(self):
        # استرجاع البيانات من النموذج عبر الكونترولر
        data_table = self.controller.get_purchases_from_model()

        # مسح البيانات القديمة في الجدول
        self.table.setRowCount(0)

        # تعبئة الجدول بالبيانات الجديدة
        if data_table and len(data_table[0]) > 0:
            row_count = len(data_table[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)

            
            for row in range(row_count):
                self.table.setItem(row, 3, QTableWidgetItem(str(data_table[0][row])))  # إدخال الاسم
                self.table.setItem(row, 0, QTableWidgetItem(data_table[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_table[2][row]))  # إدخال النوع
                self.table.setItem(row, 2, QTableWidgetItem(str(data_table[3][row])))  # إدخال العدد
             





                                     
class Salaries(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle(" الرواتب  ")
        self.resize(500, 500)

        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/Group 137.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)


        #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_salaries_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(4)  # عدد الأعمدة (المادة، العدد، اسم الشركة، سعر الشراء ,سعر البيع ,تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels([' اسم الموظف', '  رقم الهاتف', 'الراتب','الترميز'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))
                self.table.setItem(row, 2, QTableWidgetItem(data_tabel[3][row]))   # إدخال اسم الشركة
               
               
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 1, 0)

        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        

       




        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)


        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel(" اسم الموظف ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        self.employ = QLineEdit()
        self.employ.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.employ, 0, 0)

        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_company = QLabel("رقم الهاتف")
        label_company.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_company, 1, 1)

        self.em_phone = QLineEdit()
        self.em_phone.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.em_phone, 1, 0)

        

        label_company = QLabel(" الراتب")
        label_company.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_company, 2, 1)

        self.wage = QLineEdit()
        self.wage.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.wage, 2, 0)



        button1 = QPushButton()
        button1.clicked.connect(self.send_data_to_controller)
        button1.setStyleSheet("""
                   QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 29.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button1,3,0,1,2)

        



        button2 = QPushButton()
        button2.clicked.connect(self.controller.update_salar_show)
        button2.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 54 (2).png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button2,4,0,1,2)

              
    def send_data_to_controller(self):
        # الحصول على البيانات من الواجهة
        employ = self.employ.text()
        em_phone = self.em_phone.text()
        wage = self.wage.text()
       

        # إرسال البيانات إلى الكونترولر لإضافتها للنموذج
        self.controller.add_salaries_to_model( employ, em_phone, wage )

        # تحديث الجدول بعد الحفظ
        self.refresh_table()

    def refresh_table(self):
        # استرجاع البيانات من النموذج عبر الكونترولر
        data_table = self.controller.get_salaries_from_model()

        # مسح البيانات القديمة في الجدول
        self.table.setRowCount(0)

        # تعبئة الجدول بالبيانات الجديدة
        if data_table and len(data_table[0]) > 0:
            row_count = len(data_table[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)

            
            for row in range(row_count):
                self.table.setItem(row, 3, QTableWidgetItem(str(data_table[0][row])))  # إدخال الاسم
                self.table.setItem(row, 0, QTableWidgetItem(data_table[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_table[2][row]))  # إدخال النوع
                self.table.setItem(row, 2, QTableWidgetItem(str(data_table[3][row])))  # إدخال العدد
             

                                     
class Settings(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle(" الاعدادت  ")
        self.resize(500, 500) 

        
        main_frame = QFrame()
        main_frame.setStyleSheet(
            """background-color: #1A3654"""
        )
        layout = QGridLayout(main_frame)

        label_frame = QFrame()
        label_frame_layout = QVBoxLayout(label_frame)
        label_frame.setStyleSheet("""
                                  background-color: #50F296; 
                                  color: white;
                                  background-image: url('./static/Group 139.png');
                                  background-repeat: no-repeat;
                                  background-position: center;
                                  """)
        label_frame.setFixedHeight(60)
        label_frame.setGeometry(0, 0, 800, 1000)

        
        layout.addWidget(label_frame, 0, 0)

        self.setCentralWidget(main_frame)

        frame = QFrame()
        frame_layout = QGridLayout(frame)
        layout.addWidget(frame, 1, 0)

        icon = QIcon('./static/Untitled (4).png')


        
        # Button 1
        button1 = QPushButton()
        button1.clicked.connect(controller.show_password)
        button1.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 141.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button1.setIcon(icon)
        button1.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button1, 0, 0)



        # Button 2
        button2 = QPushButton()
        button2.clicked.connect(controller.show_user)
        button2.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 143.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button2.setIcon(icon)
        button2.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button2, 0, 1)


                                              
class user(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle(" المستخدمين  ")
        self.resize(500, 500) 

        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/Group 144.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)


         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        frame.setFixedHeight(700)
        new_layout.addWidget(frame,1,0)
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        # save_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

       




        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)


        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel(" اسم المستخدم ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 0, 0)

        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_company = QLabel("رقم الهاتف")
        label_company.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_company, 1, 1)

        company_input = QLineEdit()
        company_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(company_input, 1, 0)



        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("اسم الدخول")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 2, 1)

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 2, 0)


        label_history = QLabel("كلمة المرور ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 3, 1)

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 3, 0)


        label_history = QLabel("أضافة صورة ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 4, 1)

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 4, 0)




         #حفظ وتعديل 
       
        button1 = QPushButton()
        button1.setStyleSheet("""
                   QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 29.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button1,5,0,1,2)



        button2 = QPushButton()
        button2.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 54 (2).png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button2,6,0,1,2)

                                             
class password(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle(" كلمة المرور  ")
        self.resize(500, 500) 

        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/Group 121.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)


         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        frame_layout = QGridLayout(frame)
        frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        new_layout.addWidget(frame)
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

       

        
        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        frame_layout.addWidget(label)


        label_history = QLabel(" كلمة المرور الجديدة  ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        frame_layout.addWidget(label_history, 0, 1)

       
       
        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        frame_layout.addWidget(history_input, 0, 0)

        label_history = QLabel(" تاكيد كلمة المرور  ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        frame_layout.addWidget(label_history, 1, 1)

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        frame_layout.addWidget(history_input, 1, 0)

        button1 = QPushButton()
        button1.setStyleSheet("""
                   QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 29.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        frame_layout.addWidget(button1,4,0,1,2)


####################الحجوزات 



class Delreser(QMainWindow):


    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("حذف المادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد حذفه')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.id_mat = QLineEdit('')
        self.id_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.id_mat,0,0)

        button1 = QPushButton()
        button1.clicked.connect(self.send_id_reser_to_controller)
        button1.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/Group 30 (1).png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        new_layout.addWidget(button1,1,0,1,2)

    def send_id_reser_to_controller(self):
        id_reser = self.id_mat.text()
        self.controller.del_reservations_from_model(id_reser)



class Updatereser(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تعديل مادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد تعديله')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.purch_id = QLineEdit()
        self.purch_id.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.purch_id,0,0)


        label = QLabel('اسم الزبون')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,1,1)

        self.cos_name = QLineEdit()
        self.cos_name.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.cos_name,1,0)
 

        label = QLabel('رقم الزبون')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,2,1)

        self.cos_phone = QLineEdit()
        self.cos_phone.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.cos_phone,2,0)

        

        label = QLabel('القاعة')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,3,1)

        self.hall = QLineEdit()
        self.hall.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.hall,3,0)





        label = QLabel('تاريخ الحجز')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,4,1)



        self.date = QLineEdit()
        self.date.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.date,4,0)
        
        


        

        label = QLabel('وقت الحجز')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,5,1)



        self.datetime = QLineEdit()
        self.datetime.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.datetime,5,0)


        label = QLabel('الخدمات')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,6,1)



        self.services = QLineEdit()
        self.services.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.services,6,0)
        


        label = QLabel('العربون')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,7,1)



        self.deposit = QLineEdit()
        self.deposit.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.deposit,7,0)




        label = QLabel('المبلغ المتبقي ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,8,1)



        self.remaining_amount = QLineEdit()
        self.remaining_amount.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.remaining_amount,8,0)
        






 

        button = QPushButton()
        button.clicked.connect(self.send_update_reser_to_controller)
        button.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/Group 54 (2).png')  # تحميل الأيقونة
        button.setIcon(icon)
        button.setIconSize(QSize(90, 36))

        new_layout.addWidget(button,9,0,1,2)

    def send_update_reser_to_controller(self):
        purch_id = self.purch_id.text()
        cos_name = self.cos_name.text()
        cos_phone = self.cos_phone.text()
        hall = self.hall.text()
        date = self.date.text()
        datetime = self.datetime.text()
        services = self.services.text()
        deposit = self.deposit.text()
        remaining_amount = self.remaining_amount.text()
       
        
        
        self.controller.update_reservations_to_model(purch_id, cos_name,cos_phone,hall,date, datetime ,services ,deposit,remaining_amount )


###########الخدمات


class Updatserve(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تعديل مادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد تعديله')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.serv_id = QLineEdit()
        self.serv_id.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.purchserv_id_id,0,0)


        label = QLabel('المأكولات')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,1,1)

        self.food = QLineEdit()
        self.food.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.food,1,0)
 

        label = QLabel('المرطبات')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,2,1)

        self.refreshments = QLineEdit()
        self.refreshments.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.refreshments,2,0)

        

        label = QLabel('التصوير')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,3,1)

        self.photography = QLineEdit()
        self.photography.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.photography,3,0)





        label = QLabel('أخرى ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,4,1)



        self.others = QLineEdit()
        self.others.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.others,4,0)
        
        


        
        






 

        button = QPushButton()
        button.clicked.connect(self.send_update_reser_to_controller)
        button.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/Group 54 (2).png')  # تحميل الأيقونة
        button.setIcon(icon)
        button.setIconSize(QSize(90, 36))

        new_layout.addWidget(button,5,0,1,2)

    def send_update_reser_to_controller(self):
        serv_id = self.serv_id.text()
        food = self.food.text()
        refreshments = self.refreshments.text()
        photography = self.photography.text()
        others = self.others.text()
        
        
        
        self.controller.update_services_to_model(serv_id,  food, refreshments, photography , others )


#########قاعه

class Delhall(QMainWindow):


    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("حذف المادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد حذفه')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.id_hall = QLineEdit('')
        self.id_hall.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.id_hall,0,0)

        button1 = QPushButton()
        button1.clicked.connect(self.send_id_hall_to_controller)
        button1.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/Group 30 (1).png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        new_layout.addWidget(button1,1,0,1,2)

    def send_id_hall_to_controller(self):
        id_hal = self.id_hall.text()
        self.controller.del_hall_from_model(id_hal)


class Updathall(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تعديل مادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد تعديله')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.hall_id = QLineEdit()
        self.hall_id.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.hall_id,0,0)


        label = QLabel('رقم القاعة')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,1,1)

        self.hall_num = QLineEdit()
        self.hall_num.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.hall_num,1,0)
 

        label = QLabel('عدد الطاولات')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,2,1)

        self.tabels = QLineEdit()
        self.tabels.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.tabels,2,0)

 

        button = QPushButton()
        button.clicked.connect(self.send_update_hall_to_controller)
        button.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/Group 54 (2).png')  # تحميل الأيقونة
        button.setIcon(icon)
        button.setIconSize(QSize(90, 36))

        new_layout.addWidget(button,3,0,1,2)

    def send_update_hall_to_controller(self):
        hal_id = self.hall_id.text()
        hall_num = self.hall_num.text()
        tabels = self.tabels.text()
       
        
        
        
        self.controller.update_hall_to_model(hal_id,  hall_num, tabels )


########المشتريات



class Updatepurch(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تعديل مادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد تعديله')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.pruch_id = QLineEdit()
        self.pruch_id.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.pruch_id,0,0)


        label = QLabel('المادة ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,1,1)

        self.mat = QLineEdit()
        self.mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.mat,1,0)
 

        label = QLabel('السعر ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,2,1)

        self.price = QLineEdit()
        self.price.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.price,2,0)

        
        label = QLabel('التاريخ ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,3,1)

        self.date = QLineEdit()
        self.date.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.date,3,0)

 

        button = QPushButton()
        button.clicked.connect(self.send_update_purchases_to_controller)
        button.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/Group 54 (2).png')  # تحميل الأيقونة
        button.setIcon(icon)
        button.setIconSize(QSize(90, 36))

        new_layout.addWidget(button,4,0,1,2)

    def send_update_purchases_to_controller(self):
        purchases_id = self.pruch_id.text()
        mat = self.mat.text()
        price = self.price.text()
        date = self.date.text()
        
       
        
        
        
        self.controller.update_purchases_to_model(purchases_id,  mat, price , date )

####33الرواتب



class Updatesalar(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تعديل مادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد تعديله')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.salar_id = QLineEdit()
        self.salar_id.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.salar_id,0,0)


        label = QLabel('اسم الموظف ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,1,1)

        self.employ = QLineEdit()
        self.employ.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.employ,1,0)
 

        label = QLabel('رقم الهاتف ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,2,1)

        self.em_phone = QLineEdit()
        self.em_phone.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.em_phone,2,0)

        
        label = QLabel('الراتب ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,3,1)

        self.wage = QLineEdit()
        self.wage.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.wage,3,0)

 

        button = QPushButton()
        button.clicked.connect(self.send_update_salaries_to_controller)
        button.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/Group 54 (2).png')  # تحميل الأيقونة
        button.setIcon(icon)
        button.setIconSize(QSize(90, 36))

        new_layout.addWidget(button,4,0,1,2)

    def send_update_salaries_to_controller(self):
        salaries_id = self.salar_id.text()
        employ = self.employ.text()
        em_phone = self.em_phone.text()
        wage = self.wage.text()
        
       
        
        
        
        self.controller.update_salaries_to_model(salaries_id,  employ, em_phone , wage )


