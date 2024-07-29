import requests
import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk  # Make sure to install pillow package
from datetime import datetime

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.resizable(True, True)

api_key = 'ffda06a797c8549b6eafc202267d7e71'

# Load weather icons
icons = {
    "clear": ImageTk.PhotoImage(Image.open(r"C:\Users\mayan\Documents\Python Weather app\icons\sun.png")),
    "clouds": ImageTk.PhotoImage(Image.open(r"C:\Users\mayan\Documents\Python Weather app\icons\cloudy5.png")),
    "partly cloudy": ImageTk.PhotoImage(Image.open(r"C:\Users\mayan\Documents\Python Weather app\icons\partly_cloudy.png")),
    "overcast": ImageTk.PhotoImage(Image.open(r"C:\Users\mayan\Documents\Python Weather app\icons\overcast.png")),
    "rain": ImageTk.PhotoImage(Image.open(r"C:\Users\mayan\Documents\Python Weather app\icons\rain.png")),
    "thunderstorm": ImageTk.PhotoImage(Image.open(r"C:\Users\mayan\Documents\Python Weather app\icons\thunderstorm.png")),
    "snow": ImageTk.PhotoImage(Image.open(r"C:\Users\mayan\Documents\Python Weather app\icons\snow.png")),
    "mist": ImageTk.PhotoImage(Image.open(r"C:\Users\mayan\Documents\Python Weather app\icons\mist.png")),
    "haze": ImageTk.PhotoImage(Image.open(r"C:\Users\mayan\Documents\Python Weather app\icons\haze.png")),
    "default": ImageTk.PhotoImage(Image.open(r"C:\Users\mayan\Documents\Python Weather app\icons\default.png"))
}

def get_weather_icon(weather):
    weather = weather.lower()
    if "clear" in weather:
        return icons["clear"]
    elif "clouds" in weather:
        return icons["clouds"]
    elif "partly cloudy" in weather:
        return icons["partly cloudy"]
    elif "overcast" in weather:
        return icons["overcast"]
    elif "rain" in weather:
        return icons["rain"]
    elif "thunderstorm" in weather:
        return icons["thunderstorm"]
    elif "snow" in weather:
        return icons["snow"]
    elif "mist" in weather or "fog" in weather:
        return icons["mist"]
    elif "haze" in weather:
        return icons["haze"]
    else:
        return icons["default"]

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def display_weather(weather_data, user_input):
    clear_frame(content_frame)  # Clear current content

    weather = weather_data['weather'][0]['description']
    temp = round(weather_data['main']['temp'])
    date_time = datetime.utcfromtimestamp(weather_data['dt']).strftime('%Y-%m-%d %H:%M:%S')
    icon = get_weather_icon(weather)
    
    # Create a new frame for centering content
    weather_frame = customtkinter.CTkFrame(master=content_frame)
    weather_frame.pack(pady=20, padx=20, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=weather_frame, text=f"Weather in {user_input}", font=("Roboto", 24))
    label.pack(side="top", pady=12, padx=10)

    icon_label = customtkinter.CTkLabel(master=weather_frame, image=icon)
    icon_label.image = icon  # Keep a reference to avoid garbage collection
    icon_label.pack(side="top", pady=12, padx=10)

    info_label = customtkinter.CTkLabel(master=weather_frame, text=f"Date and Time: {date_time}\nTemperature: {temp}ºF\nWeather: {weather}", font=("Roboto", 20))
    info_label.pack(side="top", pady=12, padx=10)

    back_button = customtkinter.CTkButton(master=weather_frame, text='Back', command=show_main_screen)
    back_button.pack(side="top", pady=12, padx=10)

def show_main_screen():
    clear_frame(content_frame)  # Clear current content
    
    # Recreate widgets for the main screen with a Google-like search bar
    content_frame.pack_propagate(False)  # Prevent content_frame from resizing

    # Add header label
    header_label = customtkinter.CTkLabel(master=content_frame, text="Weather Detector", font=("Roboto", 34))
    header_label.pack(pady=20, padx=20, anchor="n")  # Position header at the top

    search_frame = customtkinter.CTkFrame(master=content_frame)
    search_frame.pack(pady=20, padx=20, fill="both", expand=True)

    global entry1
    entry1 = customtkinter.CTkEntry(master=search_frame, placeholder_text="Search for Weather", font=("Roboto", 24), width=400)
    entry1.pack(pady=12, padx=10)

    global button
    button = customtkinter.CTkButton(master=search_frame, text='Get Weather', command=Weather, font=("Roboto", 18))
    button.pack(pady=12, padx=10)

def Weather():
    user_input = entry1.get()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a city.")
        return
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
    if weather_data.json()['cod'] == '404':
        messagebox.showerror("Error", "No City Found")
    else:
        display_weather(weather_data.json(), user_input)

# Main frame for content
content_frame = customtkinter.CTkFrame(master=root)
content_frame.pack(pady=0, padx=0, fill="both", expand=True)

# Initialize the main screen
show_main_screen()

root.mainloop()
