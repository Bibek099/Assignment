from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("https://dev.keela.co/")
driver.find_element(By.id,"user-email").send_keys("qatest@getnada.com")
driver.find_element(By.id,"user-password").send_keys("qatest12345")
driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()

driver.find_element(By.XPATH,"//span[normalize-space()='Contacts']")
driver.find_element(By.XPATH,"//body[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/span[1]").click()

driver.find_element(By.XPATH,'//*[@id="main-container"]/div/div[2]/div[3]/div/div[2]/div[1]/div/button').click()

title=Select(driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/form/div[2]/div[1]/div/div/div/input"))
title.select_by_visible_text("Mr.")

gender=Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/div[7]/div[1]/div[1]/div[1]/input[1]"))
gender.select_by_visible_text("Male")

phn=(driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/div[10]/div[1]/div[1]/div[1]/input[1]"))
phn.send_keys("9812345678")

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/form/div[3]/div/button").click()




driver.close()



