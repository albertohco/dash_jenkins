import pytest
import time
from selenium import webdriver

chrome_path = "/home/local_us/dash/chrome-linux64/chrome"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path
driver = webdriver.Chrome(options=chrome_options)

url = "http://127.0.0.1:8080"

# teste da página inicial
driver.get(url)
time.sleep(10)
assert "Dash" in driver.title
assert "pagina inicial" in driver.page_source
print("Teste da pagina inicial com sucesso!")

# teste da página do formulário
driver.get(url + "/formulario")
time.sleep(10)
assert "Dash" in driver.title
assert "Preencha as informações abaixo e clique em prever para rodar o modelo" in driver.page_source
print("Teste da pagina do formulario com sucesso!")

# teste da página de gráficos
driver.get(url + "/graficos")
time.sleep(10)
assert "Dash" in driver.title
assert "Histograma de idades" in driver.page_source
print("Teste da pagina de graficos com sucesso!")

driver.quit()