class Car:
    def __init__(self, car_id, model, year, is_available=True, price_per_day=0):
        self.car_id = car_id
        self.model = model
        self.year = year
        self.is_available = is_available
        self.price_per_day = price_per_day

class CarBookingSystem:
    def __init__(self):
        self.cars = {}

    def add_car(self, car):
        self.cars[car.car_id] = car

    def remove_car(self, car_id):
        if car_id in self.cars:
            del self.cars[car_id]

    def book_car(self, car_id):
        if car_id in self.cars and self.cars[car_id].is_available:
            self.cars[car_id].is_available = False
            return True
        return False

    def return_car(self, car_id):
        if car_id in self.cars and not self.cars[car_id].is_available:
            self.cars[car_id].is_available = True
            return True
        return False

    def view_available_cars(self):
        available_cars = [car for car in self.cars.values() if car.is_available]
        return available_cars

    def view_booked_cars(self):
        booked_cars = [car for car in self.cars.values() if not car.is_available]
        return booked_cars

    def check_car_availability(self, car_id):
        if car_id in self.cars:
            return self.cars[car_id].is_available
        return None

    def update_car_details(self, car_id, model=None, year=None, price_per_day=None):
        if car_id in self.cars:
            if model:
                self.cars[car_id].model = model
            if year:
                self.cars[car_id].year = year
            if price_per_day:
                self.cars[car_id].price_per_day = price_per_day

    def generate_report(self):
        report = {
            "Total Cars": len(self.cars),
            "Available Cars": len(self.view_available_cars()),
            "Booked Cars": len(self.view_booked_cars())
        }
        return report

    def calculate_total_revenue(self):
        total_revenue = sum(car.price_per_day for car in self.view_booked_cars())
        return total_revenue
