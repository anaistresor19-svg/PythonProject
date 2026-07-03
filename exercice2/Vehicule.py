class Vehicule :
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
v1 = Vehicule("Toyota", 230,15)
print(v1.name, v1.max_speed, v1.mileage)
