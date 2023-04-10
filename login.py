from main import Bot
from datetime import datetime
from bs4 import BeautifulSoup
import bd
import time
import json
import requests
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

login = os.environ.get('LOGIN')
password = os.environ.get('PASSWORD')
win_quit = os.environ.get('WINS')
loss_quit = os.environ.get('LOSS')


bot = Bot()

bot.Start()

login, reason = bot.Login(login , password)


#Entrada
betRed = {
    "color": "red", "amount": 1.2  # GREEN: 1,0
}
betBlack = {
    "color": "black", 'amount': 1.2  # GREEN: 1,0
}
betWhite = {
    "color": "white", "amount": 0.2  # GREEN: 1,4
}

#Martigale 1
betRed_g1 = {
    "color": "red", "amount": 2.8 # G1: 1,0
}
betBlack_g1 = {
    "color": "black", 'amount': 2.8 # G1: 1,0
}
betWhite_g1 = {
    "color": "white", "amount": 0.4 # G1: 1,2
}

#Martigale 2
betRed_g2 = {
    "color": "red", "amount": 6.5 # G2: 1,0
}
betBlack_g2 = {
    "color": "black", 'amount': 6.5 # G2: 1,0
}
betWhite_g2 = {
    "color": "white", "amount": 0.9 # G2: 0,6    ///  LOSS: 12,0
}




print('Os Sinais Comerçara em 15s...')
time.sleep(15)
print('Os Sinais Comerçara em instante')


# Sair quando bate a Meta
def meta():

    # Sair Quando fazer 2 Wins
    if bd.Win == win_quit:
        bot.Stop()

    # Sair Quando bate 1 Loss
    if bd.Loss == loss_quit:
        bot.Stop()



def horas():
    atual = datetime.now()

    data_hora = atual.strftime("%d/%m/%Y, %H:%M:%S")

    print("Data e Horas do Reset:",data_hora)


def reset():
    bd.estrategy_name = 'TRUE'
    bd.direction_color = 'NULL'
    bd.analisar = 0
    bd.gale_atual = 0
    horas()
    meta()


def martingales():
    def very_gale(num):
        if num[0:1] == [0]:
            if bd.gale_atual == 0:
                print('BRANCO SEM GALE')

                bd.Win += 1
                bd.Branco +=1
                bd.Win_consecutivo += 1
                if bd.Win + bd.Loss !=0:
                    a = 100 / (bd.Win + bd.Loss) * bd.Win
                else:
                    a = 0

                bd.Win_hat = (f'{a:,.2f}%')
            
                print("Win", bd.Win)
                print("Loss", bd.Loss)
                print("Branco", bd.Branco)
                print("Porcentagem", bd.Win_hat)

                reset()
                return

            if bd.gale_atual == 1:
                print('BRANCO 1ª GALE')

                bd.Win += 1
                bd.Branco +=1
                bd.Win_consecutivo += 1
                if bd.Win + bd.Loss !=0:
                    a = 100 / (bd.Win + bd.Loss) * bd.Win
                else:
                    a = 0

                bd.Win_hat = (f'{a:,.2f}%')

                print("Win", bd.Win)
                print("Loss", bd.Loss)
                print("Branco", bd.Branco)
                print("Porcentagem", bd.Win_hat)


                reset()
                return

            if bd.gale_atual == 2:
                print('BRANCO 2ª GALE')


                bd.Win += 1
                bd.Branco +=1
                bd.Win_consecutivo += 1
                if bd.Win + bd.Loss !=0:
                    a = 100 / (bd.Win + bd.Loss) * bd.Win
                else:
                    a = 0

                bd.Win_hat = (f'{a:,.2f}%')

                
                
                print("Win", bd.Win)
                print("Loss", bd.Loss)
                print("Branco", bd.Branco)
                print("Porcentagem", bd.Win_hat)
                

                reset()
                return

        if num[0:1] > [0] and num[0:1] <= [7] and bd.direction_color == '🔴':
            if bd.gale_atual == 0:
                print('GREEN')


                bd.Win +=1
                bd.Win_consecutivo += 1
                if bd.Win + bd.Loss !=0:
                    a = 100 / (bd.Win + bd.Loss) * bd.Win
                else:
                    a = 0
        
                bd.Win_hat = (f'{a:,.2f}%')      



                print("Win", bd.Win)
                print("Loss", bd.Loss)
                print("Branco", bd.Branco)
                print("Porcentagem", bd.Win_hat)

                
                reset()
                return

            if bd.gale_atual == 1:
                print('WIN 1ª GALE')


                bd.Win += 1
                bd.Win_gale1 +=1
                bd.Win_consecutivo += 1
                if bd.Win + bd.Loss !=0:
                    a = 100 / (bd.Win + bd.Loss) * bd.Win
                else:
                    a = 0

                bd.Win_hat = (f'{a:,.2f}%')

                print("Win", bd.Win)
                print("Loss", bd.Loss)
                print("Branco", bd.Branco)
                print("Porcentagem", bd.Win_hat)
                

                reset()
                return

            if bd.gale_atual == 2:
                print('WIN 2ª GALE')


                bd.Win += 1
                bd.Win_gale2 +=1
                bd.Win_consecutivo += 1
                if bd.Win + bd.Loss !=0:
                    a = 100 / (bd.Win + bd.Loss) * bd.Win
                else:
                    a = 0
        
                bd.Win_hat = (f'{a:,.2f}%')


                print("Win", bd.Win)
                print("Loss", bd.Loss)
                print("Branco", bd.Branco)
                print("Porcentagem", bd.Win_hat)
                

                reset()
                return

        if num[0:1] >= [8] and num[0:1] <= [14] and bd.direction_color == '⚫':
            if bd.gale_atual == 0:
                print('GREEN')
                

                bd.Win +=1
                bd.Win_consecutivo += 1
                if bd.Win + bd.Loss !=0:
                    a = 100 / (bd.Win + bd.Loss) * bd.Win
                else:
                    a = 0
                
                bd.Win_hat = (f'{a:,.2f}%')

            


                print("Win", bd.Win)
                print("Loss", bd.Loss)
                print("Branco", bd.Branco)
                print("Porcentagem", bd.Win_hat)
                

                reset()
                return

            if bd.gale_atual == 1:
                print('WIN 1ª GALE')

                bd.Win += 1
                bd.Win_gale1 +=1
                bd.Win_consecutivo += 1
                if bd.Win + bd.Loss !=0:
                    a = 100 / (bd.Win + bd.Loss) * bd.Win
                else:
                    a = 0
        
                bd.Win_hat = (f'{a:,.2f}%')


                print("Win", bd.Win)
                print("Loss", bd.Loss)
                print("Branco", bd.Branco)
                print("Porcentagem", bd.Win_hat)
                

                reset()
                return

            if bd.gale_atual == 2:
                print('WIN 2ª GALE')
                

                bd.Win += 1
                bd.Win_gale2 += 1
                bd.Win_consecutivo += 1

                if bd.Win + bd.Loss !=0:
                    a = 100 / (bd.Win + bd.Loss) * bd.Win
                else:
                    a = 0
                bd.Win_hat = (f'{a:,.2f}%')


                print("Win", bd.Win)
                print("Loss", bd.Loss)
                print("Branco", bd.Branco)
                print("Porcentagem", bd.Win_hat)


            reset()
            return


        if num[0:1] >= [8] and num[0:1] <= [14] and bd.direction_color == '🔴':
            if bd.gale_atual == 0:
                bd.gale_atual += 1
                print('VAMOS PRO GALE 1º 🐓')
                doubleBet = bot.Bet(game="double", bets=[betRed_g1, betWhite_g1],
                return_results=True)

                print('Cores apostado no Martingale 1º:',doubleBet)
                

                return

            if bd.gale_atual == 1:
                bd.gale_atual += 1
                print('VAMOS PRO GALE 2º 🐓')
                doubleBet = bot.Bet(game="double", bets=[betRed_g2, betWhite_g2],
                return_results=True)

                print('Cores Apostado no Martingale 2º:',doubleBet)
                

                return

            if bd.gale_atual == 2:
                print('LOSS❌')

                bd.Loss += 1
                bd.Win_consecutivo = 0
                b = bd.Win + bd.Branco
                if(bd.Win + bd.Branco + bd.Loss)!=0:
                    a=100/(bd.Win + bd.Branco + bd.Loss)*b
                else:
                    a=0
                bd.Win_hat = (f'{a:,.2f}%')
            

                print("Win", bd.Win)
                print("Loss", bd.Loss)
                print("Branco", bd.Branco)
                print("Porcentagem", bd.Win_hat)

            reset()
            return

        if num[0:1] > [0] and num[0:1] <= [7] and bd.direction_color == '⚫':
            if bd.gale_atual == 0:
                bd.gale_atual += 1
                print('VAMOS PRO GALE 1º 🐓')
                doubleBet = bot.Bet(game="double", bets=[betBlack_g1, betWhite_g1],
                return_results=True)

                print('Cores Apostado no Martingale 1º:',doubleBet)
                

                return

            if bd.gale_atual == 1:
                bd.gale_atual += 1
                print('VAMOS PRO GALE 2º 🐓')
                doubleBet = bot.Bet(game="double", bets=[betBlack_g2, betWhite_g2],
                return_results=True)

                print('Cores Apostado no Martingale 2º:',doubleBet)
                

                return

            if bd.gale_atual == 2:
                print('LOSS❌')

                bd.Loss += 1
                bd.Win_consecutivo = 0
                b = bd.Win + bd.Branco
                if(bd.Win + bd.Branco + bd.Loss)!=0:
                    a=100/(bd.Win + bd.Branco + bd.Loss)*b
                else:
                    a=0
                bd.Win_hat = (f'{a:,.2f}%')


                print("Win", bd.Win)
                print("Loss", bd.Loss)
                print("Branco", bd.Branco)
                print("Porcentagem", bd.Win_hat)

            reset()
            return
        
    
    
        
    very_gale(bd.finalnum)

    return
    

while True:

    try:
        # Acessa a API e Pega os Dados
        pegar_dados = requests.get('https://blaze.com/api/roulette_games/recent')
        result = json.loads(pegar_dados.content)
        time.sleep(1)
        bd.analisar_open = 1
    except NameError as erro:
        continue
    except Exception as erro:
        continue

    # Verifica se Atualizou a Ultima Rodada
    ids = [x['id'] for x in result]

    if bd.id_antigo != ids[0]:
    
        bd.id_antigo = ids[0]

        bd.finalcor.clear()
        bd.final_cor.clear()
        
        
        # Seleciona Somente os Numeros que sairam
        dados_bruto = [x['roll'] for x in result]

        #Cria um Lista de Cores
        dados_color = [x['color'] for x in result]
        color_final = dados_color[:-1]
        
        nome_color = [x['color'] for x in result]
        nome_cor = nome_color[:-1]

        # finalcor = []
        for num in range(len(color_final)):
            if color_final[num] == 1:
                bd.final_cor.append('🔴')
            if color_final[num] == 2:
                bd.final_cor.append('⚫')
            if color_final[num] == 0:
                bd.final_cor.append('⚪')

        for num in range(len(nome_cor)):
            if nome_cor[num] == 1:
                bd.finalcor.append('V')
            if nome_cor[num] == 2:
                bd.finalcor.append('P')
            if nome_cor[num] == 0:
                bd.finalcor.append('B')



        if bd.analisar_open == 1:

            bd.finalnum = dados_bruto

        print(bd.finalnum[0:8])  # Vê os dois Últimos Números Jogados
        print(bd.finalcor[0:8])  # Vê as duas Últimas Cores da Jogadas
        print(bd.final_cor[0:8]) # Qual foi a ultimna cor


        
        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'E1':
            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:3] == ['V', 'V', 'P']:
                        print('🎯 ENTRADA ENVIADA ✅', str(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))
                        print('👨‍💻 ENTRADA NO: ⚫')
                        bd.estrategy_name = 'E1'
                        bd.direction_color = '⚫'
                        bd.analisar = 1
                        doubleBet = bot.Bet(game="double", bets=[betBlack, betWhite],
                        return_results=True)

                        print('Cores Apostado:',doubleBet)

                        return
                    if num[0:3] == ['P', 'P', 'V']:
                        print('🎯 ENTRADA ENVIADA ✅', str(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))
                        print('👨‍💻 ENTRADA NO: 🔴')
                        bd.estrategy_name = 'E1'
                        bd.direction_color = '🔴'
                        bd.analisar = 1
                        doubleBet = bot.Bet(game="double", bets=[betRed, betWhite],
                        return_results=True)

                        print('Cores Apostado:',doubleBet)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'E2':

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:3] == ['P', 'V', 'P']:
                        print('🎯 ENTRADA ENVIADA ✅', str(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))
                        print('👨‍💻 ENTRADA NO: ⚫')
                        bd.estrategy_name = 'E2'
                        bd.direction_color = '⚫'
                        bd.analisar = 1
                        doubleBet = bot.Bet(game="double", bets=[betBlack, betWhite],
                        return_results=True)

                        print('Cores Apostado:', doubleBet)
                        
                        return
                    if num[0:3] == ['V', 'P', 'V']: 
                        print('🎯 ENTRADA ENVIADA ✅', str(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))
                        print('👨‍💻 ENTRADA NO: 🔴')
                        bd.estrategy_name = 'E2'
                        bd.direction_color = '🔴'
                        bd.analisar = 1
                        doubleBet = bot.Bet(game="double", bets=[betRed, betWhite],
                        return_results=True)

                        print('Cores Apostado:', doubleBet)
                    
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'E3':

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:6] == ['V', 'V', 'V', 'V', 'V', 'P']:
                        print('🎯 ENTRADA ENVIADA ✅', str(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))
                        print('👨‍💻 ENTRADA NO: ⚫')
                        bd.estrategy_name = 'E3'
                        bd.direction_color = '⚫'
                        bd.analisar = 1
                        doubleBet = bot.Bet(game="double", bets=[betBlack, betWhite],
                        return_results=True)

                        print('Cores Apostado:',doubleBet)
                        
                        return
                    if num[0:6] == ['P', 'P', 'P', 'P', 'P', 'V']:
                        print('🎯 ENTRADA ENVIADA ✅', str(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))
                        print('👨‍💻 ENTRADA NO: 🔴')
                        bd.estrategy_name = 'E3'
                        bd.direction_color = '🔴'
                        bd.analisar = 1
                        doubleBet = bot.Bet(game="double", bets=[betRed, betWhite],
                        return_results=True)

                        print('Cores Apostado:',doubleBet)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            CHECK_VERSION(bd.finalcor)
        