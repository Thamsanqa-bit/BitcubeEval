import pyshorteners

f = open("user.txt", "w")
f.write("student,student1")

user = input("welcome would you like to register (yes/no): ")

while True:
    user = input("enter students name ")
    if user =="Thami":
        print("correct\n")
        break
    else:
        print("incorrect please enter name\n")

while True:
    user = input("enter surname ")
    if user =="Mbodla":
        print("correct\n")
        break
    else:
        print("incorrect please enter surname\n")

while True:
    user = input("enter email ")
    if user =="thamimbodla@gmail.com":
        print("correct\n")
        break
    else:
        print("incorrect please email\n")

while True:
    user = input("enter ID ")
    if user=="941207":
        print("correct\n")
        break
    else:
        print("incorrect enter DOB\n")

print("find a link below")

s=pyshorteners.Shortener()

print(s.tinyurl.short("https://gajeshnaik.tech"))

f = open("user.txt", "w")

print("IT lecturer fill in form\n ")

while True:
    user = input("lecturer name ")
    if user == "Ishmeal":
        print("correct\n")
        break
    else:
        print("incorrect name\n")

while True:
    user = input("please enter surname ")
    if user == "Nhlapo":
        print("correct\n")
        break
    else:
        print("incorrect surname\n")

while True:
    user = input("please email adrress")
    if user == "ishmealnhlapo@yahoo":
        print("correct\n")
        break
    else:
        print("incorrect address\n")

while True:
    user = input("please enter ID\n")
    if user == "760214":
        print("correct\n")
        break
    else:
        print("incorrect ID\n")

courses_years = ["Ishmeal Nhlapo","Information :9 months","Quatity survey :10 months","Journalism :10 months"]
for details in courses_years:
    print(details)



