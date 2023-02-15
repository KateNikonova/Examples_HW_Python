from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # вызов вебдрайвера для Google Chrome
driver.implicitly_wait(5) # задаем неявное ожидание 5 сек
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")  # передаем  URL в браузер
driver.fullscreen_window()   # открыть окно на полный размер

# заполняем все поля ввода кроме индекса
driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Маша")
driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Иванова")
driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Невский пр. 70")
driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Санк-Петербург")
driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("ivanova45@gmail.com")
driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+79509001212")
driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA Engineer")
driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "button.btn").click()

# Смотрим какого цвета поля все - в том числе и индекс
first_name = driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("color")
last_name = driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("color")
address = driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("color")
city = driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("color")
country = driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("color")
e_mail = driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("color")
phone_number = driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("color")
job_position = driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("color")
company = driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("color")
zip = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")


driver.quit() # закрываем браузер

# задаем цвета
colour_green = "rgba(15, 81, 50, 1)"
colour_red = "rgba(132, 32, 41, 1)"

# проверям равны ли фактические цвета элементов ожидаемым цветам
@pytest.mark.parametrize('per, color', [(company, colour_green),
                                        (job_position, colour_green),
                                        (first_name, colour_green),
                                        (last_name, colour_green),
                                        (address, colour_green),
                                        (city, colour_green),
                                        (country, colour_green),
                                        (e_mail, colour_green),
                                        (phone_number, colour_green),
                                        (zip, colour_red)])
def test_green(per, color):
    assert per == color
