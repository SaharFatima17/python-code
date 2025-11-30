class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")


# Example usage:
my_car = Car("Toyota", 120)
my_car.display_info()
