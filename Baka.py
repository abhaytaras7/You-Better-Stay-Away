import pyautogui , time
time.sleep(10)
f = open ("onichan.txt",'r')

for word in f:
  pyautogui.typewrite(word)
  
  time.sleep(4)
  
  pyautogui.press("enter")

