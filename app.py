from flask import Flask,request, render_template
from function import book_status

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def  predict():

    data = request.form

    no_of_adults = int(data['no_of_adults'])
    no_of_children = int(data['no_of_children'])
    no_of_weekend_nights= int(data['no_of_weekend_nights'])
    no_of_week_nights =int(data['no_of_week_nights'])
    type_of_meal_plan = int(data['type_of_meal_plan'])
    required_car_parking_space = float(data['required_car_parking_space'])
    room_type_reserved = str(data['room'])
    lead_time = float(data['lead_time'])
    market_segment_type = str(data['market'])
    repeated_guest = int(data['repeated_guest'])
    no_of_previous_cancellations = int(data['no_of_previous_cancellations'])
    no_of_previous_bookings_not_canceled= int(data['no_of_previous_bookings_not_canceled'])
    avg_price_per_room =float(data['avg_price_per_room'])
    no_of_special_requests = float(data['no_of_special_requests'])
    overall_people = no_of_adults + no_of_children
    average_price_per_room_person = float(data['average_price_per_room_person'])
    overall_nights = int(data['overall_nights'])
    overall_price =float(data['overall_price'])



    

    status = book_status(no_of_adults,no_of_children,no_of_weekend_nights,no_of_week_nights,type_of_meal_plan,
    required_car_parking_space,room_type_reserved,lead_time,market_segment_type,repeated_guest,
    no_of_previous_cancellations,no_of_previous_bookings_not_canceled,avg_price_per_room,no_of_special_requests,
    overall_people,average_price_per_room_person,overall_nights,overall_price)
    Output = status.result()
    print(Output)

    return render_template('index.html',HTML_Output=Output)


if __name__ == "__main__":
    app.run(host ='0.0.0.0' , port = 8080 , debug=True)