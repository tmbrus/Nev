from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 1. Укажите путь к yandexdriver.exe (скачайте его с GitHub)
service = Service(r'C:\WebDriver\bin\yandexdriver.exe')  # Пример пути, замените на свой

# 2. Укажите путь к Яндекс.Браузеру (обычно в AppData)
options = Options()
options.binary_location = r'C:\Users\tmbru\AppData\Local\Yandex\YandexBrowser\Application\browser.exe'

# 3. Запуск браузера
driver = webdriver.Chrome(service=service, options=options)

# Открыть страницу
driver.get("https://ya.ru")

# Проверка (выведет версию браузера)
print("Версия Яндекс.Браузера:", driver.capabilities['browserVersion'])

# Закрыть браузер (раскомментируйте, когда будете готовы)
# driver.quit()