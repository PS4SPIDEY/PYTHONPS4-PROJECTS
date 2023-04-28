import pyautogui as auto

from time import sleep
user_value = input("Enter your message...:-")
time_toSent = int(input("How many time do you want to sent:-"))
for i in range(time_toSent):
    auto.write(user_value)
    auto.press('enter')

    sleep(0)