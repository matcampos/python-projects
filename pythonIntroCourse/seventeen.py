# Creating functions in python

def getEvenNumbers(count):
    list = []
    for num in range(0, count):
        if (num % 2 == 0):
            list.append(num)
    return list

def howLongIsList(number):
    if(len(getEvenNumbers(number)) >= 5):
        print("It's longer than 5")
    elif (len(getEvenNumbers(number)) <= 5):
        print("It's smaller than 5")

howLongIsList(10)