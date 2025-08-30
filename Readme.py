import requests
import pandas as pd
import matplotlib.pyplot as plt


url = 'https://openweathermap.org/api'
api_key = '4a97f69b13dac0a3eec0866177c6dc1f'
def fetch_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
def extract_weather_info(data):
    if data:
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather = data['weather'][0]['description']
        return {'City': city, 'Temperature': temperature, 'Humidity': humidity, 'Weather': weather}


def visualize_weather(data):
    if data:
        cities = [item['City'] for item in data]
        temperatures = [item['Temperature'] for item in data]
        humidities = [item['Humidity'] for item in data]

        x = range(len(cities))  # x-axis positions

        plt.bar(x, temperatures, width=0.4, label='Temperature (°C)', color='b', align='center')
        plt.bar([p + 0.4 for p in x], humidities, width=0.4, label='Humidity (%)', color='g', align='center')

        plt.xlabel('Cities')
        plt.ylabel('Values')
        plt.title('Weather Data')
        plt.xticks([p + 0.2 for p in x], cities)
        plt.legend()
        plt.show()
if __name__ == '__main__':
    cities = ['Pune', 'Mumbai', 'New Delhi']  # You can add more cities
    weather_data = []
    
    for city in cities:
        data = fetch_weather_data(city)
        weather_info = extract_weather_info(data)
        if weather_info:
            weather_data.append(weather_info)
    
    visualize_weather(weather_data)
