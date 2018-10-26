from selenium import webdriver
import time
# Запускаем chrome
driver = webdriver.Chrome(".\\chromedriver.exe")

# Заходим на сайт lostfilm
driver.get("https://www.lostfilm.tv/")
# Открываем файл series.txt и считываем название сериала
series_name = open(".\\series.txt")
series_name = series_name.readline()
# Открываем файл rating.txt, при его отсутствии создаем такой файл
rating_txt = open(".\\rating.txt", "w")

# Ищем поисковую строку и вводим название сериала из series.txt
search = driver.find_element_by_xpath('//*[@class="search-input"]')
search.send_keys(f'{series_name}')
time.sleep(2)

# Нажимаем на кнопку все результаты
button_all_results = driver.find_element_by_xpath('//*[@class="link-pane"]').click()
time.sleep(1)

# Нажимаем на строку английского названия сериала (на сайте имеется строка с русским названием)
series = driver.find_element_by_xpath(f'//*[@class="name-en" and contains(text(),"{series_name}")]').click()
time.sleep(1)

# Ищем рейтинг сериала
rating = driver.find_element_by_xpath('//*[@class="serie-mark-pane"]')
time.sleep(1)
# Записываем рейтинг сериала в текстовый файл
rating_txt.write("Рейтинг сериала " + series_name + " " + rating.text)

driver.close()