import numpy as np
from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):

    @property
    @abstractmethod
    def __vehicle_type__(self):
        pass

    @property
    @abstractmethod
    def size(self):
        pass

    @property
    @abstractmethod
    def vehicle_registered_number(self):
        pass

    @staticmethod
    def get_vehicle_number():
        return np.random.randint(1000, 9999)


class Bike(Vehicle):
    __vehicle_type__ = "Bike"
    size = 5
    vehicle_registered_number: int = None

    def __init__(self):
        self.vehicle_registered_number = self.get_vehicle_number()


class Car(Vehicle):
    __vehicle_type__ = "Car"
    size = 10
    vehicle_registered_number: int = None

    def __init__(self):
        self.vehicle_registered_number = self.get_vehicle_number()


class Truck(Vehicle):
    __vehicle_type__ = "Truck"
    size = 20
    vehicle_registered_number: int = None

    def __init__(self):
        self.vehicle_registered_number = self.get_vehicle_number()
