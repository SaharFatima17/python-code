#TEMPERATURE CONVERTOR
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15


# --- Main Program ---
c = float(input("Enter temperature in Celsius: "))
temp = Temperature(c)

print("Fahrenheit:", temp.to_fahrenheit())
print("Kelvin:", temp.to_kelvin())



#E-COMMERENCE CART SYSTEM
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def item_total(self):
        return self.product.price * self.quantity


# --- Create Products ---
p1 = Product("Shirt", 500)
p2 = Product("Shoes", 1200)
p3 = Product("Watch", 800)

# --- Create Cart Items ---
c1 = CartItem(p1, 2)
c2 = CartItem(p2, 1)
c3 = CartItem(p3, 3)

# --- Calculate Total Bill ---
total_bill = c1.item_total() + c2.item_total() + c3.item_total()

print("Total Bill:", total_bill)
