Задача 1
Выведите список клиентов, отсортированный по возрасту по убыванию.
Пример ожидаемого результата:
first_name | age
-----------|-----
Michael | 40
Alice | 35
John | 31




select first_name, age
from customers
order by age desc; -- отсортировываем клиентов по возрасту