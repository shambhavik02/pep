class car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors 
        self.enginetype=enginetype
    def driving(self):
        print("Car is used for the driving")
# Audi car is inheriting from car class   
class Audi(car):
    def __init__(self, windows, doors,enginetype,horsepower):
        super().__init__(windows,doors,enginetype)
        self.horsepower=horsepower
    def selfDriving(self):
        print("It is self driving")

audiq7=Audi(4,5,"Diesel",200)
print(audiq7.horsepower)
print(audiq7.windows)
audiq7.driving()
audiq7.selfDriving()

car1=car(4,5,"Diesel")
print(car1)
print(audiq7)

print(dir(audiq7))
print(dir(car1))