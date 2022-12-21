f = open("mydata.txt")
contents = f.read()
f.close()
print(contents)

f = open("createdfile.txt", "w")
f.write("This is some data that our Python script created.\n")
f.close()