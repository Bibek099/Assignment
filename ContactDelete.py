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

driver.find_element(By.XPATH,"//*[@id="sidebar"]/div[2]/ul[2]/li[3]/a/span").click()
driver.find_element(By.XPATH,"//td[@align='center']").click()

driver.find_element(By.XPATH,'//*[@id="mdkxfk2ZBvcrzx4He"]/i').click()
driver.find_element(By.XPATH,"//a[normalize-space()='Delete Contact']").click()
driver.find_element(By.XPATH,"//input[contains(@class,'swal2-input')]").send_keys("DELETE")

driver.find_element(By.XPATH,"//button[normalize-space()='Confirm']").click()

driver.close()



