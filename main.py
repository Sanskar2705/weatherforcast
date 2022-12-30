import requests
from twilio.rest import Client


api_key= "*************************"
OWM_Endpoint ="https://api.openweathermap.org/data/2.5/forecast"

account_sid ="*****************************"
auth_token ="*******************************"

weather_params ={
    "lat": -14.452114,
    "lon": 132.271515,
    "appid": api_key,

}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data= response.json()
weather_slice= weather_data["list"][:1]
print(weather_slice)

will_rain = False
for three_hour_data in weather_slice:
    condition_code= three_hour_data["main"]['temp']
    condition_code = int(condition_code)- 273
    print(condition_code)
    if int(condition_code)>29:
        will_rain =True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"weather is sunny today,the temp is: {condition_code}  ",
        from_='+18318511615',
        to='+***********'
    )
    print(message.status)
