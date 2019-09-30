from flight_class import *
from people_class import *
from passengers_class import *



flight_1 = Flight('BA1465', 'Accra(Ghana)', 'London(Heathrow)', '12:45' )
flight_2 = Flight('RY1346', 'Lisbon(Portugal)', 'Lille(France)', '6:00')





flight_dict = {
    'flight_1': [flight_1.flight_number, flight_1.destination, flight_1.orgin, flight_1.flight_time],
    'flight_2': [flight_2.flight_number, flight_2.destination, flight_2.orgin, flight_2.flight_time]
}


pass_list = [('Lennox Bampoe-Addo - 153647568'), ('Rory .P. Stoke - 164856498') ]

pass_list1 = [('Stormzy - 564736546'), ('Eyrizzle - 563820479')]




# print('{flight_1[0]}'.format_map(flight_dict))


helper_input = input("How can I help you?: ")

while helper_input != 'no':

    helper_question = input("Ok, what can I do for you?: ")
    count = 0
    if 'all flights' in helper_question:
        print('Ok we have Flights: \n {flight_1[0]} | Destination: {flight_1[1]} | Origin: {flight_1[2]} | flight time: {flight_1[3]} \n'
              ' {flight_2[0]} | Destination: {flight_2[1]} | Origin: {flight_2[2]} | flight time: {flight_2[3]}'.format_map(flight_dict))



    elif 'book a flight' in helper_question:

        count = 0
        while len(pass_list ) < 4:
            pass_fname = input("Of course you can. May I have your first name please ?: ")
            # pass_list.append(pass_fname)
            pass_lname = input("And your last name ?: ")
            # pass_list.append(pass_lname)
            pass_nationality = input("lovely and finally your passport number please?: ")
            passenger_ID = (f"{pass_fname} {pass_lname} - {pass_nationality}")


            print('\n')

            passenger_dict = {}
            which_flight = input("Ok so which flight would you like to get?").lower().strip()
            if ('ghana' or 'accra') in which_flight:
                pass_list.append(passenger_ID)
                passenger_dict.update({'BA1465' : pass_list})

            else:
                pass_list1.append(passenger_ID)
                passenger_dict.update({'RY1346' : pass_list1})


            # print(pass_list)
            print("\n Ok, that's been processed for you ")

            print(passenger_dict)



            helper_question3 = input(" \n Can I help you with anything else?").strip()
            if helper_question3 != 'no':
                print("No problem")

            else:
                print("Ok, hope Ive helped, Have an amazing day")
                break



else:
    print("Ok, well have an amazing day")
#


#-----------------------------------------------------------
#
# # print("people_class test")
# #
# # people_1 = People('BA1465', 'Accra - Ghana', 'London - England', '12.45', 'Rory .P.', 'Stokes', '134515647')
# #
# # people_2 = People('RY1346', 'Lisbon - Portugal', 'Lille - France', '6:00', 'Filipe', 'Paiva', '156035275')
# #
# #
# # people = {
# #     'passenger1' : [people_1.flight_number, people_1.destination, people_1.origin, people_1.flight_time, people_1.fname, people_1.lname, people_1.passport_number ],
# #     'passenger2' : [people_2.flight_number, people_2.destination, people_2.origin, people_2.flight_time, people_2.fname, people_2.lname, people_2.passport_number  ]
# #
# # }
# #
# # print(' The name of the passenger is: {passenger1[4]} {passenger1[5]} '.format_map(people))
# #
# # print('{passenger1[6]}, {passenger2[6]}'.format_map(people))
#
#
# #-----------------------------------------------------------
#
#
# kiosk_helper = input("Can I help you sir/madam? ").lower().strip()
#
# while kiosk_helper != 'no':
#     kiosk_deeper = input("Ok, how can I assist you today?: ")
#     if 'flights' in kiosk_deeper:
#         pass
#
#     else:
#         print("Nice try")
#
# else:
#     print("Ok, well have a good day")





