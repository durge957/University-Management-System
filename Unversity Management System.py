#Additional Features to be added
#1. To implement OTP Verification for Teacher & Student
#2. Display student of Only particular Branch
#3. display Teachers of only particular subject
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class person:
    def __init__(self,rollno,name,email):
        self.name = name
        self.rollno = rollno
        self.email = email
class student(person):
    def __init__(self,srollno,sname,semail,branch):
        super().__init__(srollno,sname,semail)
        self.branch = branch
class teacher(person):
    def __init__(self,trollno,tname,temail,subject):
        super().__init__(trollno,tname,temail)
        self.subject = subject
class college:
    def __init__(self,cid,cname):
        self.cid = cid
        self.cname = cname
        self.students = []
        self.teachers = []
    def add_student(self,student):
        self.students.append(student)
    def add_teacher(self,teacher): 
        self.teachers.append(teacher)
colleges = []

while True:
    print("Choose your Option")
    print("1. Add College ")
    print("2. Add Student ")
    print("3. Add Teacher ")
    print("4. Display Student Details ")
    print("5. Display Teacher Details ")
    print("6. Exit ")
    ip = int(input("Enter Your Option: "))
    if ip == 1:
        cname = input("Enter college Name: ")
        cid = input("Enter College Id: ")
        x = False
        for i in colleges:
            if i.cid == cid:
                x = True
                break
        if x == True:
            print("************************")
            print("College Already Exists !")
            print("************************")
        else:
            clg = college(cid,cname)
            colleges.append(clg)
            print("****************************")
            print("College Created sucessfullly")
            print("****************************")
        print(colleges)
    elif ip == 2:
        cid = input("Enter College id: ")
        x = False
        clg = None
        for i in colleges:
            if i.cid == cid:
                x = True
                clg = i
                break
        if x == True:
            name = input("Enter Student Name: ")
            roll = input("Enter Student Roll number: ")
            email = input("Enter Student Email: ")
            branch = input("Enter Student Branch: ")
            s = student(roll,name,email,branch)
            
            otp = random.randint(1000, 9999)
            months = {1:"January",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"Decemeber"}
            date = int(input("Enter Your Date of Birth: "))
            month = int(input("Enter your Month of birth: "))
            Year = int(input("Enter your Year: "))
            subject = "OTP For Verification"
            body = f"Hello {name} !\nroll no : {roll} \nbranch : {branch} \nDate of Birth : {date} - {months[month]}\nYour Secret OTP is {otp}"

            msg = MIMEMultipart()
            msg['From'] = "durgeshsai555@gmail.com"
            msg['To'] = email
            msg['Subject'] = subject
            msg.attach(MIMEText(body,'plain'))
            
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login("durgeshsai555@gmail.com","ahgz dtgk dekf nsvo")
            server.send_message(msg)
            server.quit()
            
            print(f"An OTP has been sent to your email {email}, Please enter it to proceed.")
            uotp=int(input('Enter OTP:'))
            if otp==uotp:
                print('OTP verified')
                clg.add_student(s)
                print("*************************")
                print("Student added Sucessfully!")
                print("*************************")
            else:
                print('OTP invalid')
                print("*************************")
                print("Student not added!")
                print("*************************")
        else:
            print("************************")
            print("College Does not Exists !")
            print("************************")
    elif ip == 3:
        cid = input("Enter College id: ")
        x = False
        clg = None
        for i in colleges:
            if i.cid == cid:
                x = True
                clg = i
                break
        if x == True:
            name = input("Enter Teacher Name: ")
            roll = input("Enter Teacher Roll number: ")
            email = input("Enter Teacher Email: ")
            subject = input("Enter Teacher Subject: ")
            t = teacher(roll,name,email,subject)
            
            otp = random.randint(1000, 9999)
            months = {1:"January",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"Decemeber"}
            date = int(input("Enter Your Date of Birth: "))
            month = int(input("Enter your Month of birth: "))
            Year = int(input("Enter your Year: "))
            subject = "OTP For Verification"
            body = f"Hello {name} !\nroll : {roll} \n subject : {subject} \nDate of Birth : {date} - {months[month]}\nYour Secret OTP is {otp}"

            msg = MIMEMultipart()
            msg['From'] = "durgeshsai555@gmail.com"
            msg['To'] = email
            msg['Subject'] = subject
            msg.attach(MIMEText(body,'plain'))
            
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login("durgeshsai555@gmail.com","ahgz dtgk dekf nsvo")
            server.send_message(msg)
            server.quit()
            print(f"An OTP has been sent to your email {email}, Please enter it to proceed.")
            uotp=int(input('Enter OTP:'))
            if otp==uotp:
                print('OTP verified')
                clg.add_teacher(t)
                print("*************************")
                print("Teacher added Sucessfully!")
                print("*************************")
            else:
                print('OTP invalid')
                print("*************************")
                print("Teacher not added!")
                print("*************************")
    elif ip == 4:
        cid = input("Enter College id: ")
        x = False
        clg = None
        for i in colleges:
            if i.cid == cid:
                x = True
                clg = i
                break
        if x == True:
            students = clg.students
            print("**********************************")
            print(f"Student Deatils of {clg.cname}: ")
            for x in students:
                print()
                print(f"Student Roll Number: {x.rollno}")
                print(f"Student Name: {x.name}")
                print(f"Student Email: {x.email}")
                print(f"Student Branch: {x.branch}")
            print()
            print("**********************************")
        else:
            print("************************")
            print("College Does not Exists !")
            print("************************")
    elif ip == 5:
        cid = input("Enter College id: ")
        x = False
        clg = None
        for i in colleges:
            if i.cid == cid:
                x = True
                clg = i
                break
        if x == True:
            teachers = clg.teachers
            if len(teachers) == 0:
                print("************************")
                print("No Teacher Exits")
                print("************************")
            else:
                print("**********************************")
                print(f"Teacher Deatils of {clg.cname}: ")
                for x in teachers:
                    print()
                    print(f"Teacher Roll Number: {x.rollno}")
                    print(f"Teacher Name: {x.name}")
                    print(f"Teacher Email: {x.email}")
                    print(f"Teacher Subject: {x.subject}")
                print()
                print("**********************************")
        else:
            print("************************")
            print("College Does not Exists !")
            print("************************")
    else:
        print("************************")
        print("Thanks! Visit Again ")
        print("************************")
        break
