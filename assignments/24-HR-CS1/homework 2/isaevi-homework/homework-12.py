from datetime import date

class Vehicle:
    def __init__(self, vehicle_id, make, model):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.is_rented = False
        self.rental_date = None

    def rent(self):
        if self.is_rented:
            print(f"{self.make} {self.model} (ID: {self.vehicle_id}) is already rented.")
        else:
            self.is_rented = True
            self.rental_date = date.today()
            print(f"{self.make} {self.model} (ID: {self.vehicle_id}) rented on {self.rental_date}.")

    def return_vehicle(self):
        if not self.is_rented:
            print(f"{self.make} {self.model} (ID: {self.vehicle_id}) is not currently rented.")
        else:
            return_date = date.today()
            days = (return_date - self.rental_date).days or 1
            cost = self.calculate_rental_cost(days)
            self.is_rented = False
            self.rental_date = None
            print(f"{self.make} {self.model} (ID: {self.vehicle_id}) returned on {return_date}.")
            print(f"Total days: {days}, Cost: ${cost}")

    def calculate_rental_cost(self, days):
        return 0

class Car(Vehicle):
    def __init__(self, vehicle_id, make, model, num_doors, daily_rate):
        super().__init__(vehicle_id, make, model)
        self.num_doors = num_doors
        self.daily_rate = daily_rate

    def rent(self):
        if self.is_rented:
            print(f"Car {self.make} {self.model} (ID: {self.vehicle_id}) is already rented.")
        else:
            self.is_rented = True
            self.rental_date = date.today()
            print(f"Car {self.make} {self.model} (ID: {self.vehicle_id}) with {self.num_doors} doors rented on {self.rental_date}.")

    def calculate_rental_cost(self, days):
        return days * self.daily_rate

class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, make, model, has_sidecar, daily_rate):
        super().__init__(vehicle_id, make, model)
        self.has_sidecar = has_sidecar
        self.daily_rate = daily_rate

    def rent(self):
        if self.is_rented:
            print(f"Motorcycle {self.make} {self.model} (ID: {self.vehicle_id}) is already rented.")
        else:
            self.is_rented = True
            self.rental_date = date.today()
            sidecar_msg = "with sidecar" if self.has_sidecar else "without sidecar"
            print(f"Motorcycle {self.make} {self.model} (ID: {self.vehicle_id}) {sidecar_msg} rented on {self.rental_date}.")

    def calculate_rental_cost(self, days):
        return days * self.daily_rate

class Bicycle(Vehicle):
    def __init__(self, vehicle_id, make, model, bike_type, daily_rate):
        super().__init__(vehicle_id, make, model)
        self.bike_type = bike_type
        self.daily_rate = daily_rate

    def rent(self):
        if self.is_rented:
            print(f"Bicycle {self.make} {self.model} (ID: {self.vehicle_id}) is already rented.")
        else:
            self.is_rented = True
            self.rental_date = date.today()
            print(f"Bicycle {self.make} {self.model} (ID: {self.vehicle_id}) ({self.bike_type}) rented on {self.rental_date}.")

    def calculate_rental_cost(self, days):
        return days * self.daily_rate

class RentalSystem:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.vehicle_id] = vehicle
        print(f"{vehicle.make} {vehicle.model} (ID: {vehicle.vehicle_id}) added.")

    def rent_vehicle(self, vehicle_id):
        v = self.vehicles.get(vehicle_id)
        if v:
            v.rent()
        else:
            print(f"No vehicle with ID: {vehicle_id}")

    def return_vehicle(self, vehicle_id):
        v = self.vehicles.get(vehicle_id)
        if v:
            v.return_vehicle()
        else:
            print(f"No vehicle with ID: {vehicle_id}")

    def list_available(self):
        for v in self.vehicles.values():
            if not v.is_rented:
                rate = getattr(v, 'daily_rate', 0)
                print(f"- {v.make} {v.model} (ID: {v.vehicle_id}), Rate: ${rate}/day")

if __name__ == "__main__":
    rs = RentalSystem()
    rs.add_vehicle(Car(1, "Toyota", "Camry", 4, 40))
    rs.add_vehicle(Car(2, "Honda", "Civic", 4, 35))
    rs.add_vehicle(Car(6, "Volkswagen", "Golf 4", 4, 45))
    rs.add_vehicle(Motorcycle(3, "Harley-Davidson", "Sportster", False, 30))
    rs.add_vehicle(Bicycle(4, "Giant", "Defy", "road", 10))
    rs.add_vehicle(Bicycle(5, "Trek", "Marlin", "mountain", 12))

    print("\nAvailable vehicles:")
    rs.list_available()

    rs.rent_vehicle(1)
    rs.rent_vehicle(3)
    rs.rent_vehicle(4)
    rs.rent_vehicle(1)

    print("\nAvailable after rentals:")
    rs.list_available()

    rs.return_vehicle(3)

    print("\nAvailable after return:")
    rs.list_available()
