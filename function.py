from distutils.command.config import config
import pickle
from unittest import result
import numpy as np
import json
import config

class book_status():

    def __init__(self,no_of_adults,no_of_children,no_of_weekend_nights,no_of_week_nights,type_of_meal_plan,
    required_car_parking_space,room_type_reserved,lead_time,market_segment_type,repeated_guest,
    no_of_previous_cancellations,no_of_previous_bookings_not_canceled,avg_price_per_room,no_of_special_requests,
    overall_people,average_price_per_room_person,overall_nights,overall_price):
        """ init function for accepting the User Input """

        self.no_of_adults = no_of_adults
        self.no_of_children = no_of_children
        self.no_of_weekend_nights= no_of_weekend_nights
        self.no_of_week_nights =no_of_week_nights
        self.type_of_meal_plan = type_of_meal_plan
        self.required_car_parking_space = required_car_parking_space
        self.room_type_reserved = room_type_reserved
        self.lead_time = lead_time
        self.market_segment_type = market_segment_type
        self.repeated_guest = repeated_guest
        self.no_of_previous_cancellations = no_of_previous_cancellations
        self.no_of_previous_bookings_not_canceled= no_of_previous_bookings_not_canceled
        self.avg_price_per_room =avg_price_per_room
        self.no_of_special_requests = no_of_special_requests
        self.overall_people = overall_people
        self.average_price_per_room_person = average_price_per_room_person
        self.overall_nights = overall_nights
        self.overall_price =overall_price


    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as file:
            self.model = pickle.load(file)

        with open(config.COLUMN_LIST__PATH,'r') as file:
            self.columns_dict = json.load(file)


    def result(self):
        self.load_model()

        array = np.zeros(len(self.columns_dict['columns']))

        array[0] = self.no_of_adults     
        array[1] = self.no_of_children
        array[14] = self.no_of_adults + self.no_of_children
        array[2] = self.no_of_weekend_nights
        array[3] = self.no_of_week_nights
        array[4] = self.type_of_meal_plan       
        array[5] = self.required_car_parking_space
        room = int((self.room_type_reserved.split())[-1])
        array[6] = room   
        array[7] = self.lead_time
        market = int(self.market_segment_type.replace('Online',"1").replace('Offline',"0").replace('Corporate',"2").replace('Complementary',"3").replace('Aviation',"4"))
        array[8] = market
        array[9] = self.repeated_guest
        array[10]=self.no_of_previous_cancellations
        array[11] = self.no_of_previous_bookings_not_canceled
        array[12] = self.avg_price_per_room
        array[13] = self.no_of_special_requests
        array[14] = self.overall_people
        array[15] = self.average_price_per_room_person
        array[16] = self.overall_nights
        array[17] = self.overall_price


        # print(array)

        result = self.model.predict([array])
        if result[0] == 0 :
            outt = "Booking Cancel"
        else:
            outt = "Booking Not Cancel"
        # print(result)

        return outt




if __name__ == '__main__':

    no_of_adults = 0
    no_of_children =2
    no_of_weekend_nights= 0
    no_of_week_nights= 1
    type_of_meal_plan= 2
    required_car_parking_space= 1
    room_type_reserved = "Room_Type 1"
    lead_time=224.0
    market_segment_type="Online"
    repeated_guest=0
    no_of_previous_cancellations=0
    no_of_previous_bookings_not_canceled=0
    avg_price_per_room=65.0
    no_of_special_requests=0
    overall_people=2
    average_price_per_room_person= 32.5
    overall_nights=3
    overall_price =195.0


    book_status_obj = book_status(no_of_adults,no_of_children,no_of_weekend_nights,no_of_week_nights,type_of_meal_plan,
    required_car_parking_space,room_type_reserved,lead_time,market_segment_type,repeated_guest,
    no_of_previous_cancellations,no_of_previous_bookings_not_canceled,avg_price_per_room,no_of_special_requests,
    overall_people,average_price_per_room_person,overall_nights,overall_price)

    book_status_obj.result()

