import bcrypt
import re
import datetime
import uuid 
import os
regex = r'^01[0125][0-9]{8}$'
def append_new_line(file_name, text_to_append):
    with open(file_name, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(text_to_append)

def check(pnum):
    if(re.fullmatch(regex, pnum)):
        return True
    else:
        return False

def delline(i):
    a_file = open("projects.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    del lines[i]
    new_file = open("projects.txt", "w+")
    for line in lines:
        new_file.write(line)

    new_file.close()
def createp():
    pnm = input("Enter project name: ")
    dtls = input("Enter project desc: ")
    trgt = input("Enter target: ")
    strtd = input("Enter start date %Y-%m-%d: ")
    try:
        datetime.datetime.strptime(strtd, '%Y-%m-%d')
    except:
        print("Not Valid Date")
        createp()
    endate = input("Enter end date %Y-%m-%d: ")
    try:
        datetime.datetime.strptime(endate, '%Y-%m-%d')
    except:
        print("Not Valid Date")
        createp()
    if strtd >= endate:
        print("Dates are invalid")
        createp()
    
    if not pnm.isspace() and not dtls.isspace() and trgt.isnumeric() and not strtd >= endate:
        xid = str(uuid.uuid1())
        plst = gainAccess.mymail+","+pnm +","+ dtls+"," + trgt+","+strtd+","+endate+","+xid
        append_new_line("projects.txt", plst)
    else:
        createp()
def viewall():
    f = open("projects.txt", "r")
    content_list = [line.rstrip('\n') for line in f]
    f.close()
    for i in range(len(content_list)):
        print("Project title: " +content_list[i].split(",")[1]+", Details: "+content_list[i].split(",")[2]+", Total target: "+content_list[i].split(",")[3]+", Start Date: "+content_list[i].split(",")[4]+", End date: "+content_list[i].split(",")[5], ", Owner: "+content_list[i].split(",")[0])


def editp():
    f = open("projects.txt", "rt")
    content_list = [line.rstrip('\n') for line in f]
    f.close()
    newx = 0
    user_lst = []
    for i in range(len(content_list)):
        if content_list[i].split(",")[0] == gainAccess.mymail:
            newx += 1
            user_lst.append(content_list[i])
            print(str(newx-1) + "-"+content_list[i].split(",")[1])
    userchs = input("Choose project to change: ")
    crruserp = []
    for vrb in range(newx):
        if int(userchs) == vrb:
            crruserp.append(str(user_lst[vrb].split(",")[6]))
            print(user_lst[vrb].split(",")[6])
    a_file = open("projects.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    print(f"0.delete project| 1. change project name: |2. change description:{os.linesep}3.change target |4. change start date: |5. change end date: ")
    userchlist = input("Choose field to change: ")
    if userchlist == "1":
        chng = input("Enter new name: ")
        for line in range(len(crruserp)):
            for line2 in range(len(content_list)):
                if crruserp[line] == content_list[line2].split(",")[6]:
                    newline2 = gainAccess.mymail+","+ chng + ","+content_list[line2].split(",")[2]+","+content_list[line2].split(",")[3]+","+content_list[line2].split(",")[4]+","+content_list[line2].split(",")[5]+","+content_list[line2].split(",")[6]+"\n"
                    file_object = open('projects.txt', 'a')
                    file_object.write(newline2)
                    file_object.close()
                    delline(int(line2))
    if userchlist == "2":
        chng = input("Enter new description: ")
        for line in range(len(crruserp)):
            for line2 in range(len(content_list)):
                if crruserp[line] == content_list[line2].split(",")[6]:
                    newline2 = gainAccess.mymail+","+content_list[line2].split(",")[1]+","+ chng + ","+content_list[line2].split(",")[3]+","+content_list[line2].split(",")[4]+","+content_list[line2].split(",")[5]+","+content_list[line2].split(",")[6]+"\n"
                    file_object = open('projects.txt', 'a')
                    file_object.write(newline2)
                    file_object.close()
                    delline(int(line2))
    if userchlist == "3":
        chng = input("Enter new target: ")
        for line in range(len(crruserp)):
            for line2 in range(len(content_list)):
                if crruserp[line] == content_list[line2].split(",")[6]:
                    newline2 = gainAccess.mymail+","+content_list[line2].split(",")[1]+ ","+content_list[line2].split(",")[2]+","+ chng +","+content_list[line2].split(",")[4]+","+content_list[line2].split(",")[5]+","+content_list[line2].split(",")[6]+"\n"
                    file_object = open('projects.txt', 'a')
                    file_object.write(newline2)
                    file_object.close()
                    delline(int(line2))
    if userchlist == "4":
        chng = input("Enter new start date: ")
        for line in range(len(crruserp)):
            for line2 in range(len(content_list)):
                if crruserp[line] == content_list[line2].split(",")[6]:
                    newline2 = gainAccess.mymail+","+content_list[line2].split(",")[1]+ ","+content_list[line2].split(",")[2]+","+content_list[line2].split(",")[3]+","+ chng +","+content_list[line2].split(",")[5]+","+content_list[line2].split(",")[6]+"\n"
                    file_object = open('projects.txt', 'a')
                    file_object.write(newline2)
                    file_object.close()
                    delline(int(line2))
    if userchlist == "5":
        chng = input("Enter new end date: ")
        for line in range(len(crruserp)):
            for line2 in range(len(content_list)):
                if crruserp[line] == content_list[line2].split(",")[6]:
                    newline2 = gainAccess.mymail+","+content_list[line2].split(",")[1]+ ","+content_list[line2].split(",")[2]+","+content_list[line2].split(",")[3]+","+content_list[line2].split(",")[4]+","+ chng +","+content_list[line2].split(",")[6]+"\n"
                    file_object = open('projects.txt', 'a')
                    file_object.write(newline2)
                    file_object.close()
                    delline(int(line2))
    if userchlist == "0":
        for line in range(len(crruserp)):
            for line2 in range(len(content_list)):
                if crruserp[line] == content_list[line2].split(",")[6]:
                    delline(int(line2))
def srchdate():
    f = open("projects.txt", "rt")
    content_list = [line.rstrip('\n') for line in f]
    f.close()
    srcd = input("Enter search date: ")
    user_lstsr = []
    for i in range(len(content_list)):
        if content_list[i].split(",")[4] == srcd or content_list[i].split(",")[5] == srcd:
            user_lstsr.append(content_list[i])
            print("Project title: " +content_list[i].split(",")[1]+", Details: "+content_list[i].split(",")[2]+", Total target: "+content_list[i].split(",")[3]+", Start Date: "+content_list[i].split(",")[4]+", End date: "+content_list[i].split(",")[5], ", Owner: "+content_list[i].split(",")[0])
    #f = open("projects.txt", "r")
    #content_list = [line.rstrip('\n') for line in f]
    #f.close()
    #for i in range(len(content_list)):
        #print("Project title: " +content_list[i].split(",")[1]+", Details: "+content_list[i].split(",")[2]+", Total target: "+content_list[i].split(",")[3]+", Start Date: "+content_list[i].split(",")[4]+", End date: "+content_list[i].split(",")[5], ", Owner: "+content_list[i].split(",")[0])

def pscreen(optione=None):
        print("Welcome, please select an option")
        optione = input("1.Create project |2.View all  |3.Edit: |4.Search by date:")
        if optione == "1":
            createp()
        elif optione == "2":
            viewall()
        elif optione == "3":
            editp() 
        elif optione == "4":
            srchdate() 
        else:
            print("Please enter a valid parameter, this is case-sensitive")

def gainAccess(Email=None, Password=None):
    Email = input("Enter your Email:")
    gainAccess.mymail = Email
    Password = input("Enter your Password:")
    if not len(Email or Password) < 1:
        if True:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a = i.split(",")[0]
                b = i.split(",")[1]
                b = b.strip()
                c = a,b
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            try:
                if Email in data:
                    hashed = data[Email].strip('b')
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')
                    
                    try:
                        if bcrypt.checkpw(Password.encode(), hashed):
                        
                            print("Login success!")
                            print("Hi", Email)
                            pscreen()
                        else:
                            print("Wrong password")
                        
                    except:
                        print("Incorrect passwords or Email")
                else:
                    print("Email doesn't exist")
            except:
                print("Password or Email doesn't exist")
        else:
            print("Error logging into the system")
            
    else:
        print("Please attempt login again")
        gainAccess()	
def register(Email=None, Password1=None, Password2=None):
    Email = input("Enter an Email:")
    fname = input("Enter First name:")
    lname = input("Enter Last name:")
    pnumb = input("Enter phone number:")
    Password1 = input("Create password:")
    Password2 = input("Confirm Password:")
    db = open("database.txt", "r")
    d = []
    for i in db:
        a = i.split(",")[0]
        b = i.split(",")[1]
        b = b.strip()
        c = a,b
        d.append(a)
    if not check(pnumb):
        print("not valid number")
        register()
    if not len(Password1)<=5:
        db = open("database.txt", "r")
        if not Email ==None:
            if len(Email) <1:
                print("Please provide a Email")
                register()
            elif Email in d:
                print("Email exists")
                register()		
            else:
                if Password1 == Password2:
                    Password1 = Password1.encode('utf-8')
                    Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())
                    db = open("database.txt", "a")
                    db.write(Email+", "+str(Password1)+","+fname+","+lname+","+pnumb+ "\n")
                    print("User created successfully!")
                    print("Please login to proceed:")
					
                else:
                    print("Passwords do not match")
                    register()
    else:
        print("Password too short")



def home(option=None):
	print("Welcome, please select an option")
	option = input("1. Login | 2. Signup:")
	if option == "1":
		gainAccess()
	elif option == "2":
		register()
	else:
		print("Please enter a valid parameter, this is case-sensitive")



home()