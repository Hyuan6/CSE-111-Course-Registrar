from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sqlite3
import json

import sqlite3
from random import randint

from RegistrationPage.utils.LegRegAPI import LegacyRegistrationAPI

def openConnection(_dbFile):
    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    return conn

def closeConnection(_conn, _dbFile):
    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

def index(request):
    response = render(request, 'RegistrationPage/homePage.html')

    if request.method == 'POST':
        form = request.POST.dict()
        database = f"db.sqlite3"

        if 'crn-submit' in request.POST:
            conn = openConnection(database)
            cur = conn.cursor()

            username = form.get('username')
            password = form.get('password')

            if 'sign-up' in request.POST:
                YEAR_IN_SCHOOL_CHOICES = ['FR', 'SO', 'JR', 'SR', 'GR']
                student_id = randint(100000000,999999999)
                class_standing = YEAR_IN_SCHOOL_CHOICES[randint(0,4)]
                phone_number = "XXX-XXX-XXXX"

                cur.execute(f"""insert into RegistrationPage_student( Student_ID, Password, Username, Class_Standing, Phone_Number, Academic_Probation_Hold)
                                values ({student_id}, '{password}', '{username}', '{class_standing}', '{phone_number}', 0);""")
                conn.commit()

                print(f"Successfully added {username} to Students")

            cur.execute(f"""SELECT EXISTS(SELECT 1 
                                      FROM RegistrationPage_student 
                                      WHERE Username='{username}' and Password='{password}' 
                                      LIMIT 1);""")
            success = cur.fetchone()[0]
            
            if success:
                student_id = cur.execute(f"""SELECT Student_ID
                              FROM RegistrationPage_student
                              WHERE Username = '{username}' and Password='{password}'
                              LIMIT 1""").fetchone()[0]

                response.set_cookie(key="student_id", value=student_id)

            conn.commit()

            print(f"{username} Logged In Successfully")
            closeConnection(conn, database)

    return response

def courseReg(request):
    return render(request, 'RegistrationPage/regPage.html')

#used to update autocomplete on search bar
def search_bar(request):
    # print("this method is running")
    if request.is_ajax and request.method == "GET":
        # print("hey this shit works")
        ans = autocomp_data()
        
        return JsonResponse(ans, safe = False, status = 200)
    return JsonResponse({"shits not working":True}, status = 200)
#query db for autocomplete info
def autocomp_data():
    database = f"db.sqlite3"
    conn = sqlite3.connect(database)
    with conn:
        try:
            sql = """select crn, cnum, title
                        from RegistrationPage_course
                        where Actv = ? """
            cur = conn.cursor()
            cur.execute(sql, ("LECT", ))
            rows = cur.fetchall()
            response = []
            for row in rows:
                response.append(row[1])
        except sqlite3.Error as e:
            print(e)
    conn.close()
    return response

def student_profile(request):
    database = f"db.sqlite3"
    conn = openConnection(database)
    cur = conn.cursor()

    if request.is_ajax and request.method == "GET":
        student_id = list(request.GET.items())[0][1]

        sql = f"""select Username, Class_Standing, Phone_Number, Academic_Probation_Hold from RegistrationPage_student where Student_ID = {student_id}"""

        val = cur.execute(sql).fetchall()[0]

        res = []
        for i in val:
            res.append(i)
            print(i)

        return JsonResponse(res, safe = False, status = 200)
    return JsonResponse({"oops":True}, status = 200)

def gradPlan(request):
    return render(request, 'RegistrationPage/development.html')


# handel register request
def reg_for(request):
    if request.is_ajax() and request.method == "GET":
        a = request.GET.values()
        course_nums = list(a)
        
        student_ID = None

        try:
            student_ID = course_nums[-1]
        except IndexError:
            return JsonResponse("Login", safe = False, status = 200)
        
        course_crns = []

        for num in course_nums[:-1]:
            temp = f_crn(num)
            course_crns.append(temp)

        print(course_crns)

        lgAPI = LegacyRegistrationAPI(course_crns, student_ID)
        lgAPI.start()

    else:
        print("do otherthing")

    return JsonResponse("Success", safe = False, status = 200)
# find crns for course passed through reg_for
def f_crn(course_number):
    database = f"db.sqlite3"
    conn = sqlite3.connect(database)
    with conn:
        try:
            sql = """select crn
                        from RegistrationPage_course
                        where cnum = ? """
            cur = conn.cursor()
            cur.execute(sql, (course_number, ))
            rows = cur.fetchall()
            return rows
        except sqlite3.Error as e:
            print(e)
    conn.close()
    return "crn not found!"