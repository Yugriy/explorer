import pandas as pd

class Product:
    def __init__(self, category, name, price, unit, manufacturer, sku):
        self.category = category
        self.name = name
        self.price = price
        self.unit = unit
        self.manufacturer = manufacturer
        self.sku = sku
        self.quantity = 0

class Inventory:
    def __init__(self):
        self.products = pd.DataFrame(columns=['Category', 'Name', 'Price', 'Unit', 'Manufacturer', 'SKU', 'Quantity'])

    def add_product(self, product):
        new_product = pd.DataFrame([[product.category, product.name, product.price, product.unit, product.manufacturer, product.sku, product.quantity]],
                                   columns=['Category', 'Name', 'Price', 'Unit', 'Manufacturer', 'SKU', 'Quantity'])
        self.products = self.products.append(new_product, ignore_index=True)

    def ship_product(self, sku, quantity):
        self.products.loc[self.products['SKU'] == sku, 'Quantity'] -= quantity

    def check_stock(self, sku):
        return self.products.loc[self.products['SKU'] == sku, 'Quantity'].values[0]

    def show_inventory(self):
        print(self.products)

    def search_product(self, keyword):
        result = self.products[self.products['Name'].str.contains(keyword, case=False)]
        print(result)

    def demand_chart(self):
        # реализация графика о востребованности товара
        pass

inventory = Inventory()

def menu():
    print("1. Add Product")
    print("2. Ship Product")
    print("3. Check Stock")
    print("4. Show Inventory")
    print("5. Search Product")
    print("6. Exit")
    choice = input("Enter choice: ")
    return choice

while True:
    choice = menu()
    if choice == '1':
        category = input("Enter category: ")
        name = input("Enter name: ")
        price = float(input("Enter price: "))
        unit = input("Enter unit: ")
        manufacturer = input("Enter manufacturer: ")
        sku = input("Enter SKU: ")
        product = Product(category, name, price, unit, manufacturer, sku)
        inventory.add_product(product)
    elif choice == '2':
        sku = input("Enter SKU: ")
        quantity = int(input("Enter quantity: "))
        inventory.ship_product(sku, quantity)
    elif choice == '3':
        sku = input("Enter SKU: ")
        print("Stock:", inventory.check_stock(sku))
    elif choice == '4':
        inventory.show_inventory()
    elif choice == '5':
        keyword = input("Enter keyword to search: ")
        inventory.search_product(keyword)
    elif choice == '6':
        break