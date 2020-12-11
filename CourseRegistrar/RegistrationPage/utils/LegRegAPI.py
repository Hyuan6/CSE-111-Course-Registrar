from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class LegacyRegistrationAPI:
    def __init__(self, crns, student_ID):
        self.options = Options()
        self.options.add_argument('headless')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')

        self.crns = crns #[1,2,3,4,5]
        self.student_ID = student_ID #0
        self.port = 8000
        self.url = f"http://127.0.0.1:{self.port}/LegReg/"

    def start(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        self.driver.get(self.url)

        self.driver.execute_script(f"document.getElementById(\"student_id\").value = \"{self.student_ID}\"")

        for key, val in enumerate(self.crns):
            crnInputId = f"crn_id{key+1}"
            self.driver.execute_script(f"document.getElementById(\"{crnInputId}\").value = \"{val}\"")

        self.driver.find_element_by_id("submit_button").click()
        
        sleep(10)

        self.driver.quit()

    def setPort(self, portId):
        self.port = portId
        self.url = f"http://192.168.1.144:{self.port}/LegReg/"

    def close(self):
        self.driver.quit()