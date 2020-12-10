from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sqlite3
import json

def index(request):
    return render(request, 'RegistrationPage/homePage.html')

def courseReg(request):
    return render(request, 'RegistrationPage/regPage.html')

#used to update autocomplete on search bar
def search_bar(request):
    print("this method is running")
    if request.is_ajax and request.method == "GET":
        print("hey this shit works")
        ans = autocomp_data()

        y = json.dumps(ans)
        
        return JsonResponse(ans, safe = False, status = 200)
    return JsonResponse({"shits not working":True}, status = 200)
#query db for autocomplete info
def autocomp_data():
    database = r"C:/Users/IDC/Documents/Code/DataBases/Project/CSE-111-Course-Registrar/CourseRegistrar/db.sqlite3"
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

def gradPlan(request):
    return render(request, 'RegistrationPage/development.html')


# handel register request
def reg_for(request):
    if request.is_ajax() and request.method == "GET":
        a = request.GET.values()
        course_nums = list(a)
        print(course_nums)
        course_crns = []
        for num in course_nums:
            temp = f_crn(num)
            course_crns.append(temp)
        print(course_crns)


        # API TAKES OVER HERE



        print("do thing")
    else:
        print("do otherthing")

    return JsonResponse(1, safe = False, status = 200)
# find crns for course passed through reg_for
def f_crn(course_number):
    database = r"C:/Users/IDC/Documents/Code/DataBases/Project/CSE-111-Course-Registrar/CourseRegistrar/db.sqlite3"
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