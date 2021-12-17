from selenium import webdriver
from selenium.webdriver.common import keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#Variaveis
userVar="@rod_bock"
passwordVar="%RUVk&ZZ#t27" 
tweetSearch = "segunda eu disse q ia cortar o refrigerante e hj já to tomando coca"
tweetBody = " Teste de comentário do bot"

bot = webdriver.Chrome(options=options, executable_path=r"C:\Users\Rodrigo\Downloads\chromedriver_win32\chromedriver.exe")

bot.get('https://twitter.com/login')
time.sleep(1)

# encontra os elementos email e password pra preencher
user = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
password = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

# limpa e preenche os campos 
user.clear()
user.send_keys(userVar)
password.clear()
password.send_keys(passwordVar)
time.sleep(1)

# Click no botão "Entrar"
bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()
time.sleep(1)


# encontra, limpa, preenche e preciona o enter 
searchIcon = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div')
searchIcon.click()
time.sleep(1)

searchbox = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
searchbox.click()
searchbox.send_keys(tweetSearch)
time.sleep(1) 

searchbox.send_keys(keys.Keys.RETURN)
time.sleep(4) 

   # Busca o tweet
bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]/div/div/article/div/a/div/div[2]/div/span').click()
time.sleep(3)
# Busca o local para inserir a resposta
bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div/div/div/label/div[1]/div/div').click()
tweetAnswer = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
time.sleep(1)
tweetAnswer.send_keys(tweetBody)
time.sleep(1)
    
# Busca o botão pra enviar a resposta do tweet
bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]').click()
time.sleep(3)

bot.get('https://twitter.com/home')
time.sleep(2)

createPost = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
createPost.clear()
createPost.send_keys(tweetBody)
time.sleep(2)

# posta o tweet
bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(2)
# Entra no perfil 
bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div').click()
time.sleep(5)

# Clica nos 3 pontinhos ao lado do post criado anteriormente
bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div').click()
time.sleep(1)

# seleciona a opção de excluir
bot.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[1]').click()
time.sleep(3)

# Clica em excluir para confirmar
bot.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]').click()

# Encontra e executa o click nas opções de perfil(não sei o nome, canto inferior esquerdo, 3 pontinhos do lado do nome)
bot.find_element_by_xpath("//div[@data-testid='SideNav_AccountSwitcher_Button']").click()
time.sleep(1)

# Encontra e executa o click no botão de logout
bot.find_element_by_xpath("//a[@data-testid='AccountSwitcher_Logout_Button']").click()
time.sleep(2)

# Encontra e executa o click no botão de confirmar
bot.find_element_by_xpath("//div[@data-testid='confirmationSheetConfirm']").click()
time.sleep(3) 
    