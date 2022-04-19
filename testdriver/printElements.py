#cada chave do valor devera ser o valor de atributo
#cada valor deve ser o texto contido no elemento
from selenium import webdriver
from time import sleep
navegador = webdriver.Chrome(executable_path='D:\\chromeDriver\\chromedriver.exe')
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
navegador.get(url)
sleep(1)

titulo = navegador.find_element_by_tag_name('h1')

print("({" f"'{titulo.text}'" ': ' ' {')
for i in range(3):
    p = navegador.find_elements_by_tag_name('p')
    print(f"    'texto{i+1}'" ': ' f"'{p[i].text}'")
print('}})')
