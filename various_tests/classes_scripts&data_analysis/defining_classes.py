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


# class Car:
#     def __init__(self, make, model, year, color):
#         self.make = make           # Manufacturer of the car
#         self.model = model         # Model of the car
#         self.year = year           # Year of manufacture
#         self.color = color         # Color of the car
#         self.running = False       # Tracks whether the car is running (initially off)

#     # Method to display car details
#     def display_info(self):
#         print(f"Car Information:\n Make: {self.make}\n Model: {self.model}\n Year: {self.year}\n Color: {self.color}")

#     # Method to start the car
#     def start(self):
#         if not self.running:
#             self.running = True
#             print(f"The {self.make} {self.model} has started.")
#         else:
#             print(f"The {self.make} {self.model} is already running.")

#     # Method to stop the car
#     def stop(self):
#         if self.running:
#             self.running = False
#             print(f"The {self.make} {self.model} has stopped.")
#         else:
#             print(f"The {self.make} {self.model} is already stopped.")
            
#     def get_info(self):
#         return f"This car is a {self.make}, and it is {'running' if self.running else 'stopped'}."


# civic_car = Car("Honda", "Civic", 2019, "Red")

# print(civic_car)

# civic_car.start()
# civic_car.start()

# civic_car.start()

# civic_car.stop()
# civic_car.stop()

# civic_car.get_info()

import time

class Car:
    def __init__(self, make, model, year, color):
        self.make = make           # Manufacturer of the car
        self.model = model         # Model of the car
        self.year = year           # Year of manufacture
        self.color = color         # Color of the car
        self.is_running = False    # Tracks if the car is running (initially off)
        self.speed = 0             # Tracks the current speed of the car (initially 0)

    # Method to display car details
    def display_info(self):
        print(f"Car Information:\n Make: {self.make}\n Model: {self.model}\n Year: {self.year}\n Color: {self.color}\n Speed: {self.speed} km/h")

    # Method to start the car
    def start(self):
        if not self.is_running:
            print(f"Starting the {self.color} {self.year} {self.make} {self.model}")
            time.sleep(1)
            self.is_running = True
            print(f"The {self.color} {self.year} {self.make} {self.model} has started.")
        else:
            print(f"The {self.color} {self.year} {self.make} {self.model} is already running.")

    # Method to stop the car
    def stop(self):
        if self.is_running:
            print(f"Stopping the {self.color} {self.year} {self.make} {self.model}")
            self.is_running = False
            self.speed = 0
            print(f"The {self.make} {self.model} has stopped.")
        else:
            print(f"The {self.make} {self.model} is already stopped.")

    # Method to accelerate the car
    def accelerate(self, increase):
        if self.is_running:
            self.speed += increase
            print(f"The {self.make} {self.model} accelerates by {increase} km/h. Current speed: {self.speed} km/h.")
        else:
            print(f"Cannot accelerate. The {self.make} {self.model} is not running.")

    # Method to apply brakes and reduce speed
    def brake(self, decrease):
        if self.is_running:
            self.speed -= decrease
            if self.speed <= 0:
                self.speed = 0
                self.stop()
                print(f"The {self.make} {self.model} has come to a stop.")
            else:
                print(f"The {self.make} {self.model} decelerates by {decrease} km/h. Current speed: {self.speed} km/h.")
        else:
            print(f"Cannot brake. The {self.make} {self.model} is not running.")
            
tesla_car = Car("Tesla", "Model 3", 2021, "Black")
tesla_car.start()
tesla_car.accelerate(62)

tesla_car.accelerate(20)
tesla_car.accelerate(12.5)

tesla_car.brake(30)

tesla_car.brake(300)

tesla_car.accelerate(20)

tesla_car.start()


# # Example usage
# my_car = Car("Toyota", "Corolla", 2022, "Blue")
# my_car.display_info()    # Show car details

# my_car.start()           # Start the car
# my_car.accelerate(20)    # Accelerate the car by 20 km/h
# my_car.accelerate(15)    # Accelerate the car by 15 km/h
# my_car.brake(10)         # Decelerate the car by 10 km/h
# my_car.brake(30)         # Decelerate the car by 30 km/h, which should stop the car







