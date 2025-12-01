#Day 4
#List Methods
list = ["apple", "banana", "orange"]
print(list)

#ADD ITEM
list.append("mango") #adds mango to end of list
print(list)
list.insert(1, "grape") #adds grape to index 1(2nd)
print(list)
list.extend(["grape", "watermelon", "papaya"])#adds multiple items
print(list)

#REMOVE ITEM
list.pop() #removes last item
print(list)
list.pop(6)#remove specific index(7th item in this case)
print(list)
list.remove("grape")#remove first occurance of item
print(list)
list.clear()#empties the list
print(list)

#SEARCHING
list = ["apple", "banana", "orange"]
print(list.index("banana"))#gives index value
print("pineapple" in list)#check existance (True/False)

#SORTING
list.sort()#sorts list in asending order
print(list)
list.reverse() #flips list, NOT IN DESENDING ORDER
print(list)
list.sort(reverse=True)#sorts list in desending order
print(list)

#String Methods
name = "SaMiT MaHaRjAn"
print(name)
name=name.title()
print(name)
name=name.lower()
print(name)
name=name.upper()
print(name)
name1=name.split()
print(name1)
name=name.replace("A","@")
print(name)

#checking string method
print(name.startswith("S"))
print(name.endswith("S"))
print("@" in name)

name ="    Samit Maharjan     "
name=name.strip()
print(name)
