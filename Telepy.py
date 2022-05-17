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
bot = telebot.TeleBot('') # here you paste your bot's API, which you can get in "BotFather" bot
@bot.message_handler(content_types=['text','document', 'audio'])
 
def get_text_messages(message):
    # bot's interface
    bot.send_message(message.from_user.id, "Commands\n\n\n"             "1 - close browser\n\n"       "2 - screenOff function\n\n"        "3 - shutdown computer\n\n"       "4 - turn off the camera\n\n"       "5 - iplogger\n\n"       "6 - screenphotos")
    
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
# display screen resolution, get it using pyautogui itself
            SCREEN_SIZE = tuple(pyautogui.size())
# define the codec
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
# frames per second
            fps = 12.0
# create the video write object
            out = cv2.VideoWriter("output.avi", fourcc, fps, (SCREEN_SIZE))
# the time you want to record in seconds
            record_seconds = 1000
            for i in range(int(record_seconds * fps)):
    # make a screenshot
                img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
                frame = np.array(img)
    # convert colors from BGR to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
                out.write(frame)
    # show the frame
                cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
                if cv2.waitKey(1) == ord("q"):
                    break
        except:
            print("sww")
# make sure everything is closed when exited
    cv2.destroyAllWindows()
    out.release()
                
bot.polling(none_stop=True, interval=0)
