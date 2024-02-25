from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook


list1 = []
list2 = []
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.only.com/it-it/womens-fashion/jeans")
time.sleep(8)
driver.find_element(By.XPATH,'//span[text()="Reject All"]').click()
time.sleep(4)

# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(3)
# jeansName = driver.find_elements(By.XPATH,'//span[@class = "product-tile-info__title ellipsis"]')
# time.sleep(5)
#
# for i in jeansName:
#     list1.append(i.text)
# print(list1)
# print(len(list1))

while True:
    try:
        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(4)
        jeansName = driver.find_elements(By.XPATH, '//span[@class = "product-tile-info__title ellipsis"]')
        for i in jeansName:
            list1.append(i.text)
        time.sleep(2)
        jeansPrice = driver.find_elements(By.XPATH,'//div[@class = "product-price__list-price" or @class = "product-price__discounted-price product-price__price-pad"]')
        for j in jeansPrice:
            list2.append(j.text)
        time.sleep(4)
        driver.find_element(By.XPATH, '//li[@class = "paginator__item paginator__item--arrow-right"]').click()
    except:
        break

print(list1)
print(len(list1))
print(list2)
print(len(list2))

final = list(zip(list1 , list2))
wb = Workbook()
sh=wb.active
wb["Sheet"].title = "OnlyData"
sh.append(["Name","Price"])
for z in final:
    sh.append(z)
wb.save("onlyWomenJeansData.xlsx")