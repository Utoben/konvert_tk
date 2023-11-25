from tkinter import *
from tkinter import ttk
import requests
from config import *

# Этого кода еще нет - допиши в верхнюю часть
uah = 'UAH'
rub = 'RUB'
eur = 'EUR'
usd = 'USD'

# отправялем GET запрос на сервер и обрабатываем его ответ, извлекаем результат
def get_konvert(currency_to, currency_from, amount):

	url = f"https://api.apilayer.com/currency_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

	headers= {
  		"apikey": API_KEY,
	}

	response=requests.get(url, headers=headers)
	if response.status_code == 200:
		result_json = response.json()
		result=result_json.get("result")
		res=round(result,3)
		print(f'Результат конвертации: {res}')
		return res
	else:
		print(f'Проблема: {response.status_code}')
		return 0

def konvert():
	val2.delete(0, END)
	a=float( val1.get() ) #получаем значение из поля1 
	b=com.get() #первый комбобокс
	d=com2.get() #второй комбобокс

		
	if b=='EUR' and d!='EUR': # если конвертим из EUR
		if d=='USD': result = get_konvert(usd, eur, a)
		if d=='UAN': result = get_konvert(uah, eur, a)
		if d=='RUB': result = get_konvert(rub, eur, a)
	# сюда поставить else: окно Ошибка

	if b=='USD' and d!='USD': # если конвертим из USD
		if d=='EUR': result = get_konvert(eur, usd, a)
		if d=='UAN': result = get_konvert(uah, usd, a)
		if d=='RUB': result = get_konvert(rub, usd, a)
		
	if b=='UAN' and d!='UAN': # если конвертим из UAN
		if d=='USD': result = get_konvert(usd, uah, a)
		if d=='EUR': result = get_konvert(eur, uah, a)
		if d=='RUB': result = get_konvert(rub, uah, a)

	if b=='RUB' and d!='RUB': # если конвертим из RUB
		if d=='USD': result = get_konvert(usd, rub, a)
		if d=='EUR': result = get_konvert(eur, rub, a)
		if d=='UAN': result = get_konvert(uah, rub, a)

	val2.insert(0 , result) #выводим результат в поле 2

# остальной код создания окна - он уже у тебя есть
def center(win):
	win.update_idletasks()
	width = win.winfo_width()
	height = win.winfo_height()
	x = (win.winfo_screenwidth() // 2) - (width // 2)
	y = (win.winfo_screenheight() // 2) - (height // 2)
	win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window = Tk() #создание окна
window.title('Konvert') #изменяем заголовок
window.geometry('500x300')
center(window)
window.resizable(False, False)

VAL=['USD','EUR','UAN' ,'RUB'] #список валют

Label(window, text='Конвертор валют' , font='Times 30').pack()
Label(window, text='Сумма:',   font='Times 15').place(x=120, y=84)
Label(window, text='Конвертировать в:', font='Times 15').place(x=120, y=150)
Label(window, text='Результат :', font='Times 15').place(x=120, y=200)
Button(window , text='Провести конверт', padx='20', pady='8', bg='#32a893', command=konvert).place(x=200 , y = 250)
#комбобокс 1
com=ttk.Combobox(window, width=10, values=VAL , font='20' ,state='readonly')
com.current(0)
com.place(x=300, y =88)
#поле для ввода 1
val1=Entry(window, width=10)
val1.place(x=200 , y=90)
#комбобокс 2
com2=ttk.Combobox(window, width=10, values=VAL , font='20' ,state='readonly')
com2.current(0)
com2.place(x=300, y =150)
#поле для ввода 2
val2=Entry(window, width=10)
val2.place(x=230 , y=204)
window.mainloop() #отобразить окно
