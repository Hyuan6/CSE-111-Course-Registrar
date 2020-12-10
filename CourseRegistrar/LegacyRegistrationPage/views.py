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
    response = render(request, 'LegacyRegistrationPage/LegacyRegistrationPage.html')

    if request.method == 'POST':
        form = request.POST.dict()
        database = f"db.sqlite3"

        sql = """insert into RegistrationPage_roll(course, student, grade)
               values """
        student_id = form.get('student_id')

        null_count = 0

        for index, crn in form.items():
            if crn == '':
                null_count += 1
                continue

            if "CRN_" in index:
                sql += f"({crn}, {student_id}, 'null'),"

        #remove hanging ','
        sql = sql[:-1]

        if null_count < 10:
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

    return response

    