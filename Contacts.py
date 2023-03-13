from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver =webdriver.Chrome()
driver.get("https://dev.keela.co/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='user-email']").send_keys("qatest@getnada.com")
driver.find_element(By.ID,"user-password").send_keys("qatest12345")
driver.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/div/div/div/div/div/div/form/div/div/div[3]/div/div/button").click()

driver.find_element(By.XPATH,'//*[@id="sidebar"]/div[2]/ul[2]/li[3]/a/span').click()
driver.find_element(By.XPATH,'//*[@id="main-container"]/div/div[2]/div/div/div[1]/div[2]/button[5]')

driver.find_element(By.ID,"gsbF5pRhWbrZ66M7K").send_keys("Bibek")
driver.find_element(By.ID,"KCuQe6ccXHtChBiQD").send_keys("Adhikari")
driver.find_element(By.ID,"D93LvPWtx4h9yfhD3").send_keys("test@gmail.com")


company=driver.find_element(By.XPATH,"//input[@id='h9ueYjkuETfjGnx93']")
company.select_by_visible_text("QA COMPANY")

priority =Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[3]/div[4]/div[1]/div[1]/div[1]/select[1]"))
priority.select_by_visible_text("Medium")

date=Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[7]/div[1]/div[1]/div[1]/input[1]"))
date.select_by_visible_text("10")

driver.find_element(By.ID,"bkrQgMFkqdTJXaXZastreet").send_keys("Kathmandu,Nepal")

driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/button[1]").click()



time.sleep(5)


