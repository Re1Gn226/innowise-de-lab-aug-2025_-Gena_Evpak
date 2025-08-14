Часть 5: SUBQUERIES
Задача 1
Найдите всех клиентов, которые сделали заказ с максимальной суммой.
Пример ожидаемого результата:
first_name | last_name | amount
-----------|-----------|--------
David | Robinson | 12000


select first_name, last_name, amount
from customers inner join orders on customers.customer_id = orders.customer_id
where amount = (select max(amount) -- Подзапрос: находим максимальную сумму заказа
			from orders);