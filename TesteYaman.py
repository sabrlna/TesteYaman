from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import os

driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Register.html")
time.sleep(2)

#Preenchendo Nome e Sobrenome#
nome = driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[1]/div[1]/input').send_keys("Sabrina")
time.sleep(1)

sobrenome = driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').send_keys("Souza")
time.sleep(1)

#Preenchendo o campo Endereço#
endereco = driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[2]/div/textarea').send_keys("Rua São Paulo, Osasco - SP")
time.sleep(1)

#Preenchendo Endereço de E-mail#
email = driver.find_element_by_xpath('//*[@id="eid"]/input').send_keys("testeyaman@hotmail.com")
time.sleep(1)

#Preenchendo Número de Telefone#
tel = driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[4]/div/input').send_keys("9673508662")
time.sleep(1)

#Selecionando o Sexo#
sexo = driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[5]/div/label[2]').click()
time.sleep(1)

#Selecionando Hobbies#
hobbies = driver.find_element_by_id("checkbox2").click()
time.sleep(1)

#Linguagens#
linguagem = driver.find_element_by_id("msdd").click()
valorlinguagem = driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[29]/a').click()
time.sleep(1)

#Selecionando Skills#
Select(driver.find_element_by_id("Skills")).select_by_value("Software")

#Selecionando País#
Select(driver.find_element_by_id("countries")).select_by_value("Brazil")

#Selecionar País2#
Select(driver.find_element_by_xpath('//*[@id="country"]')).select_by_index(10)

#Data de Aniversário#
Select(driver.find_element_by_id("yearbox")).select_by_value("2001")
Select(driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[11]/div[2]/select')).select_by_value("February")
Select(driver.find_element_by_id("daybox")).select_by_value("10")

#Senha#
senha = driver.find_element_by_id("firstpassword").send_keys("123Yaman")
time.sleep(1)
confsenha = driver.find_element_by_id("secondpassword").send_keys("123Yaman")

#Foto#
driver.find_element_by_xpath("//input[@type='file']").send_keys(os.getcwd()+'/yamanfoto.jpg')

#Confirmar Registro#
btnconfirmar = driver.find_element_by_id("submitbtn").click()

driver.get("http://demo.automationtesting.in/WebTable.html")
time.sleep(3)

#Apagar Registro#
apagar = driver.find_element_by_xpath('/html/body/section/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div[6]/user-click-select/div[1]/del-click/button/i')
ActionChains(driver).context_click(apagar).perform()
time.sleep(2)

#Confirmar Exclusão#
driver.find_element_by_xpath('/html/body/section/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div[6]/user-click-select/div[1]/div/ul/li[1]/button').click()
driver.switch_to.alert.accept()