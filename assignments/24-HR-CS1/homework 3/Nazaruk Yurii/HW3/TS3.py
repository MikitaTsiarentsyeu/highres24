import json

with open("assignments/24-HR-CS1/homework 3/Nazaruk Yurii/HW3/time_descriptions.json", "r", encoding="utf-8") as file:
    data = json.load(file)
while True:
    time = input("Введите время в формате ЧЧ:ММ: ")
    if time in data:
        print( data[time])
        break
    else:
        print("Время введено неправильно, повторите попытку")
        