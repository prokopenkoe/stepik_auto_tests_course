import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    firstname.send_keys('user')

    lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lastname.send_keys('userovich')

    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys('user@ovich.ru')

    file = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла