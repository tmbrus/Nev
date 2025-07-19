from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди поле "Email" и заполни его
driver.find_element(By.ID, 'email').send_keys('kurohtin_26@gmail.com')

# Найди поле "Пароль" и заполни его
driver.find_element(By.ID, 'password').send_keys('AaZ-cYD-Kt2-H3d')

# Найди кнопку "Войти" и кликни по ней
driver.find_element(By.CLASS_NAME, 'auth-form__button').click()

# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'header__logout')))

# Найди кнопку, получи её текст и проверь, что он равен 'Выйти'
assert driver.find_element(By.CLASS_NAME, 'header__logout').text == 'Выйти'

driver.quit()
