import streamlit as st
import datetime
import requests

CSS = """
h1,h2,h3 {
color:red;
}

.css-145kmo2{
    color:white;
    font-size: 15px;
}

body {
    background-image: url(https://images.unsplash.com/photo-1476106900527-9664af9d4d28?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=3294&q=80);
    background-size: cover;
}
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

'''
# NY Taxi fare
'''

st.markdown('''
### **Please enter your taxi trip details**
''')

p_date = st.date_input(
    "Pickup date",
    datetime.date(2021, 2, 26))

p_time = st.time_input(
    'Pickup time?',
    value=datetime.time(12, 0))

p_long = st.text_input(
        'Pickup longitude?',
        value=40.7614327)
p_lat = st.text_input(
        'Pickup latitude?',
        value=-73.9798156)
d_long = st.text_input(
        'Pickup latitude?',
        value=40.6413111)
d_lat = st.text_input(
        'Pickup latitude?',
        value=-73.9797156)

display = ("1", "2", "3", "4", "5", "6", "7", "8")

options = list(range(len(display)))

pickup_datetime = f'{p_date} {p_time} UTC'

passenger_count = st.selectbox('Number of Passengers', options, format_func=lambda x: display[x])


url = 'http://taxifare.lewagon.ai/predict_fare/'
params = dict(
  key='x',
  pickup_datetime=pickup_datetime,
  pickup_longitude=p_long,
  pickup_latitude=p_lat,
  dropoff_longitude=d_long,
  dropoff_latitude=d_lat,
  passenger_count=passenger_count
)

predict = round(float(requests.get(url, params=params).json()['prediction']),2)

st.markdown('## **You will pay around $' + str(predict)+"**")
