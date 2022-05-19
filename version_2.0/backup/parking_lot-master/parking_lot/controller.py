from datetime import datetime
from parking_lot.entities import Queue
from parking_lot.entities.parking_area import ParkingArea
from parking_lot.entities.payments import PaymentGateway
from parking_lot.entities.vehicle import Vehicle
from parking_lot.exceptions import ParkingSpotNotAvailable
from parking_lot.entities.parking_ticket import ParkingTicket


class ParkingManager:

    def __init__(self, parking_spots_per_vehicle_type):
        self.parking_area = ParkingArea(parking_spots_per_vehicle_type=parking_spots_per_vehicle_type)
        self.vehicle_waiting_queue = {subclass.__vehicle_type__: Queue() for subclass in Vehicle.__subclasses__()}
        self.payment_gateway = PaymentGateway()

    def show_parking_lot(self):
        print(str(self.parking_area))

    def enter(self, vehicle: Vehicle):
        """
        This will handle the process when vehicles wants to enter the parking lot
        :param vehicle: Vehicle
        """
        print(f"A {vehicle.__vehicle_type__} with number {vehicle.vehicle_registered_number} wants to park")
        try:
            free_parking_spot_id = self.parking_area.get_free_parking_spot_id(
                vehicle_type=vehicle.__vehicle_type__
            )
            new_parking_ticket = ParkingTicket(parking_spot_id=free_parking_spot_id)
            self.parking_area.assign_parking_spot(parking_spot_id=free_parking_spot_id, vehicle=vehicle)
            print(f"{vehicle.__vehicle_type__} parked, ticket generated:", str(new_parking_ticket))
            return {"status": True, "data": new_parking_ticket}
        except ParkingSpotNotAvailable:
            self.vehicle_waiting_queue[vehicle.__vehicle_type__].enqueue(vehicle)
            print(f"Parking lot is full, {len(self.vehicle_waiting_queue[vehicle.__vehicle_type__].queue)} "
                  f"{vehicle.__vehicle_type__}(s) waiting in queue.")
            return {"status": False, "message": "Parking lot is full, please wait for sometime."}

    def exit(self, parking_ticket: ParkingTicket, payment_method="CASH"):
        """
        This will handle the process when vehicles wants to exit the parking lot
        :param parking_ticket: ParkingTicket
        :param payment_method: str
            how the user wants to pay
            ("CASH"|"DEBIT CARD"|"CREDIT CARD"|"UPI")
        """
        total_parking_fees = self.calculate_parking_fees(parking_ticket=parking_ticket)
        print("Total parking fees: ₹", total_parking_fees)
        input("Press Enter to complete payment")
        self.payment_gateway.do_payment(total_amount=total_parking_fees, payment_method=payment_method)
        self.parking_area.unassign_parking_spot(parking_ticket.parking_spot_id)

        parking_spot_type = self.parking_area.get_parking_spot_type_by_id(parking_spot_id=parking_ticket.parking_spot_id)
        print(f"{parking_spot_type} exited")
        try:
            first_waiting_vehicle = self.vehicle_waiting_queue[parking_spot_type].dequeue()
            if first_waiting_vehicle:
                print(f"Next {parking_spot_type} in queue entering")
                self.enter(first_waiting_vehicle)
        except Exception as e:
            print(e.__str__())

    def calculate_parking_fees(self, parking_ticket: ParkingTicket):
        """
        This will compute the parking cost for any given parking ticket
        :param parking_ticket: ParkingTicket
        :return: int
        """
        total_parked_time = (datetime.now() - parking_ticket.time_of_entry).seconds
        cost_per_second = self.parking_area.get_parking_spot_fees_by_id(parking_ticket.parking_spot_id)
        print(f"Total parked time: {total_parked_time} seconds")
        return cost_per_second * total_parked_time
