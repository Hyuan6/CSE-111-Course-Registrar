import sqlite3
from sqlite3 import Error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

ops = Options()
ops.page_load_strategy = 'normal'

driver = webdriver.Chrome(executable_path='C:/Users/IDC/Documents/Code/DataBases/Project/CSE-111-Course-Registrar/chromedriver.exe', options= ops)
def open_conn(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
        print("db open")
    except Error as e:
        print(e)

    return conn

def close(conn):
    try:
        conn.close()
        print("db closed")
    except Error as e:
        print(e)

def insert_sub(conn, val):
    try:
        sql = """INSERT INTO RegistrationPage_subject(title)
                 values(?)"""
        conn.execute(sql,(val, ))
        conn.commit()
        print(f"adding: {val}")
    except Error as e:
        conn.rollback()
        print(e)

def insert_table(conn, x, cache):
    try:
        sql = """INSERT INTO RegistrationPage_course(crn, Instructor, Title, cnum, Actv, Units, Days, TimeOfLec, Bldg_Rm, Start, End, Max_enrl, Act_enrl, Seats_avil, sub_id)
                 values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """
        y =[]
        if(len(x) == 9):
            t = x[5]
            temp = t.split(' ', 6)
            crn = x[0]
            cnum = x[1]
            Title = x[2]
            Units = x[3]
            Actv = x[4]
            Days = temp[0]
            TimeOfLec = temp[1]
            Bldg_Rm = "REMOTE ONLY"
            Start = temp[4]
            End = temp[5]
            Instructor = temp[6]
            Max_enrl = x[6]
            Act_enrl = x[7]
            Seats_avil = x[8]
            sub_id = cnum.split("-")[0]
            y = [crn, Instructor, Title, cnum, Actv, Units, Days, TimeOfLec, Bldg_Rm, Start, End, Max_enrl, Act_enrl, Seats_avil, sub_id]
            conn.execute(sql,(crn, Instructor, Title, cnum, Actv, Units, Days, TimeOfLec, Bldg_Rm, Start, End, Max_enrl, Act_enrl, Seats_avil, sub_id))
            conn.commit()
            print(f"adding: {x[0]}")
        
        elif len(x) > 9:
            t = x[len(x)-4]
            temp = t.split(' ', 6)
            crn = x[0]
            cnum = x[1]
            Title = x[2]
            Units = x[len(x)-6]
            Actv = x[len(x)-5]
            Days = temp[0]
            TimeOfLec = temp[1]
            Bldg_Rm = "REMOTE ONLY"
            Start = temp[4]
            End = temp[5]
            Instructor = temp[6]
            Max_enrl = x[len(x)-3]
            Act_enrl = x[len(x)-2]
            Seats_avil = x[len(x)-1]
            sub_id = cnum.split("-")[0]
            y = [crn, Instructor, Title, cnum, Actv, Units, Days, TimeOfLec, Bldg_Rm, Start, End, Max_enrl, Act_enrl, Seats_avil, sub_id]
            conn.execute(sql,(crn, Instructor, Title, cnum, Actv, Units, Days, TimeOfLec, Bldg_Rm, Start, End, Max_enrl, Act_enrl, Seats_avil, sub_id))
            conn.commit()
            print(f"adding: {x[0]}")
            
        elif x[0] == "      EXAM":
            t = x[1]
            temp = t.split(' ')
            crn = cache[0]
            cnum = cache[3]
            Title = cache[2]
            Units = cache[5]
            Actv = x[0].replace(" ", "")
            Days = temp[0]
            TimeOfLec = temp[1]
            Bldg_Rm = "REMOTE ONLY"
            Start = temp[4]
            End = temp[5]
            Instructor = cache[1]
            Max_enrl = cache[11]
            Act_enrl = cache[12]
            Seats_avil = cache[13]
            sub_id = cnum.split("-")[0]
            conn.execute(sql,(crn, Instructor, Title, cnum, Actv, Units, Days, TimeOfLec, Bldg_Rm, Start, End, Max_enrl, Act_enrl, Seats_avil, sub_id))
            conn.commit()
            print(f"adding: {x[0]}")
       
    except Error as e:
        conn.rollback()
        print(e)

    return y

def main():
    #scrape data
    driver.get("https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.p_selectsubject")
    driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value = 'N']").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    subjects = driver.find_elements_by_tag_name("h3")
    tables = driver.find_elements_by_tag_name("tr")
    
    ## opening db and adding to it
    database = r"C:/Users/IDC\Documents/Code/DataBases/Project/CSE-111-Course-Registrar/CourseRegistrar/NCR.sqlite3"
    conn = open_conn(database)
    with conn:
        cache = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ## do things
        for sub in subjects:
            insert_sub(conn, sub.text)

        for row in tables:
            x = row.text.split("\n")
            if x[0] != "CRN":
                print(f"passing:{x}")
                print(f"current cache: {cache}")
                y = insert_table(conn, x, cache)
                if x[0] != "      EXAM" and len(y) > 1:
                    cache = y
            
    
    close(conn)
    driver.close()

if __name__ == "__main__":
    main()