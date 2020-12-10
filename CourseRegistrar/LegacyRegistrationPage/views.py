from django.shortcuts import render
from django.http import HttpResponse, Http404

import sqlite3

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
    if request.method == 'POST':
        form = request.POST.dict()
        database = f"db.sqlite3"

        sql = """insert into RegistrationPage_roll(course, student)
               values """
        student_id = form.get('student_id')

        for index, crn in form.items():
            if "CRN_" in index and crn != '':
                sql += f"({crn}, {student_id}),"

        #remove hanging ','
        sql = sql[:-1]

        print(sql)

        conn = openConnection(database)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

        for index, crn in form.items():
            if "CRN_" in index and crn != '':
                sql = f"""update RegistrationPage_course
                          set Seats_avil = Seats_avil - 1,
                              Act_enrl = Act_enrl + 1
                          where crn = {crn};"""
                cur.execute(sql)
                conn.commit()

        closeConnection(conn, database)

    return render(request, 'LegacyRegistrationPage/LegacyRegistrationPage.html')

    