# Passo a passo do projeto - PowerUp

# 1. Abrir o sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
   # pyautogui - automatizar ações do teclado e mouse
      # pyautogui.click -> clicar com o mouse
      # pyautogui.write -> escrever um texto
      # pyautogui.press -> apertar uma tecla
      # pyautogui.hotkey -> combinação de teclas (ctrl C, ctrl V, etc)

import pyautogui
import time

pyautogui.PAUSE = 0.5 # Configura o tempo de espera entre os comandos

# abrir o navegador 
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# acessar o sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# 2. Fazer login
time.sleep(3)
# print(pyautogui.position()) # descobrir a posição do botão de login
pyautogui.click(x=1407, y=401)
pyautogui.write("leticia.rodrigues20021@gmail.com")
pyautogui.press("tab")

pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

# 3. Abrir/importar base de dados de produtos para cadastrar

time.sleep(3)
# pyautogui.click(x=1334, y=282)

import pandas as pd

tabela = pd.read_csv("produtos.csv") # Importar a base de dados

# 4. Cadastrar produtos
for linha in tabela.index: # index -> retorna a quantidade de linhas da tabela 
   pyautogui.click(x=1334, y=282)
   pyautogui.write(str(tabela.loc[linha, "codigo"])) # loc é de localizar
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "marca"]))
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "categoria"]))
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "custo"]))
   pyautogui.press("tab")

   if not pd.isna(tabela.loc[linha, "obs"]): 
      pyautogui.white(str(tabela.loc[linha, "obs"]))
   pyautogui.press("tab")
   pyautogui.press("enter")
   pyautogui.scroll(5000) # Rolar a tela para cima



# 5. Repetir isso tudo até acabar a lista de produtos