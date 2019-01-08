numbers_1_to_5 = []
numbers_1_to_5.append(1)
numbers_1_to_5.append(2)
for number in range(3, 5+1):
    numbers_1_to_5.append(number)

print(numbers_1_to_5)


iterable = 1, 2, 3, 4

multiplied_list = list(map(lambda num: 5*num, iterable))

print(multiplied_list)

multiplied_list = [ 5*num for num in iterable]

multiplied_generator = ( 5*num for num in iterable)
next(multiplied_generator)

multiplied_dict = { num: 5*num for num in iterable}

filtered_multiplied_list = list(map(lambda num: 5*num, filter(lambda num: num%2==0, iterable)))

print(filtered_multiplied_list)

filtered_multiplied_list = [ 5*num for num in iterable if num%2==0 ]