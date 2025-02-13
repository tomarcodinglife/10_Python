# How to count no of object creat using class
class car:
    total_no_of_Car = 0 # add variable for count no of car
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"{self.brand} - {self.model}")
        car.total_no_of_Car += 1 # using this i can track how much time use this function

    def fuelType(self):
        print("Diesel or Petrol")

class ElectricCar(car) :
    total_no_of_Electric_Car = 0 # # add variable for count no of car
    def __init__(self, brand, model, battrySize):
        self.battrySize = battrySize
        super().__init__(brand, model)
        print(f"{self.brand} - {self.model} - {self.battrySize}")
        ElectricCar.total_no_of_Electric_Car += 1 # using this i can track how much time use this function

    def fuelType(self):
        print("Electric Charge")

carFirst = ElectricCar("Tesla", "CyberTruck", "80 kWh")
carFirst.fuelType()
carSecond = car("Tata", "Safari")

print(car.total_no_of_Car) # 2
print(ElectricCar.total_no_of_Electric_Car) # 1

