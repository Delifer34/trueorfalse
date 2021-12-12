#библиотеки для работы приложения

import PySimpleGUI as sg
import random
import time

#Дизайн приложения

sg.theme('DarkGrey5')

layout = [
	[sg.Text("Задай свой вопрос: ", font="Arial, 11")],[sg.Input(key="Answeruser")],
	[sg.Button("Узнать ответ")],[sg.Text("Результат:", font="Arial, 15")],
	[sg.Text("Нет, это ложь!", key="lie", visible=False, font="Arial, 20")],
	[sg.Text("Да,это правда!", key="true", visible=False, font="Arial, 20")],
]

window = sg.Window("True Or False?", layout, icon=r'/logo.png', size=(290,400), finalize=True) #основное окно приложения

while True: #Закрывает программу
	event, values = window.read() 
	if event == sg.WIN_CLOSED: #завершает работу приложения
		break
	if event == 'Узнать ответ':
		answer = random.randint(0,1) # генерация ответа
		print("Кнопка работает") #Проверка кнопки
		if answer == 0:
			window["lie"].update(visible=True) #Программа сначала выводит текст который выпал затем обновляет экран и прячет текст
			window.Refresh()
			time.sleep(3)
			window["lie"].update(visible=False)
		elif answer == 1:
			window["true"].update(visible=True) #Программа сначала выводит текст который выпал затем обновляет экран и прячет текст
			window.Refresh()
			time.sleep(3)
			window["true"].update(visible=False)
#обновление экрана
		window.Refresh()

#закрытие окна приложения
window.close()
