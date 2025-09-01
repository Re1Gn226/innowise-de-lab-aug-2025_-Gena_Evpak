prices = [1000, 3499, 250]
nds = 0.20
def add_vat(prices): #объявляем функцию с параметром prices
    for price in prices: #вводим цикл
        a = price + price * nds #считаем сумму с ндс
        print(a)
add_vat(prices) #вызываем функцию