import tkinter as tk
import requests

API_KEY = "05fdcdc413888d3ae6dc084f7bc1a266"  # Get from https://openweathermap.org/api

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            result_label.config(text=f"Error: {data['message']}")
        else:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"].capitalize()
            result_label.config(text=f"{city}:\n{temp}°C\n{desc}")
    except:
        result_label.config(text="Error retrieving weather data.")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

get_button = tk.Button(root, text="Get Weather", command=get_weather)
get_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
