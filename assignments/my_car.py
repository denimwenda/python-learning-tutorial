from carry import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.display_info())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()