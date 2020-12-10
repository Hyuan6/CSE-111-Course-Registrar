from LegRegAPI import LegacyRegistrationAPI as LRAPI
from time import sleep

crns = [1,2,3,4,5]
student_id = 0

x = LRAPI(crns, student_id)
x.start()
# sleep(10)
# x.close()
