Часть 6: WINDOW FUNCTIONS
Задача 1
Для каждого заказа добавьте колонку с суммой всех заказов этого клиента (используя
оконную функцию).
Пример ожидаемого результата:
order_id | customer_id | item | amount | total_by_customer
---------|-------------|----------|--------|-------------------
1 | 4 | Keyboard | 400 | 700
2 | 4 | Mouse | 300 | 700


select order_id, customer_id, item, amount, sum(amount) over(partition by customer_id) as total_by_customer  -- Оконная функция: сумма всех заказов по каждому клиенту
from orders
group by order_id
order by order_id asc;  -- Сортировка результатов по возрастанию

