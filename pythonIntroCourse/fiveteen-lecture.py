inputStr = input("What is yout name?")
fileOpen = open("test.txt", "w")
fileOpen.write("The user name is: " + str(inputStr))
fileOpen.close()