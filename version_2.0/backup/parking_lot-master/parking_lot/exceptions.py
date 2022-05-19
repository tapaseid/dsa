class RootException(Exception):
    def __repr__(self):
        return self.error_message


class ParkingSpotNotAvailable(RootException):
    error_message = "Parking spot not available"


class ParkingSpotAlreadyOccupied(RootException):
    error_message = "Vehicle already parked at the current spot"


class NoVehicleParked(RootException):
    error_message = "No vehicle is parked at the current spot"


class InvalidPaymentMethod(RootException):
    error_message = "Please select a valid payment method"


class InvalidParkingSpotId(RootException):
    error_message = "Please select a valid payment method"
