import os, sys
import PySimpleGUI as sg
import pyfiglet
import time
sg.theme('DarkPurple6')
def slp(n):
	time.sleep(n)
def empt():
	print(" ")
def fig(text):
	ar = pyfiglet.figlet_format(text)
	print(ar)
def figfont(text , font2):
	result = pyfiglet.figlet_format(text, font = font2 )
	print(result)
figfont("This is Output window.", "slant")
slp(3)
fig("Welcome to ")
slp(1)
fig("FigletMancy")
slp(1)
figfont(" - or - ", "rounded")
slp(1)
fig("ASCII-crafter")

def win2():
	layout = [[sg.Text('Wait what ?', font='Arial', text_color='white', size=(10,1))],      
	             [sg.Text('Enter your text here >>'), sg.InputText('', size=(17, 1), key='input2')],
	             [sg.Text('Enter your font here >>'), sg.InputText('', size=(17, 1), key='font')],       
	             [sg.Button('Send', key='submit'), sg.Button('Close', key='close'), sg.Button(' (͡° ͜ʖ ͡°) ', key='fnt21'), sg.Text('Author >>'), sg.Button('¯\_(ツ)_/¯', key='athur')]]      
	window = sg.Window('R E W O R K E D', layout)
	while True:
	   event, values = window.read()
	   if event == sg.WIN_CLOSED or event == 'close': # if user closes window or clicks cancel
	       window.close()
	   if event == 'fnt21':
	   	print(pyfiglet.FigletFont.getFonts())
	   	sg.popup('''This button print all fonts. Look to the output window !
Вывод Фиглет шрифтов в .txt невозможен в этой программе!
Кириллица поддерживается только с шрифтом banner !''')
	   a1 = values["font"]
	   a2 = values["input2"]
	   if event == "athur":
	   	sg.popup('''Hiii! My GitHub - github.com/CodelessHeart
Discord - LegitGirl#0131''')
	   if event == "submit":
	   	if a1 == "":
	   	    fig(a2)
	   	else:
	   	 try:
	   	     figfont(a2, a1)
	   	 except (pyfiglet.FontNotFound):
	   	      print("Error , font not found.")
try:
	win2()
except TypeError:
	raise SystemExit
