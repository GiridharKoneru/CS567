import unittest
from car import Car, CarBookingSystem

class TestCarBookingSystem(unittest.TestCase):
    def setUp(self):
        self.car_system = CarBookingSystem()
        self.car1 = Car(1, "Toyota Camry", 2020, price_per_day=50)
        self.car2 = Car(2, "Honda Accord", 2019, price_per_day=60)
        self.car_system.add_car(self.car1)
        self.car_system.add_car(self.car2)

    def test_add_car(self):
        self.assertIn(1, self.car_system.cars)
        self.assertIn(2, self.car_system.cars)

    def test_remove_car(self):
        self.car_system.remove_car(1)
        self.assertNotIn(1, self.car_system.cars)

    def test_book_car(self):
        self.assertTrue(self.car_system.book_car(1))
        self.assertFalse(self.car_system.book_car(1))  # Already booked
        self.assertFalse(self.car_system.book_car(3))  # Car not found

    def test_return_car(self):
        self.car_system.book_car(1)
        self.assertTrue(self.car_system.return_car(1))
        self.assertFalse(self.car_system.return_car(2))  # Car not booked
        self.assertFalse(self.car_system.return_car(3))  # Car not found

    def test_view_available_cars(self):
        available_cars = self.car_system.view_available_cars()
        self.assertEqual(len(available_cars), 2)

    def test_view_booked_cars(self):
        self.car_system.book_car(1)
        booked_cars = self.car_system.view_booked_cars()
        self.assertEqual(len(booked_cars), 1)

    def test_check_car_availability(self):
        self.assertTrue(self.car_system.check_car_availability(1))
        self.car_system.book_car(1)
        self.assertFalse(self.car_system.check_car_availability(1))

    def test_update_car_details(self):
        self.car_system.update_car_details(1, model="Toyota Corolla", year=2021, price_per_day=55)
        updated_car = self.car_system.cars[1]
        self.assertEqual(updated_car.model, "Toyota Corolla")
        self.assertEqual(updated_car.year, 2021)
        self.assertEqual(updated_car.price_per_day, 55)

    def test_generate_report(self):
        report = self.car_system.generate_report()
        self.assertEqual(report['Total Cars'], 2)
        self.assertEqual(report['Available Cars'], 2)
        self.assertEqual(report['Booked Cars'], 0)

    def test_calculate_total_revenue(self):
        self.car_system.book_car(1)
        self.car_system.book_car(2)
        total_revenue = self.car_system.calculate_total_revenue()
        self.assertEqual(total_revenue, 110)  # 50 + 60

if __name__ == '__main__':
    unittest.main()
