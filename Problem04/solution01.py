#Basic Class and objects
#Create a car class with attributes like brand and model . Then create an instance
#of this class


class Car:
    # brand = None
    # model = None
    def __init__(self, brand,model):
       self. __brand = brand
       self.model = model

    def get_brand(self):
        return self.__brand
    


    def full_name(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85kWh")
print(my_tesla.__brand )   
print(my_tesla.fu)   


# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_car2 = Car("Tata","Safari")
# print(my_car2.brand)
# print(my_car2.model)



#Class Method and Self
# Problem Add a method to the car class that diplays the full name of the car(brand and model)


# Create an Electric car class that inherits from the car class and has an additional attribute battery_size

#Encapsulation

#modify the car class to encapsulate the brand attribute making it private and provide a geeter method for it

