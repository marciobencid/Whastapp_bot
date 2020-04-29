from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

class WhastappBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)
        #self.contatos =['Josenilto G&P','Baixola']
        self.contatos = open('./lista_contatos.txt','r',encoding="utf8").readlines()
        self.texto = open('./mensagem.txt','r',encoding="utf8").readlines()
        self.data_atual = datetime.now()
        self.data_arq = self.data_atual.strftime('%d_%m_%Y_%H_%M_%S')
        self.lista_contatos_saida = open('./lista_contatos_saida_'+ self.data_arq +'.txt','a')

    def EnviarMensagens(self):  
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)
        
        for contato in self.contatos:
            data_e_hora = self.data_atual.strftime('%d/%m/%Y/%H-%H:%M:%S')
            print(contato + ' - ' + data_e_hora)
            
             #COMANDO BOT        
            contato = self.driver.find_element_by_xpath(f"//span[@title='{contato}']")
            time.sleep(3)
            contato.click()
            chat_box = self.driver.find_element_by_class_name("_1Plpp")
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.texto)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

            # ESCEVER NO ARQUIVo
            #não grava no arquivo
            self.lista_contatos_saida.append(data_e_hora + contato)
            time.sleep(3)
        

            
bot = WhastappBot()
bot.EnviarMensagens()