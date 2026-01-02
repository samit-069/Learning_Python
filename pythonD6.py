#Day 6
#File Handlling

#opening file
#file = open("data.txt", "r")

#writing to file:
#file = open("data.txt","w")
#file.write("hello world")

#other modes:
    #"a" : append
    #"r+" : read + write

#mini exercise

with open("test.txt","w") as file:
    content = file.write(input("Enter name: "))
with open("test.txt","r") as file:
    content = file.read()
    print(content)