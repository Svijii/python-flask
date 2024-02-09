

path= "mydata.txt"
file=open(path,"r")
lines =file.readlines()
line_count=len(lines)
print("The file has", line_count, "lines.")
file.close()
