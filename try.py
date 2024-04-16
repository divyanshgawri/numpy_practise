#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.#Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        self.total_fare = self.capacity *100
        print("your total fare of the vehicle is ",self.total_fare)
class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage, capacity)
        print(f"the bus is {self.name} and its mileage is {self.mileage},, its capacity is {self.capacity}")
    def fare(self):
        super().fare()
        self.final_amount = self.total_fare +(self.total_fare*0.1)
        print(f"Your Final Amount is {self.final_amount}")
School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
# v = Vehicle("tour",150,12)
# v.fare()
