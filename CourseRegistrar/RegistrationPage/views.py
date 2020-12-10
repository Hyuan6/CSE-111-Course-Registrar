from django.shortcuts import render
from django.http import HttpResponse

import sqlite3
from random import randint

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

            # print(f"{username} Logged In Successfully")
            closeConnection(conn, database)

        elif 'sign-up' in request.POST:
            conn = openConnection(database)
            cur = conn.cursor()

            YEAR_IN_SCHOOL_CHOICES = ['FR', 'SO', 'JR', 'SR', 'GR']

            student_id = randint(100000000,999999999)
            username = form.get('username')
            password = form.get('password')
            class_standing = YEAR_IN_SCHOOL_CHOICES[randint(0,4)]
            phone_number = "XXX-XXX-XXXX"

            cur.execute(f"""insert into RegistrationPage_student( Student_ID, Password, Username, Class_Standing, Phone_Number)
                            values ({student_id}, '{password}', '{username}', '{class_standing}', '{phone_number}');""")

            print(f"Successfully added {username} to Students")

            conn.commit()
            closeConnection(conn, database)

    return 

def courseReg(request):
    return render(request, 'RegistrationPage/regPage.html')

def gradPlan(request):
    return render(request, 'RegistrationPage/development.html')

