import requests

apikey = '32c84eae16aa13319b840ac5a3fd67f0'

weather_input = input("Enter city: ")

weather_datas = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={weather_input}&units=imperial&APPID={apikey}")

if weather_datas.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_datas.json()['weather'][0]['main']
    temp = round(weather_datas.json()['main']['temp'])

    print(f"The weather in {weather_input} is: {weather}")
    print(f"The temperature in {weather_input} is: {temp}ºF")
