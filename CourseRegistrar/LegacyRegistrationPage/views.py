from django.shortcuts import render
from django.http import HttpResponse, Http404

import sqlite3

YEAR_IN_SCHOOL_CHOICES = {'FR': 'Freshman',
                          'SO': 'Sophmore',
                          'JR': 'Junior',
                          'SR': 'Senior',
                          'GR': 'Graduate'}

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
    response['Sucess'] = False

    if request.method == 'POST':
        form = request.POST.dict()
        database = f"db.sqlite3"
        conn = openConnection(database)
        cur = conn.cursor()

        sql = """insert into RegistrationPage_roll(course, student, grade)
               values """
        student_id = form.get('student_id')

        #check if student on hold or academic probation
        holdSQL = f"""select exists (select 1 
                                     from RegistrationPage_student 
                                     where Student_ID = '{student_id}' and Academic_Probation_Hold = 1)"""
        holds = cur.execute(holdSQL).fetchone()
        if holds == 1:
            return response

        classStandingSQL = f"""select Class_Standing
                               from RegistrationPage_student
                               where Student_ID = '{student_id}'"""

        classStanding = cur.execute(classStandingSQL).fetchone()
        classStanding = YEAR_IN_SCHOOL_CHOICES[classStanding[0]]

        null_count = 0

        for index, crn in form.items():
            if crn == '':
                null_count += 1
                continue

            if "CRN_" in index:
                #check if student meets crn requirements
                checkCSSQL = f"""select exists (select 1
                                 from RegistrationPage_requirments
                                 where course_id = '{crn}' and (cs1 = '{classStanding}' 
                                                             or cs2 = '{classStanding}' 
                                                             or cs3 = '{classStanding}' 
                                                             or cs4 = '{classStanding}'))"""

                validCS = cur.execute(checkCSSQL).fetchone()[0]
                # print(validCS)
                if validCS != 1:
                    print("Registration Failed: invalid class standing")
                    return response

                checkPRSQL = f"""with baseTable as(
                                    select substr(cnum, 1,INSTR(cnum, '-') + 3)
                                    from RegistrationPage_roll left join RegistrationPage_course on course = crn
                                    where student = '{student_id}'
                                 )
                
                                 select exists (select 1
                                 from RegistrationPage_requirments
                                 where course_id = {crn} and ((pr1 in baseTable or pr1 = 'null')
                                                            and (pr2 in baseTable or pr2 = 'null')
                                                            and (pr3 in baseTable or pr3 = 'null')
                                                            and (pr4 in baseTable or pr4 = 'null')
                                                            and (pr5 in baseTable or pr5 = 'null')))"""

                havePR = cur.execute(checkPRSQL).fetchone()[0]
                if havePR != 1:
                    print("Registration Failed: incomplete prerequisites")
                    return response

                sql += f"({crn}, {student_id}, 'null'),"

        #remove hanging ','
        sql = sql[:-1]

        if null_count < 10:
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

            response['Sucess'] = True

        closeConnection(conn, database)

    return response

    