# Weather Detector 

#### Description:
Weather Detector is a Python script that creates a simple weather application using the `customtkinter` library for a modern user interface and `requests` to fetch weather data from the OpenWeatherMap API. This application provides an intuitive and interactive way to check weather conditions for a specified city.

## Overview
The application offers a graphical interface where users can input a city name, retrieve weather data by clicking a button, and view the results, including weather conditions and temperature.

## Key Features

1. **Modern UI:**
   - Utilizes `customtkinter` to create a sleek, modern-looking application with customizable themes.
   - The interface includes a header, a search bar, and buttons styled to fit a contemporary design.

2. **Weather Data Retrieval:**
   - Fetches weather data from the OpenWeatherMap API based on user input.
   - Displays current weather conditions using icons for a visual representation (e.g., sunny, cloudy, rainy).

3. **Dynamic Layout:**
   - Dynamically adjusts its layout based on window resizing, ensuring a responsive design.
   - Features a main screen with a search bar and a results screen showing weather information and an option to return to the main screen.

4. **User Interaction:**
   - Users input a city name into a search bar and click a button to get weather information.
   - Displays error messages if no city is found or if the input is empty, enhancing user experience with feedback.

## Functionality

- **`get_weather_icon(weather)`**
  - Returns a corresponding icon based on the weather condition provided.

- **`clear_frame(frame)`**
  - Clears all widgets from a specified frame, used to refresh the content when switching between screens.

- **`display_weather(weather_data, user_input)`**
  - Displays weather information on a results screen, including the weather condition icon, temperature, and a back button to return to the main screen.

- **`show_main_screen()`**
  - Sets up the main screen with a header, search bar, and a button to fetch weather information.

- **`Weather()`**
  - Handles the retrieval of weather data from the OpenWeatherMap API based on user input and displays it by calling `display_weather()`. Shows error messages for invalid inputs or if no data is found.

## Main Frame
- A `customtkinter.CTkFrame` serves as the main content area, packed to fill the window and adapt to resizing.

## Execution
The application initializes by setting up the main screen and enters the Tkinter event loop to wait for user interactions. 

This project is a practical example of using `customtkinter` for building a modern GUI and integrating external APIs for dynamic data display.

