import requests
from bs4 import BeautifulSoup

def fetch_weather(city):
    url = f"https://www.weather.com/weather/today/l/{city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    weather = soup.find('div', class_='CurrentConditions--phraseValue--2xXSr').text
    temperature = soup.find('span', class_='CurrentConditions--tempValue--3KcTQ').text

    return weather, temperature

if __name__ == "__main__":
    city = "Sao+Paulo"
    weather, temperature = fetch_weather(city)
    print(f"The weather in {city.replace('+', ' ')} is {weather} with a temperature of {temperature}.")
