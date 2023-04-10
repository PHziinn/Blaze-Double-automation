import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
import time
import requests



class Bot:
    
    driver = None
    LOGIN_SUCCESS = None
    
    ACCOUNT_BALANCE = None
    BASE_URL = ""
    
    # Iniciar | Inicie a biblioteca Selenium, abra o navegador e carregue a página da web
    def Start(self):
        
        print('Automação em Funcionamento!')
        
        global BASE_URL
        BASE_URL = 'https://blaze.com/pt/games/double'
            
        global driver
        
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--window-size=1300,1000")
        
        chrome_options.add_argument("--log-level=3")
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36"
        chrome_options.add_argument(f"user-agent={user_agent}")
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_position(500, 0, windowHandle="current")
        driver.get(BASE_URL)
        
        print("Automação iniciado")
    
    # Parar | Feche todas as instâncias e processos do Selenium
    def Stop(self):
        
        print("A Automação está parando")
        driver.quit()
        print("Automação parado")
    
    # Login
    def Login(self, email, password):
        
        error = None
        global LOGIN_SUCCESS


        try:
            wait = WebDriverWait(driver, 10)
            wait_0 = WebDriverWait(driver, timeout=1200, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
            LOGIN_BUTTON = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div/div[2]/div/div/div[1]/a')))
            LOGIN_BUTTON.click()
            
            time.sleep(2)
            EMAIL_INPUT = driver.find_elements(By.CLASS_NAME, 'input-wrapper')[0].find_element(By.TAG_NAME, 'input')
            EMAIL_INPUT.send_keys(email)
            
            PASSWORD_INPUT = driver.find_elements(By.CLASS_NAME, 'input-wrapper')[1].find_element(By.TAG_NAME, 'input')
            PASSWORD_INPUT.send_keys(password)
            
            SUBMIT_BUTTON = driver.find_element(By.CLASS_NAME, 'submit')
            SUBMIT_BUTTON.click()
            time.sleep(1.2)
            # Você tem que resolver o captcha para continuar 
            wait_0.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#header > div.right > div > div.routes > div > div.icons > div:nth-child(2) > div")))
            time.sleep(1.2)
                
            LOGIN_SUCCESS = True
            
        except Exception as e:
            error = [False, e]
        finally:
            if error:
                print("Error", error)
                LOGIN_SUCCESS = False
                return error
            else:
                print("Login successful")
                Bot.Get_Balance(self)
                return [LOGIN_SUCCESS, None]
    

    # Balance
    def Get_Balance(self):
        
        error = None
        result = None
        
        global ACCOUNT_BALANCE
        
        try:
            balance_description = driver.find_element(By.CLASS_NAME, 'description').get_attribute("textContent")
            
            currency = None
            symbol = None
            
            if "R$" in balance_description:
                currency = "BRL"
                symbol = "R$"
            elif "$" in balance_description:
                currency = "USD"
                symbol = "$"
            elif "€" in balance_description:
                currency = "EUR"
                symbol = "€"
            
            balance = balance_description.split("(")[1].replace(")", "").replace(symbol, "")
            real = float(balance.split("+")[0].strip())
            bonus = float(balance.split("+")[1].strip().split(" ")[0])
            
            result = [real, bonus, currency]
            print("Valor em Real:", real, "Valor de Bônus:", bonus, "Moeda Convertida:", currency)
        except:
            error = False
            print("Algo deu errado")
            return error
        finally:
            if error == None:
                ACCOUNT_BALANCE = result
                return result
    
    
    # Double

    def Bet(self, game, bets, return_results):
        global driver
        global BASE_URL
        

        if game == "double":
            BASE_URL = 'https://blaze.com/pt/games/double'
            driver.get(BASE_URL)
            return self.BetDouble(bets, return_results)
    
    def BetDouble(self, bets, return_results):
        
        total_bet = 0
        
        # Verifique se as apostas estão bem formatadas e se o saldo é suficiente
        for bet in bets:
            if len(bet) < 2 or isinstance(bet['color'], str) == False:
                print("Formatação incorreto", "Tamanhos")
                return False
            
            if bet['color'].lower() == "white" or bet['color'].lower() == "black" or bet['color'].lower() == "red":
                pass
            else:
                print("Formatação incorreta", "Nome de cor incorreto")
                return False
            
            if bet['amount'] * 1 > 0:
                total_bet += bet['amount']
            else:
                print("Formatação incorreta", "Valor errado")
                return False
            
        if total_bet > ACCOUNT_BALANCE[0]:
            print("Você não tem saldo suficiente")
            return False
        
        # Aguarde a próxima janela de aposta
        current_status = None
        while current_status != "waiting":
            current_status = requests.get('https://blaze.com/api/roulette_games/current')
            if current_status.status_code == 200:
                    current_status = current_status.json()['status']
            time.sleep(1)
        
        # Obtenha a referência de entrada e botões
        
        INPUT_AMOUNT = driver.find_element(By.XPATH, '//*[@id="roulette-controller"]/div[1]/div[2]/div[1]/div/div[1]/input')
        RED_BUTTON = driver.find_element(By.XPATH, '//*[@id="roulette-controller"]/div[1]/div[2]/div[2]/div/div[1]')
        BLACK_BUTTON = driver.find_element(By.XPATH, '//*[@id="roulette-controller"]/div[1]/div[2]/div[2]/div/div[3]')
        WHITE_BUTTON = driver.find_element(By.XPATH, '//*[@id="roulette-controller"]/div[1]/div[2]/div[2]/div/div[2]')
        BET_BUTTON = driver.find_element(By.XPATH, '//*[@id="roulette-controller"]/div[1]/div[3]/button')
        
        # Realizar aposta
        for bet in bets:
            
            INPUT_AMOUNT.clear()
            INPUT_AMOUNT.send_keys(str(bet['amount']))
            
            time.sleep(0.2)
            if bet['color'].lower() == "red":
                RED_BUTTON.click()
            elif bet['color'].lower() == "black":
                BLACK_BUTTON.click()
            elif bet['color'].lower() == "white":
                WHITE_BUTTON.click()
            
            time.sleep(0.2)
            BET_BUTTON.click()

            
            print('Botão Para Aposta:', bet)
        
        # Confira os resultados
        if return_results == True:
            
            current_result = None
            current_status = None
            while current_status != "complete":
                result = requests.get('https://blaze.com/api/roulette_games/current')
                if result.status_code == 200:
                    current_status = result.json()['status']
                    current_result = result.json()
                time.sleep(1)
            
            result_color = None
            multiplier = None
            
            if current_result['color'] == 0:
                result_color = "white"
                multiplier = 14
            elif current_result['color'] == 1:
                result_color = "red"
                multiplier = 1
            elif current_result['color'] == 2:
                result_color = "black"
                multiplier = 1
            
            bet_results = []
            total_result = 0
            
            for bet in bets:
                result = None
                if bet['color'] == result_color:
                    result = bet['amount'] * multiplier
                else:
                    result = 0 - bet['amount']
                
                total_result += result
                bet_results.append({ "color": bet['color'], "amount": result})
                
            print([total_result, bet_results])
            print('Main: Total Results é Bet Results', total_bet,bet_results)
            return [total_result, bet_results]