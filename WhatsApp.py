from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Configurações do WebDriver
chrome_options = Options()
chrome_options.add_argument(
    "user-data-dir=C:/Users/Gustavo/AppData/Local/Google/Chrome/User Data"
)  # Perfil do Chrome
chrome_options.add_argument("profile-directory=Profile 1")  # Perfil específico
service = Service(
    "C:/Users/Gustavo/Downloads/Nova pasta/chromedriver-win64/chromedriver.exe"
)  # Caminho do ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)


def send_whatsapp_message():
    try:
        logging.info("Abrindo o WhatsApp Web")
        driver.get("https://web.whatsapp.com/")
        time.sleep(15)  # Espera adicional para garantir o carregamento completo

        logging.info("Aguardando o carregamento da página do WhatsApp Web")
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@role="textbox" and @data-tab="3"]')
            )
        )

        logging.info("Procurando o chat desejado")
        chat_name = "Lobinha ❤️"
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@role="textbox" and @data-tab="3"]')
            )
        )
        search_box.send_keys(chat_name)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        logging.info("Anexando a imagem")
        attach_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span',
                )
            )
        )
        attach_button.click()

        time.sleep(2)

        image_path = "C:/Users/Gustavo/Documents/TI/Projetos/Message_sending_automation/captura_de_tela.png"  # Caminho da imagem
        logging.info(f"Usando o caminho da imagem: {image_path}")

        image_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
        )
        image_input.send_keys(image_path)
        time.sleep(2)

        logging.info("Enviando a imagem")
        send_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))
        )
        send_button.click()

        logging.info("Imagem enviada com sucesso!")
    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")


# Agendamento
##schedule.every(30).minutes.do(send_whatsapp_message)
send_whatsapp_message()

while True:
    schedule.run_pending()
    time.sleep(1)
