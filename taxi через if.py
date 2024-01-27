def func(distance, min_price=100, base_price_km=12):
    if distance <= 3:
        return min_price
    else:
        return min_price + (distance - 3) * base_price_km

distance = 20.5
cost = func(distance)
print('Стоимость поездки:', cost, "руб.")
