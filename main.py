from canvasapi import Canvas
import requests
from datetime import datetime
import os.path
from os import path
import getpass

def userInput():
    print("PLEASE MAKE SURE YOUR USERNAME HAS NO SPACES. This is your current username: " + getpass.getuser())
    print("What is your canvas token?")
    tokenInput = input()
    return tokenInput


if not path.exists("/Users/"+getpass.getuser()+"/Desktop/Assignments.txt"):
    token = userInput()
    filePath = "/Users/"+getpass.getuser()+"/Desktop/Assignments.txt"
    file = open(filePath, 'w+')
    canvas = Canvas(base_url="https://canvas.iastate.edu/", access_token=token)
    userString = str(canvas.get_current_user())[-7:]
    userStringReplaced = userString.replace('(', '')
    userStringReplaced2 = userStringReplaced.replace(')', '')
    user = canvas.get_user(int(userStringReplaced2))
    courses = user.get_courses(enrollment_state='active')
    currentNumber = 0
    semester_courses = []
    for course in courses:
        if str(course)[:5] == "S2021":
            semester_courses.append(course)
    now = datetime.now()

    file.write("Access token: "+token)
    file.write("\n")
    file.write("\n")
    file.write("Date today: " + now.strftime("%m/%d/%Y"))
    file.write("\n")
    file.write("\n")
    for c in semester_courses:
        s = str(c)[-7:]
        s = s.replace('(', '')
        s = s.replace(')', '')
        url = "https://canvas.iastate.edu/api/v1/courses/" + s + "/assignments"
        classString = str(c)
        file.write("-----------------------------------------------------------------")
        file.write("\n")
        file.write(classString[:-8])
        file.write("\n")
        headers = {'Authorization': 'Bearer ' + token}
        r = requests.get(url, headers=headers)
        listHW = r.json()
        if len(listHW) > 0:
            for x in listHW:
                if x['due_at'] is None:
                    file.write("              - " + x['name'] + ": Due Date - None")
                    file.write("\n")
                else:
                    month = int(x['due_at'][5:7])
                    day = int(x['due_at'][8:10])
                    year = x['due_at'][0:4]
                    if not now.month > month or now.month < month and now.day > day or now.month == month and now.day > day:
                        file.write(
                            "              - " + x['name'] + ": Due Date - " + x['due_at'][5:7] + "/" + x['due_at'][
                                                                                                        8:10] + "/" + year)
                        file.write("\n")
        else:
            file.write("                NO ASSIGNMENTS")
            file.write("\n")

    file.close()

else:

    filePath = "/Users/"+getpass.getuser()+"/Desktop/Assignments.txt"
    fileRead = open(filePath, 'r')
    tokenRead = fileRead.readline()[14:-1]
    fileRead.close()
    file = open(filePath, 'w')
    canvas = Canvas(base_url="https://canvas.iastate.edu/", access_token=tokenRead)
    userString = str(canvas.get_current_user())[-7:]
    userStringReplaced = userString.replace('(', '')
    userStringReplaced2 = userStringReplaced.replace(')', '')
    user = canvas.get_user(int(userStringReplaced2))
    courses = user.get_courses(enrollment_state='active')
    currentNumber = 0
    semester_courses = []
    for course in courses:
        if str(course)[:5] == "S2021":
            semester_courses.append(course)
    now = datetime.now()
    file.write("Access token: " + tokenRead)
    file.write("\n")
    file.write("\n")
    file.write("Date today: " + now.strftime("%m/%d/%Y"))
    file.write("\n")
    file.write("\n")
    for c in semester_courses:
        s = str(c)[-7:]
        s = s.replace('(', '')
        s = s.replace(')', '')
        url = "https://canvas.iastate.edu/api/v1/courses/" + s + "/assignments"
        classString = str(c)
        file.write("-----------------------------------------------------------------")
        file.write("\n")
        file.write(classString[:-8])
        file.write("\n")
        headers = {'Authorization': 'Bearer ' + tokenRead}
        r = requests.get(url, headers=headers)
        listHW = r.json()
        if len(listHW) > 0:
            for x in listHW:
                if x['due_at'] is None:
                    file.write("              - " + x['name'] + ": Due Date - None")
                    file.write("\n")
                else:
                    month = int(x['due_at'][5:7])
                    day = int(x['due_at'][8:10])
                    year = x['due_at'][0:4]
                    if not now.month > month or now.month < month and now.day > day or now.month == month and now.day > day:
                        file.write(
                            "              - " + x['name'] + ": Due Date - " + x['due_at'][5:7] + "/" + x['due_at'][
                                                                                                        8:10] + "/" + year)
                        file.write("\n")
        else:
            file.write("                NO ASSIGNMENTS")
            file.write("\n")

    file.close()
