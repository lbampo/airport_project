from flight_class import *
from people_class import *

class Passenger(People):

    def __init__(self, flight_number, destination, origin, gate_close, fname, lname, email, passport_number):
        super().__init__(flight_number, destination, origin, gate_close)
        self.fname = fname
        self.lname = lname
        self.email = email
        self.passport_number = passport_number

    # def passenger_name

