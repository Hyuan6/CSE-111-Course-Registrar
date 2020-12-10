from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import sqlite3
import re

from time import sleep

YEAR_IN_SCHOOL_CHOICES = ['Freshmen', 'Sophmore', 'Junior', 'Senior', 'Graduate']
DATABASE = f"../../db.sqlite3"
COURSE_REGEX_PATTERN = re.compile("[A-Z]{2,5} [0-9]{2,4}")

def open_conn(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)

    return conn

def close(conn):
    try:
        conn.close()
        print("db closed")
    except Error as e:
        print(e)

def main():
    options = Options()
    options.add_argument('headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
    driver.implicitly_wait(3)

    driver.get("https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.p_selectsubject")
    driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value = 'N']").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    for crn in driver.find_elements_by_tag_name("a"):

        crn_text = crn.text 
        print(crn_text)
        crn_href = crn.get_attribute("href")

        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(crn_href)

        values = driver.find_elements_by_class_name("dedefault")
        labels = driver.find_elements_by_class_name("delabel")

        classStanding = False
        levelStatusNegative = False

        for label in labels:
            if "class level must be on of the following" in label.text:
                classStanding = True
            if "level status can not be one of the following" in label.text:
                levelStatusNegative = True

        cs = []
        pr = []

        if not classStanding and levelStatusNegative:
            for i in range(4):
                cs.append(YEAR_IN_SCHOOL_CHOICES[i])

        else:
            for ele in values:
                if ele.text == "Graduate" and len(cs) > 0:
                    continue
                if ele.text in YEAR_IN_SCHOOL_CHOICES:
                    cs.append(ele.text)

        for ele in values:
            preReqs = COURSE_REGEX_PATTERN.findall(ele.text)

            for pReq in preReqs:
                pr.append(pReq)

        # print("")

        while len(cs) < 4:
            cs.append("null")

        while len(pr) < 5:
            pr.append("null")

        # for i in cs:
        #     print(i)

        # print("")

        # for i in pr:
        #     print(i)

        # print("")

        sql = f"""insert into RegistrationPage_requirments (cs1, cs2, cs3, cs4, pr1, pr2, pr3, pr4, pr5, course_id)
                  values ('{cs[0]}', '{cs[1]}', '{cs[2]}', '{cs[3]}', '{pr[0]}', '{pr[1]}', '{pr[2]}', '{pr[3]}', '{pr[4]}', '{crn_text}')"""

        conn = open_conn(DATABASE)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

        driver.close()

        driver.switch_to_window(driver.window_handles[0])

    driver.quit()

def reqTest():
    url = "https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.P_ViewCrnDetail?subjcode=ANTH&crsenumb=003&validterm=202110&crn=10158"

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
    driver.implicitly_wait(3)
    driver.get(url)

    values = driver.find_elements_by_class_name("dedefault")
    labels = driver.find_elements_by_class_name("delabel")

    classStanding = False
    levelStatusNegative = False

    for label in labels:
        if "class level must be on of the following" in label.text:
            classStanding = True
        if "level status can not be one of the following" in label.text:
            levelStatusNegative = True

    cs = []
    pr = []

    if not classStanding and levelStatusNegative:
        for i in range(4):
            cs.append(YEAR_IN_SCHOOL_CHOICES[i])

    else:
        for ele in values:
            if ele.text == "Graduate" and len(cs) > 0:
                continue
            if ele.text in YEAR_IN_SCHOOL_CHOICES:
                cs.append(ele.text)

    for ele in values:
        preReqs = COURSE_REGEX_PATTERN.findall(ele.text)

        for pReq in preReqs:
            pr.append(pReq)

    print("")

    while len(cs) < 4:
        cs.append("null")

    while len(pr) < 5:
        pr.append("null")

    for i in cs:
        print(i)

    print("")

    for i in pr:
        print(i)

    print("")

main()

# reqTest()