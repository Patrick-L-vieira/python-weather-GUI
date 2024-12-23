import requests
import requests_cache
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

# Set up caching
requests_cache.install_cache('weather_cache', backend='sqlite', expire_after=3600)

def get_weather():
    location = location_entry.get()
    if not location:
        messagebox.showwarning("Error", "Please enter a location.")
        return

    try:
        # Custom format string for wttr.in
        format_string = "%c+%t(%f)+%w+%V+%p"  
        url = f"http://wttr.in/{location}?format={format_string}"

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        weather_data = response.text


        weather_label.config(text=weather_data)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather: {e}")




root = Tk()
root.title("Weather App")

#GUI elements
location_label = Label(root, text="Location:")
location_label.grid(row=0, column=0, padx=5, pady=5)

location_var = StringVar()
location_entry = Entry(root, textvariable=location_var)
location_entry.grid(row=0, column=1, padx=5, pady=5)


get_weather_button = Button(root, text="Get Weather", command=get_weather)
get_weather_button.grid(row=1, column=0, columnspan=2, pady=10)

weather_label = Label(root, text="")
weather_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()