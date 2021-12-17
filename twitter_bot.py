from selenium import webdriver
from selenium import common
from selenium.webdriver.common import keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

bot = webdriver.Chrome(options=options, executable_path=r"C:\Users\Rodrigo\Downloads\chromedriver_win32\chromedriver.exe")
bot.get('https://twitter.com/login')

#Quantidade que quer comentar, +1 para igualar a sequencia que o tt exige
cycles = 1
cycles += 1
tweetSearch = "segunda eu disse q ia cortar o refrigerante e hj já to tomando coca"
tweetBody = "Teste de comentário do bot"

time.sleep(1)
try:
    # encontra os elementos email e password pra preencher
    email = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
    password = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
except common.exceptions.NoSuchElementException:
    time.sleep(3)
    email = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
    password = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')


    # limpa e preenche os campos 
email.clear()
email.send_keys('usuario')
password.clear()
password.send_keys('senha')

# Click no botão "Entrar"
time.sleep(1)
bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()
time.sleep(1)

try:
    searchbox = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div')
except common.exceptions.NoSuchElementException:
    time.sleep(2)
    searchbox = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div')

# Limpa, preenche e preciona o enter 
searchbox.click()
time.sleep(1)


try:
    searchboxInput = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
except common.exceptions.NoSuchElementException:
    time.sleep(2)
    searchboxInput = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')

searchboxInput.click()
searchboxInput.send_keys(tweetSearch)
time.sleep(1) 
searchboxInput.send_keys(keys.Keys.RETURN)
time.sleep(3) 

# Executa a quantidade que for colocada, 10 por padrão
for i in range(1, cycles):
    # Busca o tweet, colocando o valor do array igual a i
    bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[' + str(i) + ']').click()
    time.sleep(3)
    # Busca o local para inserir a resposta
    bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div/div/div/label/div[1]/div/div').click()
    tweetAnswer = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    time.sleep(1)
    tweetAnswer.send_keys(tweetBody)
    time.sleep(1)
    
    # Busca o botão pra enviar a resposta do tweet
    #bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]').click()
    time.sleep(3)

bot.get('https://twitter.com/home')
time.sleep(4)

# Encontra e executa o click nas opções de perfil(não sei o nome, canto inferior esquerdo, 3 pontinhos do lado do nome)
try:
    bot.find_element_by_xpath("//div[@data-testid='SideNav_AccountSwitcher_Button']").click()
except common.exceptions.NoSuchElementException:
    time.sleep(3)
    bot.find_element_by_xpath("//div[@data-testid='SideNav_AccountSwitcher_Button']").click()

time.sleep(1)

      # Encontra e executa o click no botão de logout
try:
    bot.find_element_by_xpath("//a[@data-testid='AccountSwitcher_Logout_Button']").click()
except common.exceptions.NoSuchElementException:
    time.sleep(2)
    bot.find_element_by_xpath("//a[@data-testid='AccountSwitcher_Logout_Button']").click()
    
    time.sleep(3)

    # Encontra e executa o click no botão de confirmar
try:
    bot.find_element_by_xpath("//div[@data-testid='confirmationSheetConfirm']").click()
except common.exceptions.NoSuchElementException:
    time.sleep(3)
    bot.find_element_by_xpath("//div[@data-testid='confirmationSheetConfirm']").click()

time.sleep(3) 
    