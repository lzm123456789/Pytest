import os
import time

while True:
    my_time = time.strftime('%H_%M')
    if my_time == '19_11':
        os.system('pytest --alluredir Temp --allure-stories=PC端用户相关功能 --clean-alluredir')
        os.system('allure generate Temp -o TestReport/Report --clean')
        break
    else:
        time.sleep(5)
        print(time.strftime('%H_%M_%S'))