# Design a parking lot
## Setup
- Install python3 if not installed already
- Clone the repository using: `git clone https://github.com/princemathur4/parking_lot`
- cd into the project root folder
- Create a Python3 virtual env using: `python3 -m venv ./virtualenv`
- Activate the virtual env for your command line,

For Windows:
`.\virtualenv\Scripts\activate`

For Linux:
`source ./virtualenv/bin/activate`
- install packages using requirement.txt file `pip install -r requirements.txt`
 
## Run
- cd into the project root folder
- Activate virtual env like mentioned above
- Run using command: `python simulate.py`


# Proposed Design:
Entities:
- Vehicle
    Types:
    - Cars
    - Bikes
    - Trucks
    Methods/attributes:
    1 - parking cost
    2 - for space/area that they occupy
   
- Parking Spot
    Methods/attributes:
    - slot type
    - slot number
    - occupied: bool
    - vehicle details
    - vehicle entry datetime


- ParkingTicket
    - parking spot id
    - time of entry

- PaymentSystem
    - payment methods - [Debit Card, Credit Card, Cash, UPI]
    - do_payment

- Parking Lot
    - Dedicated limited space = {
        "Car": [ParkingSpot1, ParkingSpot2, ParkingSpot3],
        "Bikes": [ParkingSpot4, ParkingSpot5, ParkingSpot6],
        "Trucks": [ParkingSpot7, ParkingSpot8, ParkingSpot9],
    }
    - vehicle queue - mapping -> vehicle details
    - Number of vehicles present - mapping -> vehicle type and count
    - Entry(vehicle_details):
        `do a check for parking space available or not
        assign a parking space accordingly and
        also update the details of vehicle in ParkingSpot
        also generate a parkingTicket
        else add in waiting in queue`
    
    - Exit(parking_ticket):
        `we need to free the parking spot corresponding to that ticket
        cost = calculate_cost(parking_ticket)
        status = PaymentSystem.do_payment(cost)
        perform a check if payment is successful or not
        if there is any vehicle in queue waiting
        then we need to assign a parking spot and do the payment accordingly`
        Entry(first_vehicle_in_queue)
    
    - calculate_cost(parking_ticket):
        `no of hours = current_time - parking_ticket.time
        vehicleobj = get_vehicle_obj(parking_ticket)
        return multiply no of hours * vehicleobj.parking_cost`
