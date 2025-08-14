Часть 1: WHERE
Задача 1
Найдите всех клиентов из страны 'USA', которым больше 25 лет.
Пример ожидаемого результата:
first_name | last_name | age | country
-----------|-----------|-----|--------
John | Doe | 31 | USA
Alice | Smith | 35 | USA
Tom | White | 31 | USA
Задача 2
Выведите все заказы, у которых сумма (amount) больше 1000.
Пример ожидаемого результата:
order_id | item | amount | customer_id
---------|---------|--------|-------------
3 | Monitor | 12000 | 3
6 | Monitor | 10000 | 6
9 | Monitor | 11000 | 9


select first_name, last_name, age, country
from customers
where country = 'USA' and age > 25; -- выбираем клиентов из США возрастом старше 25 лет

SELECT * FROM orders
WHERE amount > 1000; -- находим те заказы, сумма которых превышает 1000