from parking_lot.entities.vehicle import Vehicle
from parking_lot.exceptions import ParkingSpotNotAvailable, InvalidPaymentMethod, ParkingSpotAlreadyOccupied, \
    InvalidParkingSpotId
from parking_lot.entities.parking_spot import ParkingSpot


class ParkingArea:

    def __init__(self, parking_spots_per_vehicle_type):
        self.parking_spots_per_vehicle_type = parking_spots_per_vehicle_type
        self.parking_space = {
            parking_spot_cls.__spot_type__: [
                parking_spot_cls((self.parking_spots_per_vehicle_type * idx) + (i + 1))
                for i in range(self.parking_spots_per_vehicle_type)
            ] for idx, parking_spot_cls in enumerate(ParkingSpot.__subclasses__())
        }

    def __str__(self):
        """
        This function will return the string representation of the Parking Area
        :return: str
        """
        result = []
        for spot_type in self.parking_space:
            result.append(f"\n{'_' * 11}" + ''.join([f"{'_' * 5}_" for i in range(self.parking_spots_per_vehicle_type)]) + "\n")
            result.append(f"{spot_type}s:".ljust(10, ' '))
            for parking_spot in self.parking_space[spot_type]:
                result.append(str(parking_spot.parking_spot_id).ljust(5, ' '))
            result.append(f"\n|{' '*10}")
            for parking_spot in self.parking_space[spot_type]:
                result.append(f"{parking_spot.parked_vehicle.vehicle_registered_number}".ljust(5, ' ') if parking_spot.occupied else "     ")
            result.extend([f"\n|{'_'*10}", *[f"{'_' * 5}" for i in range(self.parking_spots_per_vehicle_type)]])
        return "PARKING ---------->" + ("|".join(result)) + "|\n"

    def get_free_parking_spot_id(self, vehicle_type):
        """
        Check if there exists any parking spot that is not occupied
        Return the parking spot id if there is
        else raise error
        :param vehicle_type:
        :return:
        """
        for parking_spot in self.parking_space[vehicle_type]:
            if not parking_spot.occupied:
                return parking_spot.parking_spot_id
        raise ParkingSpotNotAvailable

    def assign_parking_spot(self, parking_spot_id: ParkingSpot.parking_spot_id, vehicle: Vehicle):
        """
        Assign the given parking spot id to the given vehicle, and park the vehicle there
        :param parking_spot_id: ParkingSpot.parking_spot_id
        :param vehicle: Vehicle
        """
        for parking_spot in self.parking_space[vehicle.__vehicle_type__]:
            if parking_spot.parking_spot_id == parking_spot_id:
                parking_spot.park(vehicle)

    def get_parking_spot_fees_by_id(self, parking_spot_id: ParkingSpot.parking_spot_id):
        """
        Fetch the parking spot fees by parking spot id
        if id is valid return the fees amount
        else raise error
        :param parking_spot_id:
        :return: ParkingSpot.cost_per_second
        """
        for vehicle_type in self.parking_space.keys():
            for parking_spot in self.parking_space[vehicle_type]:
                if parking_spot.parking_spot_id == parking_spot_id:
                    return parking_spot.cost_per_second
        raise InvalidParkingSpotId

    def get_parking_spot_type_by_id(self, parking_spot_id: ParkingSpot.parking_spot_id):
        """
        Get the parking spot type (Car, Bike, Truck) by parking spot id
        if id is valid return the fees amount
        else raise error
        :param parking_spot_id:
        :return: ParkingSpot.__spot_type__
        """
        for vehicle_type in self.parking_space.keys():
            for parking_spot in self.parking_space[vehicle_type]:
                if parking_spot.parking_spot_id == parking_spot_id:
                    return parking_spot.__spot_type__
        raise InvalidParkingSpotId

    def unassign_parking_spot(self, parking_spot_id: ParkingSpot.parking_spot_id):
        """
        Unpark the vehicle from spot
        :param parking_spot_id: ParkingSpot.parking_spot_id
        """
        for vehicle_type in self.parking_space.keys():
            for parking_spot in self.parking_space[vehicle_type]:
                if parking_spot.parking_spot_id == parking_spot_id:
                    parking_spot.unpark()
