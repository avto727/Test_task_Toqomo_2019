::@echo off
chcp 1251
echo Start %time%

pytest "D:\PycharmProjects\Test_task_Toqomo_2019\test_main_page.py" -s --alluredir D:\PycharmProjects\Test_task_Toqomo_2019\results

echo Stop %time%
::timeout /t 15
C:\Users\hp\scoop\shims\allure generate results --clean
timeout /t 15
C:\Users\hp\scoop\shims\allure serve results

pause
