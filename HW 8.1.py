str = "Python Programming" #задаем переменную
print(str)
print(f"Длина строки: {len (str) }") #находим длину строки с помощью len

seventh_symbol = str [7] #находим седьмой символ
print(seventh_symbol)

last_symbol = str [-1] #ищем символы с конца
second_last_symbol = str [-2]
third_last_symbol = str [-3]
print(last_symbol)
print(second_last_symbol)
print(third_last_symbol)

result = "gram" in str #используем in чтобы найти нужную нам часть слова
print(result)
