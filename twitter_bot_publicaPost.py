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
time.sleep(3)
bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()
time.sleep(5)

# Entra na conta, seleciona o campo de escrever um tweet

createPost = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
createPost.clear()
createPost.send_keys(tweetBody)
time.sleep(2)

# posta o tweet

bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()

time.sleep(2)

# Entra no perfil 

bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div').click()

time.sleep(4)

# Clica nos 3 pontinhos ao lado do post criado anteriormente

bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div').click()

time.sleep(1)

# seleciona a opção de excluir

bot.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[1]').click()

time.sleep(3)

# Clica em excluir para confirmar

bot.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]').click()

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
    