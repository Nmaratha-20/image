# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Firefox(executable_path ="C:\Users\nsnag\Downloads\chromedriver_win32")
# driver.get("https://www.google.co.in")
# time.sleep(5)
# searchbox = driver.find_element_by_xpath('''/html/body/div/div[3]/form/div[2]/div/div[1]/div/div[1]/input''')
# searchbox.click()
# search = input("Enter Your search: ")
# time.sleep(2)
# searchbox.send_keys(search)
# submit=driver.find_element_by_xpath('''//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]''')
# submit.click()
import pyautogui as p
x,y = p.position()
print(x,y)
