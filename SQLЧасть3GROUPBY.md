Часть 3: GROUP BY
Задача 1
Подсчитайте количество клиентов в каждой стране.
Пример ожидаемого результата:
country | count
--------|-------
USA | 4
UK | 3
UAE | 2
Задача 2
Посчитайте общее количество заказов и среднюю сумму по каждому товару.
Пример ожидаемого результата:
SQL
SQL
SQL
item | count | avg_amount
---------|-------|------------
Keyboard | 3 | 416.66
Mouse | 2 | 325.00


select country, count(customer_id) as count
from customers
group by country -- группировка результатов по странам
order by count desc; -- сортировка от большего к меньшему

select item, count(item) as count, avg(amount) as avg_amount -- находим общее количество товаров и среднюю сумму
from orders
group by item -- группируем по товарам
order by avg_amount desc; -- сортируем от самой высокой стоимости к низкой