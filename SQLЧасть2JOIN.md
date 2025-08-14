Часть 2: JOIN
Задача 1
Получите список заказов вместе с именем клиента, который сделал заказ.
SQL
SQL
SQL
Пример ожидаемого результата:
first_name | last_name | item | amount
-----------|-----------|----------|-------
John | Reinhardt | Keyboard | 400
John | Reinhardt | Mouse | 300
...
Задача 2
Выведите список доставок со статусом и именем клиента.
Пример ожидаемого результата:
status | first_name | last_name
----------|------------|-----------
Pending | Robert | Luna
Delivered | David | Robinson



SELECT first_name, last_name, item, amount
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id; -- получаем список заказов с именами клиентов, соеднияем таблицы

select status, first_name, last_name
from shippings inner join customers on shippings.customer = customers.customer_id; -- получаем список доставок со статусом и именем клиентов, соединяем таблицы shippings и customers по customer_id