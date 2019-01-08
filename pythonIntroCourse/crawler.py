import requests
import re


url="https://www.mmo-champion.com/members/"

def getSourceCode(id):
    r = requests.get(url + str(id) + ".html")
    return r.text

def getUsers():
    users = []
    for i in range(561665, 561670):
        sourceCode = getSourceCode(i)
        for match in re.findall('<title>View Profile: (\w+) - MMO-Champion</title>', sourceCode):
            if match not in users:
                users.append(match)

    print(users)



getUsers()


