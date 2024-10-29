# import time

# class Car:
#     def __init__(self, make, model, year, color):
#         self.make = make           # Manufacturer of the car
#         self.model = model         # Model of the car
#         self.year = year           # Year of manufacture
#         self.color = color         # Color of the car
#         self.is_running = False    # Tracks if the car is running (initially off)
#         self.speed = 0             # Tracks the current speed of the car (initially 0)

#     # Method to display car details
#     def display_info(self):
#         print(f"Car Information:\n Make: {self.make}\n Model: {self.model}\n Year: {self.year}\n Color: {self.color}\n Speed: {self.speed} km/h")

#     # Method to start the car
#     def start(self):
#         if not self.is_running:
#             print(f"Starting the {self.color} {self.year} {self.make} {self.model}")
#             time.sleep(1)
#             self.is_running = True
#             print(f"The {self.color} {self.year} {self.make} {self.model} has started.")
#         else:
#             print(f"The {self.color} {self.year} {self.make} {self.model} is already running.")

#     # Method to stop the car
#     def stop(self):
#         if self.is_running:
#             print(f"Stopping the {self.color} {self.year} {self.make} {self.model}")
#             self.is_running = False
#             self.speed = 0
#             print(f"The {self.make} {self.model} has stopped.")
#         else:
#             print(f"The {self.make} {self.model} is already stopped.")

#     # Method to accelerate the car
#     def accelerate(self, increase):
#         if self.is_running:
#             self.speed += increase
#             print(f"The {self.make} {self.model} accelerates by {increase} km/h. Current speed: {self.speed} km/h.")
#         else:
#             print(f"Cannot accelerate. The {self.make} {self.model} is not running.")

#     # Method to apply brakes and reduce speed
#     def brake(self, decrease):
#         if self.is_running:
#             self.speed -= decrease
#             if self.speed <= 0:
#                 self.speed = 0
#                 self.stop()
#                 print(f"The {self.make} {self.model} has come to a stop.")
#             else:
#                 print(f"The {self.make} {self.model} decelerates by {decrease} km/h. Current speed: {self.speed} km/h.")
#         else:
#             print(f"Cannot brake. The {self.make} {self.model} is not running.")
            
# tesla_car = Car("Tesla", "Model 3", 2021, "Black")
# tesla_car.start()
# tesla_car.accelerate(20)

# print(tesla_car.is_running, tesla_car.speed)

# tesla_car.is_running = False

# print(tesla_car.is_running, tesla_car.speed)

class Car:
    def __init__(self, make, model, year, color):
        self.__make = make         # Private attribute
        self.__model = model       # Private attribute
        self.__year = year         # Private attribute
        self.__color = color       # Private attribute
        self.__is_running = False  # Private attribute to track running state
        self.__speed = 0           # Private attribute to track speed
        
    def __str__(self):
        running_status = "running" if self.__is_running else "stopped"
        return (f"{self.__year} {self.__make} {self.__model} {self.__color}, "
                f"currently {running_status}, speed: {self.__speed} km/h")

    # Display car information
    def display_info(self):
        print(f"Car Information:\n Make: {self.__make}\n Model: {self.__model}\n Year: {self.__year}\n Color: {self.__color}\n Speed: {self.__speed} km/h")

    # Start the car
    def start(self):
        if not self.__is_running:
            self.__is_running = True
            print(f"The {self.__make} {self.__model} has started.")
        else:
            print(f"The {self.__make} {self.__model} is already running.")

    # Stop the car
    def stop(self):
        if self.__is_running:
            self.__is_running = False
            self.__speed = 0
            print(f"The {self.__make} {self.__model} has stopped.")
        else:
            print(f"The {self.__make} {self.__model} is already stopped.")

    # Accelerate the car
    def accelerate(self, increase):
        if self.__is_running:
            self.__speed += increase
            print(f"The {self.__make} {self.__model} accelerates by {increase} km/h. Current speed: {self.__speed} km/h.")
        else:
            print(f"Cannot accelerate. The {self.__make} {self.__model} is not running.")

    # Brake the car
    def brake(self, decrease):
        if self.__is_running:
            self.__speed -= decrease
            if self.__speed <= 0:
                self.__speed = 0
                self.stop()
                print(f"The {self.__make} {self.__model} has come to a stop.")
            else:
                print(f"The {self.__make} {self.__model} decelerates by {decrease} km/h. Current speed: {self.__speed} km/h.")
        else:
            print(f"Cannot brake. The {self.__make} {self.__model} is not running.")

    # Property to get the current speed (read-only)
    @property
    def speed(self):
        return self.__speed

    # Property to check if the car is running (read-only)
    @property
    def is_running(self):
        return self.__is_running

# Example usage
tesla_car = Car("Tesla", "Model 3", 2021, "Black")
tesla_car.start()

tesla_car.accelerate(56)

#tesla_car.__is_running, tesla_car.__speed


print(tesla_car.__dict__)

print(tesla_car._Car__make)

print(tesla_car)

tesla_car.display_info()






