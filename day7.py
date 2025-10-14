#task1
name="priya"
password="ggg"
email="priya@gmail.com"
name1=input("Username:")
password1=input("Password:")
email1=input("Emailid:")
if name==name1 and password==password1 and email==email1:
    print("login success")
else:
    print("failed")
#task2
n=int(input("Enter the number:"))
if n<=9:
    print("one digit")
elif n<=99:
    print("two digit")
elif n<=999:
    print("three digit")
elif n<=9999:
    print("four digit")
elif n<=99999:
    print("five digit")
else:
    print("Invalid")
   
#task3
Tamil=int(input("Enter the tamil marks:"))
English=int(input("Enter the english marks:"))
Maths=int(input("Enter the maths marks:"))
Science=int(input("Enter the science marks:"))
Social=int(input("Enter the social marks:"))
Total=Tamil+English+Maths+Science+Social
percentage=Total/5
print(Total)
print(percentage)
if percentage<=25:
    print("grade of F")
elif percentage==25 or percentage<=50:
    print("grade of E")
elif percentage==45 or percentage<50:
    print("grade of D")
elif percentage==50 or percentage<60:
    print("grade of C")
elif percentage==60 or percentage<=80:
    print("grade of B")
elif percentage<=80:
    print("grade of A")


#task4
cls=int(input("No of classes Held:"))
attend=int(input("No of classes attend:"))
print(cls)
print(attend)
percentage=attend/cls*100
print(percentage)
if percentage<=75:
    print("not allow the exam")
else:
    print("allow the exam")
