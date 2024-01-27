
def func(distance, min_price, base_price_km): #именуемые параметры
    print(distance, min_price, base_price_km)
    payment = (distance - 3) * min_price + base_price_km #формула вычисления
    return payment

distance = 20.5
min_price = 12
base_price_km = 100

print(func(distance, min_price, base_price_km))
