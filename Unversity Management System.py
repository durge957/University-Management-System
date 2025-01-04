class person:
    def __init__(self, rollno, name, email):
        self.name = name
        self.rollno = rollno
        self.email = email

class student(person):
    def __init__(self, srollno, sname, semail, branch):
        super().__init__(srollno, sname, semail)
        self.branch = branch

class teacher(person):
    def __init__(self, trollno, tname, temail, subject):
        super().__init__(trollno, tname, temail)
        self.subject = subject

class college:
    def __init__(self, cid, cname):
        self.cid = cid
        self.cname = cname
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

colleges = []
while True:
    print("\nChoose your Option")
    print("1. Add College ")
    print("2. Add Student ")
    print("3. Add Teacher ")
    print("4. Display Student Details ")
    print("5. Display Teachers of Particular Subject")
    print("6. Display Students of Particular Branch")
    print("7. Exit ")
    ip = int(input("Enter Your Option: "))

    if ip == 1:
        cname = input("Enter college Name: ")
        cid = input("Enter College Id: ")
        if any(clg.cid == cid for clg in colleges):
            print("************************")
            print("College Already Exists!")
            print("************************")
        else:
            clg = college(cid, cname)
            colleges.append(clg)
            print("****************************")
            print("College Created Successfully")
            print("****************************")
    elif ip == 2:
        cid = input("Enter College id: ")
        clg = next((c for c in colleges if c.cid == cid), None)
        if clg:
            name = input("Enter Student Name: ")
            roll = input("Enter Student Roll number: ")
            email = input("Enter Student Email: ")
            branch = input("Enter Student Branch: ")
            clg.add_student(student(roll, name, email, branch))
            print("*************************")
            print("Student added Successfully!")
            print("*************************")
        else:
            print("************************")
            print("College Does not Exist!")
            print("************************")
    elif ip == 3:
        cid = input("Enter College id: ")
        clg = next((c for c in colleges if c.cid == cid), None)
        if clg:
            name = input("Enter Teacher Name: ")
            roll = input("Enter Teacher Roll number: ")
            email = input("Enter Teacher Email: ")
            subject = input("Enter Teacher Subject: ")
            clg.add_teacher(teacher(roll, name, email, subject))
            print("*************************")
            print("Teacher added Successfully!")
            print("*************************")
        else:
            print("************************")
            print("College Does not Exist!")
            print("************************")
    elif ip == 4:
        cid = input("Enter College id: ")
        clg = next((c for c in colleges if c.cid == cid), None)
        if clg:
            print("**********************************")
            print(f"Student Details of {clg.cname}: ")
            for s in clg.students:
                print(f"Roll No: {s.rollno}, Name: {s.name}, Email: {s.email}, Branch: {s.branch}")
            print("**********************************")
        else:
            print("************************")
            print("College Does not Exist!")
            print("************************")
    elif ip == 5:
        cid = input("Enter College id: ")
        clg = next((c for c in colleges if c.cid == cid), None)
        if clg:
            subject = input("Enter Subject to Filter: ")
            filtered_teachers = [t for t in clg.teachers if t.subject.lower() == subject.lower()]
            if filtered_teachers:
                print(f"\nTeachers Teaching {subject} in {clg.cname}:")
                for t in filtered_teachers:
                    print(f"Roll No: {t.rollno}, Name: {t.name}, Email: {t.email}, Subject: {t.subject}")
            else:
                print("No Teachers Found for the Given Subject.")
        else:
            print("************************")
            print("College Does not Exist!")
            print("************************")
    elif ip == 6:
        cid = input("Enter College id: ")
        clg = next((c for c in colleges if c.cid == cid), None)
        if clg:
            branch = input("Enter Branch to Filter: ")
            filtered_students = [s for s in clg.students if s.branch.lower() == branch.lower()]
            if filtered_students:
                print(f"\nStudents in Branch {branch} in {clg.cname}:")
                for s in filtered_students:
                    print(f"Roll No: {s.rollno}, Name: {s.name}, Email: {s.email}, Branch: {s.branch}")
            else:
                print("No Students Found for the Given Branch.")
        else:
            print("************************")
            print("College Does not Exist!")
            print("************************")
    elif ip == 7:
        print("************************")
        print("Thanks! Visit Again")
        print("************************")
        break
    else:
        print("Invalid Option! Please Try Again.")
