emptyList = []

count = 0

while (count < 20):
    count += 1
    if count % 2 == False:
        print("Its a even number")
        emptyList.append(count)
    else:
        print("This is not a Even number")

print(emptyList)
