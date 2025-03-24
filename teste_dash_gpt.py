import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_path = "/home/local_us/dash/chrome-linux64/chrome"

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.binary_location = chrome_path
    #chrome_options.add_argument("--headless")  # Executa sem abrir o navegador
    chrome_options.add_argument("--no-sandbox")  # Necessário para ambientes Linux
    chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemas de memória
    
    # Criar serviço do WebDriver
    service = Service("/home/local_us/dash/chromedriver-linux64/chromedriver")  # Caminho do ChromeDriver

    # Inicializar WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

def test_pagina_inicial(driver):
    url = "http://127.0.0.1:8080"
    driver.get(url)
    time.sleep(5)  # Use `WebDriverWait` para melhorar performance
    assert "Dash" in driver.title
    assert "pagina inicial" in driver.page_source
    print("Teste da página inicial com sucesso!")

def test_pagina_formulario(driver):
    url = "http://127.0.0.1:8080/formulario"
    driver.get(url)
    time.sleep(5)
    assert "Dash" in driver.title
    assert "Preencha as informações abaixo e clique em prever para rodar o modelo" in driver.page_source
    print("Teste da página do formulário com sucesso!")

def test_pagina_graficos(driver):
    url = "http://127.0.0.1:8080/graficos"
    driver.get(url)
    time.sleep(5)
    assert "Dash" in driver.title
    assert "Histograma de idades" in driver.page_source
    print("Teste da página de gráficos com sucesso!")
