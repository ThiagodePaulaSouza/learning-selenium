from unittest import expectedFailure
from selenium import webdriver
from time import sleep
navegador = webdriver.Chrome(executable_path='D:\\chromeDriver\\chromedriver.exe')
url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
navegador.get(url)
sleep(5)
# logica 1
# Click on "clique aqui" enquanto o numero esperado for false
# if expected number is true stop click on "clique aqui"
a = navegador.find_element_by_tag_name('a')
receive = navegador.find_elements_by_tag_name('p')

expected = int((receive[1].text).split(' ')[-1])

while True:
    a.click()
    receive = navegador.find_elements_by_tag_name('p')
    if receive[-1].text == f"Você ganhou: {expected}":
        break

# logica 2
# se expected number is false click on clique aqui se n pare