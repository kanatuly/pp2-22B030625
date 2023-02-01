cars = ["Ford", "Volvo", "BMW"]
print(cars)

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

x = cars[0]
print(x)

cars[0] = "Toyota"
print(cars)

x = len(cars)
print(x)

for x in cars:
    print(x)

cars.append("Honda")
print(cars)

cars.pop(2)
print(cars)

cars.remove("Toyota")
print(cars)
