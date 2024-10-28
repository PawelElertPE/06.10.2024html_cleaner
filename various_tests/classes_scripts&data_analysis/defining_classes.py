# class Car:
#     pass

# car_1 = Car()

# car_2 = Car()

# print(car_1)
# print(car_2)

# print(type(car_1))
# print(type(car_2))

# car_1.make = "Honda"

# print(car_1.make)

# #print(car_2.make)

# car_2.model = "Civic"
# print(car_2.model)

# print(car_1.model)

# class Car:
#     # Constructor to initialize the properties
#     def __init__(self, make, model, year, color):
#         self.make = make       # Manufacturer of the car (e.g., 'Toyota')
#         self.model = model     # Model of the car (e.g., 'Corolla')
#         self.year = year       # Year of manufacture (e.g., 2022)
#         self.color = color     # Color of the car (e.g., 'Blue')
#         print(f"Car initialized {make}, {model}, {year}, {color} ")
        
# camry_car = Car("Toyota", "Camry", 2022, "Blue")
# civic_car = Car("Honda", "Civic", 2019, "Red")

# print(camry_car)
# print(civic_car)

# print(camry_car.make, camry_car.model, camry_car.year, camry_car.color)

# print(civic_car.make, civic_car.model, civic_car.year, civic_car.color)

# camry_car.self


class Car:
    def __init__(self, make, model, year, color):
        self.make = make           # Manufacturer of the car
        self.model = model         # Model of the car
        self.year = year           # Year of manufacture
        self.color = color         # Color of the car
        self.running = False       # Tracks whether the car is running (initially off)

    # Method to display car details
    def display_info(self):
        print(f"Car Information:\n Make: {self.make}\n Model: {self.model}\n Year: {self.year}\n Color: {self.color}")

    # Method to start the car
    def start(self):
        if not self.running:
            self.running = True
            print(f"The {self.make} {self.model} has started.")
        else:
            print(f"The {self.make} {self.model} is already running.")

    # Method to stop the car
    def stop(self):
        if self.running:
            self.running = False
            print(f"The {self.make} {self.model} has stopped.")
        else:
            print(f"The {self.make} {self.model} is already stopped.")
            
    def get_info(self):
        return f"This car is a {self.make}, and it is {'running' if self.is_running else 'stopped'}."




