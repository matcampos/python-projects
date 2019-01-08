numbers = [5, 4, 1, 3, 2]

sortedNumbers = sorted(numbers)

reverseSortedNumbers = sorted(numbers, reverse=True)

print(sortedNumbers, reverseSortedNumbers)


arr = [
    {
        "teste": "teste",
        "teste2": "teste2",
        "teste3":"teste3"
    },
    {
        "1": 1,
        "2": 2,
        "3": 3,

    },
    {
        "aaaaa": "bbbbbb",
        "bbbbbb":"cccccc",
        "dddddd":"eeeeeee"
    },
    {'python', 'none'}
]


from pprint import pprint

pprint(arr, depth=4)

print(list(enumerate(arr)))

listEnumerated = list(enumerate(arr))

print(listEnumerated)
