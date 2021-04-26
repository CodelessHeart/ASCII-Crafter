import time
import pyfiglet
def menu():
	fig("ASCII - Crafter")
	empt()
	print("Выберите нужный пункт")
	print("1. Вывести текст без шрифта (стандарт юникод)")
	print("2. Вывести текст с кастомным шрифтом.")
	print("3. Информация.")
	print("0. Выxод.")
	empt()
	choose = input("ASCII-CRAFTER > ")
	if choose == "1":
		craft()
	if choose == "2":
		craftfont()
	if choose == "3":
		info()
	if choose == "4":
		print("Выxодим...")
		time.sleep(1)
		raise SystemExit
def info():
	empt()
	print("Привет! Эта программа созданна для создания ASCII текста!")
	print("Всё просто! В будующиx обноваx будет сейв в .txt файл.")
	print("Автор github.com/CodelessHeart , за предложениями - в мой телеграмм.")
	print("Telegram - @InfinityALT")
	empt()
def empt():
	print(" ")
def fig(text):
	ar = pyfiglet.figlet_format(text)
	print(ar)
def figfont(text , font2):
	result = pyfiglet.figlet_format(text, font = font2 )
	print(result)
def craft():
	text2 = input("Текст для вывода: ")
	fig(text2)
	time.sleep(5)
def craftfont():
	text2 = input("Текст для вывода: ")
	fig(text2)
	time.sleep(1)
	fonter = input("Фонт какой? : ")
	if fonter == "Никакой":
		print("Слыш б**, я ща тебя на вертель накручу, и в шаурму закатаю, шрифт ты никакой бл*.")
		time.sleep(5)
		raise SystemExit
	if fonter == "Украина":
		print("СЛАВА УКРАИНЕ! ГЕРОЯМ СЛАВА!")
		time.sleep(5)
		raise SystemExit
	if fonter == "Зайцев Кирилл":
		print("ДА ПРИКИНЬ ЭТУ ПРОГУ НАПИСАЛ Я!")
		time.sleep(5)
		raise SystemExit
	figfont(text2 , fonter)
menu()
