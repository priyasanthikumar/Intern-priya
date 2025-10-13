#tuple
t=(4,5,6,3,4)
print(len(t))
print(type(t))

print(t.index(3))

#dictionary
person={"name":"Ragavi","age":21}

print(person.get("age"))
print(person["name"])
print(person.pop(name))
person.clear()

#list
num_list=[3,6,7,1]
num_list1=[2,4]
test="Hello"

print(num_list.count(3))

num_list.reverse()
print(num_list)

num_list.sort()
print(num_list1)

num_list.extend(test)
print(num_list)

num_list.remove('H')
print(test)

#set
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
print(len(thisset))   

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
