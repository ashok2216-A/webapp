# pickling the model
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)

def welcome():
	return 'welcome all'


def prediction(no_of_adults, no_of_children, no_of_weekend_nights, 
				no_of_week_nights, type_of_meal_plan, required_car_parking_space, 
				room_type_reserved, lead_time, arrival_year, arrival_month, arrival_date, 
				market_segment_type, repeated_guest, no_of_previous_cancellations, no_of_previous_bookings_not_canceled, 
				avg_price_per_room, no_of_special_requests):

	prediction = model.predict(
		[[no_of_adults, no_of_children, no_of_weekend_nights, 
				no_of_week_nights, type_of_meal_plan, required_car_parking_space, 
				room_type_reserved, lead_time, arrival_year, arrival_month, arrival_date, 
				market_segment_type, repeated_guest, no_of_previous_cancellations, no_of_previous_bookings_not_canceled, 
				avg_price_per_room, no_of_special_requests]])
	print(prediction)
	return prediction


def main():

	st.title("Hotel Reservation Prediction")
	html_temp = """
	<div style ="background-color:gry;padding:13px">
	<h1 style ="color:gray;text-align:center;">Streamlit Hotel Reservation Prediction ML App </h1>
	</div>
	"""
	st.markdown(html_temp, unsafe_allow_html = True)
	result =""


	no_of_adults = st.slider('No of Adults', 0, 4, 0)
	st.write("You Selected", no_of_adults, 'Adults')

	no_of_children = st.slider('no_of_children', 0, 10, 0)
	st.write("You Selected", no_of_children, 'no_of_children')
	
	no_of_weekend_nights = st.slider('no_of_weekend_nights', 0, 7, 0)
	st.write("You Selected", no_of_weekend_nights, 'Adults')

	no_of_week_nights = st.slider('no_of_week_nights', 0, 17, 0)
	st.write("You Selected", no_of_week_nights, 'Adults')

	type_of_meal_plan = st.slider('type_of_meal_plan', 0, 3, 0)
	st.write("You Selected", type_of_meal_plan, 'Adults')

	required_car_parking_space = st.slider('required_car_parking_space', 0, 1, 0)
	if required_car_parking_space == 0:
		parking = 'Yes'
	else:
		parking ='No'
	st.write("You Selected", parking, 'Adults')

	room_type_reserved = st.slider('room_type_reserved', 0, 6, 0)
	st.write("You Selected", room_type_reserved, 'Adults')
	
	lead_time = st.slider('lead_time', 0, 450, 0)
	st.write("You Selected", lead_time, 'Adults')

	arrival_year = st.selectbox(
    '2017', '2018')

	st.write("You Selected", arrival_year, 'Adults')

	arrival_month = st.slider('arrival_month', 1, 12, 0)
	st.write("You Selected", arrival_month, 'Adults')

	arrival_date = st.slider('arrival_date', 1, 31, 0)
	st.write("You Selected", arrival_date, 'Adults')

	market_segment_type = st.slider('market_segment_type', 0, 4, 0)
	st.write("You Selected", market_segment_type, 'Adults')

	repeated_guest = st.slider('repeated_guest', 0, 1, 0)
	st.write("You Selected", repeated_guest, 'Adults')

	no_of_previous_cancellations = st.slider('no_of_previous_cancellations', 0, 13, 0)
	st.write("You Selected", no_of_previous_cancellations, 'Adults')

	no_of_previous_bookings_not_canceled = st.slider('no_of_previous_bookings_not_canceled', 0, 60, 0)
	st.write("You Selected", no_of_previous_bookings_not_canceled, 'Adults')

	avg_price_per_room = st.slider('avg_price_per_room', 0, 540, 0)
	st.write("You Selected", avg_price_per_room, 'Adults')

	no_of_special_requests = st.slider('no_of_special_requests', 0, 5, 0)
	st.write("You Selected", no_of_special_requests, 'Adults')
	if st.button("Predict"):
		result = prediction(no_of_adults, no_of_children, no_of_weekend_nights, 
				no_of_week_nights, type_of_meal_plan, required_car_parking_space, 
				room_type_reserved, lead_time, arrival_year, arrival_month, arrival_date, 
				market_segment_type, repeated_guest, no_of_previous_cancellations, no_of_previous_bookings_not_canceled, 
				avg_price_per_room, no_of_special_requests)
	if result == 0:
		res = 'Not Cancelled'
	elif result == 1:
		res = 'Cancelled'
	else:
		None
	st.success('The output is {0}'.format(result))
	st.success('The Reservation is', res)
	
if __name__=='__main__':
	main()
