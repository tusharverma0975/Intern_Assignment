import requests
import json

def get_weather(date):
  url = "https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=YOUR_API_KEY&units=metric"
  response = requests.get(url)
  if response.status_code == 200:
    data = json.loads(response.content)
    return data["main"]["temp"]
  else:
    return None

def main():
  option = input("Enter 1 to get weather, 2 to get wind speed, 3 to get pressure: ")
  if option == "1":
    date = input("Enter the date (YYYY-MM-DD): ")
    temp = get_weather(date)
    if temp is not None:
      print(f"The temperature in London on {date} is {temp} degrees Celsius.")
    else:
      print("Error: Unable to get weather data.")
  elif option == "2":
    date = input("Enter the date (YYYY-MM-DD): ")
    wind_speed = get_weather(date)
    if wind_speed is not None:
      print(f"The wind speed in London on {date} is {wind_speed} meters per second.")
    else:
      print("Error: Unable to get weather data.")
  elif option == "3":
    date = input("Enter the date (YYYY-MM-DD): ")
    pressure = get_weather(date)
    if pressure is not None:
      print(f"The pressure in London on {date} is {pressure} hPa.")
    else:
      print("Error: Unable to get weather data.")
  else:
    print("Invalid option.")

if __name__ == "__main__":
  main()