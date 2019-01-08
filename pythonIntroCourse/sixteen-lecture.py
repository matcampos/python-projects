fileOpen = open("test.txt", "r+")
str = fileOpen.read()
print(str)
fileOpen.close()