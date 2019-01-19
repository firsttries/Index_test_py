from selenium import webdriver                           #Импорт вебдрайвера
from tqdm import tqdm                                    #Импорт прогрессбара

driver = webdriver.Chrome()                              #Инициализация драйвера(браузера)


driver.get("https://s3.eu-central-1.amazonaws.com/qa-web-test-task/1.html") #Начальный сайт

#driver.minimize_window()                                #Минимизация окна

for x in tqdm(range(9998)):                              #Цикл до конечного сайта
    try:                                                 #Если ссылка найдена
        driver.find_element_by_xpath("/html/body/a").click()
    except:                                              #Если ссылки нет
        print(driver.current_url)                        #Печать URL сайта без ссылки
        driver.get('https://s3.eu-central-1.amazonaws.com/qa-web-test-task/{}.html' .format(x+1)) #Перейти на следущий сайт
driver.close()
