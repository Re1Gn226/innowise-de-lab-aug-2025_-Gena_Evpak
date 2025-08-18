Часть 7 (Опционально)
Найдите клиентов, которые:
1. Сделали хотя бы 2 заказа (любых),
2. Имеют хотя бы одну доставку со статусом 'Delivered'.
Для каждого такого клиента выведите:
● full_name (имя + фамилия),
● общее количество заказов,
● общую сумму заказов,
● страну проживания.
Пример ожидаемого результата:
full_name | country | total_orders | total_amount
----------------|---------|--------------|--------------
Alice Smith | USA | 2 | 10450


select concat(first_name, ' ', last_name) as full_name, country, count(order_id) as total_orders, sum(amount) as total_amount -- полное имя клиента с помощью concat, 
from customers 
join orders on customers.customer_id = orders.customer_id 
join shippings on customers.customer_id = shippings.customer
where shippings.status = 'Delivered' -- отбирает только доставленные заказы
GROUP BY concat(first_name, ' ', last_name), customers.country
having count(orders.order_id) >= 2 -- клиенты, у которых больше двух заказов
order by total_amount desc; -- сортируем по сумме