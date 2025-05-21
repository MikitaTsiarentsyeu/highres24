class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self) -> None:
        print(f"{self.year} {self.brand} {self.model} is starting.")

    def stop(self) -> None:
        print(f"{self.year} {self.brand} {self.model} is stopping.")


class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, num_doors: int):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def open_trunk(self) -> None:
        print(f"Opening the trunk of the {self.year} {self.brand} {self.model}.")


class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, year: int, has_sidecar: bool = False):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def pop_wheelie(self) -> None:
        print(f"The {self.year} {self.brand} {self.model} pops a wheelie!")

    def attach_sidecar(self) -> None:
        if not self.has_sidecar:
            self.has_sidecar = True
            print(f"Sidecar attached to the {self.year} {self.brand} {self.model}.")
        else:
            print(f"The {self.year} {self.brand} {self.model} already has a sidecar.")


class Truck(Vehicle):
    def __init__(self, brand: str, model: str, year: int, payload_capacity_tons: float):
        super().__init__(brand, model, year)
        self.payload_capacity_tons = payload_capacity_tons

    def load_cargo(self, weight_tons: float) -> None:
        if weight_tons <= self.payload_capacity_tons:
            print(f"Loading {weight_tons} tons onto the {self.year} {self.brand} {self.model}.")
        else:
            print(f"Cannot load {weight_tons} tons: exceeds capacity of {self.payload_capacity_tons} tons.")



if __name__ == "__main__":
    volkswagen = Car("Volkswagen", "Golf", 2007, num_doors=4)
    volkswagen.start()
    volkswagen.open_trunk()
    volkswagen.stop()

    print()  

    
    harley = Motorcycle("Harley-Davidson", "Sportster", 2000)
    harley.start()
    harley.pop_wheelie()
    harley.attach_sidecar()
    harley.attach_sidecar()  
    harley.stop()

    print()  

    volvo_truck = Truck("Volvo", "FH15", 2021, payload_capacity_tons=25.0)
    volvo_truck.start()
    volvo_truck.load_cargo(20.0)
    volvo_truck.load_cargo(30.0)
    volvo_truck.stop()
