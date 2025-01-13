import sys 
from PySide6.QtWidgets import QSpinBox, QMainWindow, QPushButton, QGridLayout, QFrame, QVBoxLayout, QLabel , QLineEdit , QSizePolicy
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, QSize




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

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 0, 0)

        
        
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

        company_input = QLineEdit()
        company_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(company_input, 1, 0)



        
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

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 2, 0)

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

        number_input = QLineEdit()
        number_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(number_input, 3, 0)



        
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

        End_date_input = QLineEdit()
        End_date_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(End_date_input, 4, 0)

        
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

        age_input = QLineEdit()
        age_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(age_input, 5, 0)


        
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

        age_input = QLineEdit()
        age_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(age_input, 6, 0)


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

        age_input = QLineEdit()
        age_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(age_input, 7, 0)



        





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
        
        save_frame_layout.addWidget(button1,8,0,1,2)



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
        
        save_frame_layout.addWidget(button2,9,0,1,2)

                                              
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
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/Group 131.png')  
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

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 0, 0)

        
        
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

        company_input = QLineEdit()
        company_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(company_input, 1, 0)


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
        
        save_frame_layout.addWidget(button1,2,0,1,2)



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
        
        save_frame_layout.addWidget(button2,3,0,1,2)


                                       
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

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 0, 0)

        
        
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

        company_input = QLineEdit()
        company_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(company_input, 1, 0)



        
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

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 2, 0)


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
        
        save_frame_layout.addWidget(button1,3,0,1,2)



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
        
        save_frame_layout.addWidget(button2,4,0,1,2)

                                      
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

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 0, 0)

        
        
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

        company_input = QLineEdit()
        company_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(company_input, 1, 0)

        

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

        company_input = QLineEdit()
        company_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(company_input, 2, 0)



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
        
        save_frame_layout.addWidget(button1,3,0,1,2)

        



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
        
        save_frame_layout.addWidget(button2,4,0,1,2)

                                     
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

        company_input = QLineEdit()
        company_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(company_input, 2, 0)



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
        
        save_frame_layout.addWidget(button1,3,0,1,2)

        



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
        
        save_frame_layout.addWidget(button2,4,0,1,2)






















                                       
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


