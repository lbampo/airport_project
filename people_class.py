from flight_class import *

class People():

    def __init__(self, fname, lname, dob, gender, nationality):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.gender = gender
        self.nationality = nationality


class Staff(People):
    def __init__(self, fname, lname, dob, gender,nationality, staff_id):
        super().__init__(fname, lname, dob, gender, nationality)
        self.staff_ID = staff_id

        self.info_passenger = []
        self.flight_list = []

    def booking_passenger(self, passenger):
        self.info_passenger.append(passenger)


    def add_flight_list(self, flightlist):
        self.flight_list.append(flightlist)


class Passenger(People):
    def __init__(self, fname, lname, dob, gender, nationality, passport_number):
        super().__init__(fname, lname, dob, gender, nationality)
        self.passport_number = passport_number

    def get_details(self):
        return

















    #
    # def name(self):
    #     return f"Passenger name: {self.fname} {self.lname}"
    #
    # def destination(self):
    #     return f"Flight destination: {self.destination}"
    #
    # def origin(self):
    #     return f"Flight origin: {self.origin}"
    #

