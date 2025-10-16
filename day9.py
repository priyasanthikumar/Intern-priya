#task1
n1=int(input("Enter the no1:"))
n2=int(input("Enter the no2:"))
symbol=input("Enter the symbol:")
if symbol=="+":
    print(n1+n2)
elif symbol=="-":
    print(n1-n2)
elif symbol=="*":
    print(n1*n2)
elif symbol=="%":
    print(n1%n2)
elif symbol=="/":
    print(n1/n2)
elif symbol=="**":
    print(n1**n2)
elif symbol=="//":
    print(n1//n2)
else:
    print("none")

#task2
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multy(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
n1=int(input("Enter the no1:"))
n2=int(input("Enter the no2:"))
symbol=input("Enter the symbol:")
if symbol=="+":
    print(n1+n2)
elif symbol=="-":
    print(n1-n2)
elif symbol=="*":
    print(n1*n2)
elif symbol=="/":
    print(n1/n2)
else:
    print("none")
