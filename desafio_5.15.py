import pyautogui
import webbrowser
from time import sleep
import pyperclip
import os 

def escrever(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey("ctrl","v")

def bater_print_digite_seu_nome():
    pyautogui.scroll(-1000)
    sleep(1)
    pyautogui.screenshot("imagem.png",region=(1924,306,130,20))
    pyautogui.scroll(1000)
    sleep(1)

def bater_print_btn_alerta():
    pyautogui.scroll(-1000)
    sleep(1)
    pyautogui.screenshot("imagembtnalerta.png",region=(1928,344,50,20))
    pyautogui.scroll(1000)
    sleep(1)

def bater_print_exel():
    sleep(1)
    pyautogui.scroll(-1500)
    pyautogui.screenshot("imagemexel.png",region=(718,715,156,26))
    pyautogui.scroll(1500)
    sleep(1)

def bater_print_docx():
    sleep(1)
    pyautogui.scroll(-1500)
    pyautogui.screenshot("imagemdocx.png",region=(1099,714,155,25))
    pyautogui.scroll(1500)
    sleep(1)

def bater_print_alerta():
    sleep(1)
    pyautogui.screenshot("imagemalerta.png",region=(1432,180,35,20))

#abrir site
webbrowser.open("https://cursoautomacao.netlify.app/")
sleep(3)
#verificar se ha todos os prints se nao houver bater
imagem = os.path.exists("imagem.png")
if imagem == False:
    bater_print_digite_seu_nome()

imagem = os.path.exists("imagemdocx.png")
if imagem == False:
    bater_print_docx()

imagem = os.path.exists("imagemexel.png")
if imagem == False:
    bater_print_exel()

imagem = os.path.exists("imagembtnalerta.png")
if imagem == False:
    bater_print_btn_alerta()
# encontrar campo digite seu nome com o print
pyautogui.scroll(-1000)
sleep(1)
local = pyautogui.locateCenterOnScreen("imagem.png")
pyautogui.click(local[0],local[1],duration=1)
sleep(1)
#digitar meu nome
escrever("Marco Antônio") #ou
# pyautogui.typewrite("marco")

#clicar em alerta
local = pyautogui.locateCenterOnScreen("imagembtnalerta.png")
pyautogui.click(local[0],local[1],duration=1)
# fechar alerta
imagem = os.path.exists("imagemalerta.png")
if imagem == False:
    bater_print_alerta()

sleep(2)
local = pyautogui.locateCenterOnScreen("imagemalerta.png")
pyautogui.click(local[0],local[1],duration=1)

# subir pagina de volta
pyautogui.scroll(1000)
sleep(1)

#achar botoes de dowload com base na foto
pyautogui.scroll(-1500)
imagem_excel = pyautogui.locateCenterOnScreen("imagemexel.png")
pyautogui.moveTo(imagem_excel[0],imagem_excel[1],duration=1)
sleep(1)
pyautogui.move(0,30,duration=1)
sleep(1)
pyautogui.click()

imagem_docx = pyautogui.locateCenterOnScreen("imagemdocx.png")
pyautogui.moveTo(imagem_docx[0],imagem_docx[1],duration=1)
sleep(1)
pyautogui.move(0,30,duration=1)
sleep(1)
pyautogui.click()
# criar aleta dizendo vc terminou Marco Antônio
pyautogui.alert("terminou")