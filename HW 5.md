Бизнес-процесс - Оформление премиум-подписок. анализ премиум-подписок напрямую влияет на финансовые результаты компании. Поэтому решил выбрать этот бизнес-процесс.
Grain - Одна активная премиум-подписка на сервис в конкретный момент времени
Dimension Tables - dim_user (информация о пользователе), dim_subscriptrion_type (описывает тип подписки), dim_date (дата, в которую отслеживается статус подписки), dim_status (статус подписки)
fact table - fact_subscription_daily_check (хранит ежедневные значения состояния каждой подписки. Каждая запись показывает, был ли пользователь подписан в конкретный день и сколько денег приносила его подписка за этот день.)
Star: fact_subscription_daily_check = dim_user + dim_subscriptrion_type + dim_date + dim_status (Выбрал для простоты и производительности)
Метрики: revenue_daily (дневная выручка), is_active (активна или нет)
Атрибуты (FK): user_sk, subscription_type_sk, status_sk, date_sk


-- 1. Создание таблицы измерений dim_user
CREATE TABLE dim_user (
    user_sk INT PRIMARY KEY,
    user_source_id VARCHAR(255) NOT NULL,
    country_code CHAR(2),
    age_group VARCHAR(20),
    registration_date DATE
);

-- 2. Создание таблицы измерений dim_subscription_type
CREATE TABLE dim_subscription_type (
    subscription_type_sk INT PRIMARY KEY,
    subscription_name VARCHAR(100) NOT NULL UNIQUE,
    price_per_month DECIMAL(10, 2) NOT NULL
);

-- 3. Создание таблицы измерений dim_status
CREATE TABLE dim_status (
    status_sk INT PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE
);

-- 4. Создание таблицы измерений dim_date
CREATE TABLE dim_date (
    date_sk INT PRIMARY KEY,
    calendar_date DATE NOT NULL UNIQUE,
    month INT NOT NULL,
    year INT NOT NULL
);

-- 5. Создание таблицы фактов fact_subscription_daily_check
CREATE TABLE fact_subscription_daily_check (
    check_sk INT PRIMARY KEY,
    user_sk INT,
    subscription_type_sk INT,  -- Изменено с subscription_sk
    status_sk INT,
    date_sk INT,
    revenue_daily DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN NOT NULL,
    
    CONSTRAINT fk_user FOREIGN KEY (user_sk) 
        REFERENCES dim_user(user_sk),
    CONSTRAINT fk_subscription_type FOREIGN KEY (subscription_type_sk) 
        REFERENCES dim_subscription_type(subscription_type_sk),
    CONSTRAINT fk_status FOREIGN KEY (status_sk) 
        REFERENCES dim_status(status_sk),
    CONSTRAINT fk_date FOREIGN KEY (date_sk) 
        REFERENCES dim_date(date_sk)
);

-- 1. Заполняем таблицу пользователей (dim_user)
INSERT INTO dim_user (user_sk, user_source_id, country_code, age_group, registration_date) VALUES
(1, 'user_001', 'RU', '25-34', '2023-01-15'),
(2, 'user_002', 'US', '18-24', '2023-02-20'),
(3, 'user_003', 'KZ', '35-44', '2023-03-10'),
(4, 'user_004', 'RU', '25-34', '2023-04-05'),
(5, 'user_005', 'US', '45+', '2023-05-12');

-- 2. Заполняем таблицу типов подписки (dim_subscription_type)
INSERT INTO dim_subscription_type (subscription_type_sk, subscription_name, price_per_month) VALUES
(1, 'Индивидуальный', 299.00),
(2, 'Семейный', 499.00),
(3, 'Студенческий', 149.00);

-- 3. Заполняем таблицу статусов (dim_status)
INSERT INTO dim_status (status_sk, status_name) VALUES
(1, 'Active'),
(2, 'Cancelled'),
(3, 'Trial');

-- 4. Заполняем таблицу дат (dim_date) - данные за октябрь 2023
INSERT INTO dim_date (date_sk, calendar_date, month, year) VALUES
(20231001, '2023-10-01', 10, 2023),
(20231002, '2023-10-02', 10, 2023),
(20231003, '2023-10-03', 10, 2023),
(20231004, '2023-10-04', 10, 2023),
(20231005, '2023-10-05', 10, 2023),
(20231006, '2023-10-06', 10, 2023),
(20231007, '2023-10-07', 10, 2023),
(20231008, '2023-10-08', 10, 2023),
(20231009, '2023-10-09', 10, 2023),
(20231010, '2023-10-10', 10, 2023);

-- 5. Заполняем таблицу фактов (fact_subscription_daily_check)
-- Данные за 10 дней для 5 пользователей
INSERT INTO fact_subscription_daily_check (check_sk, user_sk, subscription_type_sk, status_sk, date_sk, revenue_daily, is_active) VALUES
-- День 1:
(1, 1, 1, 1, 20231001, 9.97, true),
(2, 2, 2, 1, 20231001, 16.63, true),
(3, 3, 3, 1, 20231001, 4.97, true),
(4, 4, 1, 1, 20231001, 9.97, true),
(5, 5, 2, 1, 20231001, 16.63, true),

-- День 2: Пользователь 3 отменил подписку
(6, 1, 1, 1, 20231002, 9.97, true),
(7, 2, 2, 1, 20231002, 16.63, true),
(8, 3, 3, 2, 20231002, 0.00, false),  -- Cancelled
(9, 4, 1, 1, 20231002, 9.97, true),
(10, 5, 2, 1, 20231002, 16.63, true),

-- День 3: Пользователь 5 перешел на trial
(11, 1, 1, 1, 20231003, 9.97, true),
(12, 2, 2, 1, 20231003, 16.63, true),
(13, 3, 3, 2, 20231003, 0.00, false),
(14, 4, 1, 1, 20231003, 9.97, true),
(15, 5, 2, 3, 20231003, 0.00, false),  -- Trial

-- День 4: Пользователь 2 отменил подписку
(16, 1, 1, 1, 20231004, 9.97, true),
(17, 2, 2, 2, 20231004, 0.00, false),  -- Cancelled
(18, 3, 3, 2, 20231004, 0.00, false),
(19, 4, 1, 1, 20231004, 9.97, true),
(20, 5, 2, 3, 20231004, 0.00, false),

-- День 5: Новый пользователь 3 активировал подписку снова
(21, 1, 1, 1, 20231005, 9.97, true),
(22, 2, 2, 2, 20231005, 0.00, false),
(23, 3, 1, 1, 20231005, 9.97, true), 
(24, 4, 1, 1, 20231005, 9.97, true),
(25, 5, 2, 3, 20231005, 0.00, false),

-- День 6: Стабильная ситуация
(26, 1, 1, 1, 20231006, 9.97, true),
(27, 2, 2, 2, 20231006, 0.00, false),
(28, 3, 1, 1, 20231006, 9.97, true),
(29, 4, 1, 1, 20231006, 9.97, true),
(30, 5, 2, 3, 20231006, 0.00, false),

-- День 7: Пользователь 5 активировал платную подписку
(31, 1, 1, 1, 20231007, 9.97, true),
(32, 2, 2, 2, 20231007, 0.00, false),
(33, 3, 1, 1, 20231007, 9.97, true),
(34, 4, 1, 1, 20231007, 9.97, true),
(35, 5, 2, 1, 20231007, 16.63, true),  -- Снова активен

-- День 8: Все стабильно
(36, 1, 1, 1, 20231008, 9.97, true),
(37, 2, 2, 2, 20231008, 0.00, false),
(38, 3, 1, 1, 20231008, 9.97, true),
(39, 4, 1, 1, 20231008, 9.97, true),
(40, 5, 2, 1, 20231008, 16.63, true),

-- День 9: Пользователь 4 перешел на семейный тариф
(41, 1, 1, 1, 20231009, 9.97, true),
(42, 2, 2, 2, 20231009, 0.00, false),
(43, 3, 1, 1, 20231009, 9.97, true),
(44, 4, 2, 1, 20231009, 16.63, true),  -- Сменил тариф
(45, 5, 2, 1, 20231009, 16.63, true),

-- День 10: Финальный день наблюдений
(46, 1, 1, 1, 20231010, 9.97, true),
(47, 2, 2, 2, 20231010, 0.00, false),
(48, 3, 1, 1, 20231010, 9.97, true),
(49, 4, 2, 1, 20231010, 16.63, true),
(50, 5, 2, 1, 20231010, 16.63, true);

1) -- Найдем динамику выручки по дням
SELECT 
    d.calendar_date,           -- Дата из таблицы измерений dim_date
    SUM(f.revenue_daily) AS total_revenue  -- Суммарная выручка всех пользователей в этот день
FROM fact_subscription_daily_check f
JOIN dim_date d 
    ON f.date_sk = d.date_sk   -- Соединяем факт и дату по surrogate key
GROUP BY d.calendar_date      -- Группируем по дате
ORDER BY d.calendar_date;     -- Сортируем по возрастанию даты

2) -- Анализ популярности тарифных планов
SELECT 
    s.subscription_name,        -- Название тарифа
    COUNT(DISTINCT f.user_sk) AS num_users  -- Считаем уникальных пользователей
FROM fact_subscription_daily_check f
JOIN dim_subscription_type s 
    ON f.subscription_type_sk = s.subscription_type_sk  -- Соединяем с таблицей тарифов
WHERE f.is_active = TRUE       -- Только активные подписки
GROUP BY s.subscription_name   -- Группируем по тарифу
ORDER BY num_users DESC;       -- Сортируем по популярности (от большего к меньшему)

3) -- Анализ оттока пользователей
SELECT 
    d.calendar_date,           -- Дата
    COUNT(*) AS churned_users  -- Количество пользователей, которые стали неактивными
FROM fact_subscription_daily_check f
JOIN dim_date d 
    ON f.date_sk = d.date_sk
WHERE f.is_active = FALSE     -- Только пользователи, которые неактивны
GROUP BY d.calendar_date       -- Группируем по дате
ORDER BY d.calendar_date;      -- Сортировка по дате



4) -- Суммарная выручка по тарифным планам
SELECT 
    s.subscription_name,        -- Название тарифа
    SUM(f.revenue_daily) AS total_revenue  -- Суммарная выручка
FROM fact_subscription_daily_check f
JOIN dim_subscription_type s 
    ON f.subscription_type_sk = s.subscription_type_sk  -- Соединяем с таблицей тарифов
GROUP BY s.subscription_name   -- Группируем по тарифу
ORDER BY total_revenue DESC;   -- Сортировка по доходу (от большего к меньшему)












