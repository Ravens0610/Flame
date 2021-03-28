print("Flame OS")
print("Authorize Clearance")
viewer=input("Put Password: ")
if viewer == "flamepassword":
  print("Authorized.")
  import webbot
  import os
  import time
  import random
  os.system('pip3 install pyautogui')
  driver = webbot.Browser()
  print("")
  tab = 1
add = 1
while True:
  input_elements = driver.find_elements(xpath='//input')
  driver.type(driver.Key.TAB,into=input_elements[0].text)
  driver.type(code)
  driver.type(driver.Key.ENTER,into=input_elements[0].text)
  time.sleep(0.8)
  input_elements = driver.find_elements(xpath='//input')
  driver.type(driver.Key.TAB,into=input_elements[0].text)
  driver.type(username)
  driver.type(driver.Key.ENTER,into=input_elements[0].text)
  time.sleep(2)
  driver.execute_script("window.open('https://scifire.repl.co');")
  tab = tab + add
  driver.switch_to_tab(tab)
  time.sleep(5)