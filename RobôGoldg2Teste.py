import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import requests

chrome_options = Options()
chrome_options.add_argument("-headless")
driver = webdriver.Chrome (options = chrome_options)
driver.get('https://blaze.com/pt/games/double')
sleep(5)

analise = '👑Esta esperando o que?'
win = '🤑✅GRENNNNN \n✔️ Bateu á meta! vaza'
galee1 = '😜✅GRENNN GALE 1'
galee2= '😜✅GRENNN GALE 2'
win_branco = '🥳⚪️GREENN BRANCOOOOO \n✔️mais 14x para banca'
loss = '❌👎LOOSS \n✔️ Não foi dessa vez'
nao_confirmacao = '✋Falhou! Aguarde o próximo...'

def esperar():
    while True:
        try:
            driver.find_element(By.CLASS_NAME,'time-left').find_element(By.TAG_NAME,'span').text
            break
        except:
            pass
    
    while True:
        try:
            driver.find_element(By.CLASS_NAME,'time-left').find_element(By.TAG_NAME,'span').text
        except:
            break
        
def retornar_historico():
    return [i['color'] for i in requests.get('https://blaze.com/api/roulette_games/recent').json()][::-1]

            
def retornar_ultimo():
    return requests.get('https://blaze.com/api/roulette_games/current').json()['color']

def martin_gale(gale,ultimo):
    enviar_mensagem(gale)
    esperar()
    sleep(9.0)
    ultimo_ = retornar_ultimo()
    if ultimo_ != ultimo and ultimo_ != 0:
        enviar_mensagem(win)
        return True
    elif ultimo_ == 0: 
        enviar_mensagem(win_branco)
        return True

def enviar_mensagem(mensagem):
    bot = '6230037536:AAFzbNZVV_zo0ILKfiok07Q87NlQUjRTnaA'
    chat_id = '-1001839680825'
    url_compra = '😱😎TENHA MAIS GANHOS\n➡️[ADQUIRA SEU ACESSO VIP AQUI](https://pay.kiwify.com.br/KNj8gZq)'
    url = f'https://api.telegram.org/bot{bot}/sendMessage?chat_id={chat_id}&text={mensagem}\n{url_compra}&parse_mode=Markdown'
    requests.get(url)

def remove_thumb(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='COMPRE A SALA VIP AQUI', disable_web_page_preview=True)

cor = ['BRANCO','PRETO','VERMELHO']
simbolo = ['⚪️','⚫️','🔴']

print('')
enviar_mensagem('')

while True:
    try:
        esperar()
        sleep(9.5)
        historico = retornar_historico()
        ultimo = retornar_ultimo()
        historico.append(ultimo)
        padrao = historico[-4::]
    
        confirmacao = f'✅ APOSTAR {simbolo[padrao[0]]} {cor[padrao[0]]}\n{simbolo[0]} BRANCO (PROTEÇÃO)\n🔹 NO MÁXIMO 2 GALE'
        gale1 = f'🎯✅ ENTRE GALE 1\nOPCIONAL/ GERENCIE-SE' 
        gale2 = f'🎯✅ ENTRE GALE 2\nOPCIONAL/ GERENCIE-SE'
        if padrao == [1,1,1,1] or padrao == [2,2,2,2] or padrao == [1,2,1,2] or padrao == [2,1,2,1]: 
         enviar_mensagem()
         esperar()
         sleep(10)
         ultimo = retornar_ultimo()
        while True:
                if ultimo == padrao[0]:
                    enviar_mensagem(confirmacao)
                    esperar()
                    sleep(11)
                    ultimo_ = retornar_ultimo()
                    if ultimo_ != ultimo and ultimo_ != 0:
                        enviar_mensagem(win)
                        break
                    elif ultimo_ == 0:
                        enviar_mensagem(win_branco)
                        break
                    else:
                        if martin_gale(gale1,ultimo):
                            break
                        else:
                            if martin_gale(gale2,ultimo):
                                break
                            else:
                                enviar_mensagem(loss)
                                break
                                      
                else:
                    enviar_mensagem()
                    break
    except Exception as e:
        print(e)
        driver.get('https://blaze.com/pt/games/double')
        sleep(10)
        pass