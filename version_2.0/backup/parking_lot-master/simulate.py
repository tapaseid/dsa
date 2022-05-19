import time
from parking_lot.entities.vehicle import Car, Vehicle
from parking_lot.controller import ParkingManager


class Simulator:
    def __init__(self):
        self.parking_manager = ParkingManager(parking_spots_per_vehicle_type=2)

    def park_new_vehicle(self, vehicle_type):
        sub_clss = Vehicle.__subclasses__()
        vehicle_cls = None
        for sub_cls in sub_clss:
            if sub_cls.__vehicle_type__ == vehicle_type:
                vehicle_cls = sub_cls

        vehicle_obj = vehicle_cls()
        result = self.parking_manager.enter(vehicle=vehicle_obj)
        self.parking_manager.show_parking_lot()
        return result

    def main(self):
        self.parking_manager.show_parking_lot()
        result1 = self.park_new_vehicle(vehicle_type="Car")
        time.sleep(2)
        result2 = self.park_new_vehicle(vehicle_type="Car")
        time.sleep(3)
        result3 = self.park_new_vehicle(vehicle_type="Car")

        self.parking_manager.exit(parking_ticket=result1["data"])
        self.parking_manager.show_parking_lot()

        self.parking_manager.exit(parking_ticket=result2["data"])
        self.parking_manager.show_parking_lot()

        self.parking_manager.show_parking_lot()
        result1 = self.park_new_vehicle(vehicle_type="Truck")
        time.sleep(2)
        result2 = self.park_new_vehicle(vehicle_type="Truck")
        time.sleep(3)
        result3 = self.park_new_vehicle(vehicle_type="Truck")

        self.parking_manager.exit(parking_ticket=result1["data"])
        self.parking_manager.show_parking_lot()

        self.parking_manager.exit(parking_ticket=result2["data"])
        self.parking_manager.show_parking_lot()

        self.parking_manager.show_parking_lot()
        result1 = self.park_new_vehicle(vehicle_type="Bike")
        time.sleep(2)
        result2 = self.park_new_vehicle(vehicle_type="Bike")
        time.sleep(3)
        result3 = self.park_new_vehicle(vehicle_type="Bike")

        self.parking_manager.exit(parking_ticket=result1["data"])
        self.parking_manager.show_parking_lot()

        self.parking_manager.exit(parking_ticket=result2["data"])
        self.parking_manager.show_parking_lot()


if __name__ == "__main__":
    Simulator().main()
