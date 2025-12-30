#Day 1 project
list = [] #declearing empty list to add in later
count = int(input("Enter the number of item to be listed:")) #taking input from user to get number of item in list

for i in range(count): #loop runs for as many times as the number given by user
    item = input(f"Enter item number {i+1}:")
    list.append(item)#adding item in list
print(list)#printing items
