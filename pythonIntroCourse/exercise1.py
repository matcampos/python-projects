tpl1 = ("windows","mac","linux")

list1 = ["bill gates", "steeve jobs", "linux"]

dictionary1 = {tpl1[0]: list1[0], tpl1[1]: list1[1], tpl1[2]: list1[2]}


dict2 = dict(zip(list1, tpl1))
print(dictionary1)

print(dict2)