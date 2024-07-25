import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_argument(
    "--headless"
)  # Executar o navegador em modo headless (sem interface gráfica)

# Inicializa o driver
service = Service(
    "C:/Users/Gustavo/Downloads/Nova pasta/chromedriver-win64/chromedriver.exe"
)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abre a página web
url = "https://app.powerbi.com/view?r=eyJrIjoiNDI3NGFlNWEtYTU4NC00MWFlLWE0ZTMtZDIyZmU0NmJhZmY5IiwidCI6IjBmODE0NjljLWNmZTYtNDE4OC1hMjQ4LThhNjEyZDg5NGEwOCJ9"
driver.get(url)
time.sleep(20)
# Tira a captura de tela
screenshot_path = "Screenshot.png"
driver.save_screenshot(screenshot_path)

# Fecha o navegador
driver.quit()

print(f"Screenshot saved in:{screenshot_path}")
