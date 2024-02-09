#reading a file
file = open("newdemo.txt","r")
mycontent = file.read()
print(mycontent)
file.close()
#writing a file
file = open("newdemo.txt","w")
print(file.write("good morning"))
file.close()

