#task1
list=[]
sum=0
n=int(input("Enter the number:"))
while n>0:
    sum+=n
    n=int(input("Enter the number:"))
print(sum)

#task5
list1=[9,-4,6,2]
i=0
p1=[]
p2=[]
for i in list1:
    if i>0:
        p1.append(i)
    else:
        p2.append(i)
print(p1)
print(p2)
   
