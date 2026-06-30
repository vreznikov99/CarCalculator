import calculator

n = list()
if __name__ == '__main__':
    calc = calculator.Calculator(years=3)
    calc.add_car(
        calculator.Car("Toyota Corolla", 110000, 7, 1200, 2500),
    )
    calc.add_car(
        calculator.ElectricalCar("Tesla Model 3", 200000, 5500, 150),
    )
    calc.add_car(
        calculator.Car("Range Rover", 650000, 3, 3000, 7000),
    )
    calc.print_cars()