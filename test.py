import json
import requests
from datetime import datetime
from canvasapi import Canvas
url = "https://canvas.iastate.edu/api/v1/courses/77688/assignments"
quizurl = "https://canvas.iastate.edu/api/v1/courses/77688/quizzes"
headers = {'Authorization' : 'Bearer 10835~LB67sbklk4Jj441ifALNVi2C5JUvTzUGqdCHy5Ix5iqdG5hMO6nJ58yNWzbTnuYe'}
r = requests.get(url, headers = headers)
quizr = requests.get(quizurl, headers = headers)
listHW = r.json()
listquiz = quizr.json()
now = datetime.now()

if len(listHW) > 0:
    print("       HW")
    for x in listHW:
        if x['due_at'] is None:
            print("              - " + x['name'] + ": Due Date - None")
        else:
            month = int(x['due_at'][5:7])
            day = int(x['due_at'][8:10])
            year = x['due_at'][0:4]
            if now.month <= month:
                if now.day <= day:
                    print("              - " + x['name'] + ": Due Date - " + x['due_at'][5:7] + "/" + x['due_at'][8:10] + "/" + year)


if len(listquiz) > 0:
    print("       Quiz")
    for y in listquiz:
        if y['due_at'] is None:
            print("              - " + y['name'] + ": Due Date - None")
        else:
            quizMonth = int(y['due_at'][5:7])
            quizDay = int(y['due_at'][8:10])
            quizYear = y['due_at'][0:4]
            if now.month <= quizMonth:
                if now.day <= quizDay:
                    print("              - " + y['title'] + ": Due Date - " + y['due_at'][5:7] + "/" + y['due_at'][8:10] + "/" + quizYear)
