import requests
from bs4 import BeautifulSoup

def fetch_weather(city):
    url = f"https://www.weather.com/weather/today/l/{city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    weather_div = soup.find('div', class_='CurrentConditions--phraseValue--2xXSr')
    temp_span = soup.find('span', class_='CurrentConditions--tempValue--3KcTQ')

    if weather_div and temp_span:
        weather = weather_div.text
        temperature = temp_span.text
        return weather, temperature
    else:
        raise ValueError("Could not find weather information on the page.")

if __name__ == "__main__":
    city = "Sao+Paulo"
    try:
        weather, temperature = fetch_weather(city)
        print(f"The weather in {city.replace('+', ' ')} is {weather} with a temperature of {temperature}.")
    except ValueError as e:
        print(e)
