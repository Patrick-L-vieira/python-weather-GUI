# Simple Weather App using Python and Tkinter

This is a simple weather application built using Python, Tkinter, and the `requests` library to fetch weather data from the [wttr.in](http://wttr.in) service.  It also implements caching using `requests-cache` to reduce API calls and improve performance.

## Features

*   Fetches current weather data for a specified location.
*   Displays weather information in a user-friendly format, using custom format codes from wttr.in.
*   Implements caching to reduce API calls and improve performance.  The cache expires after one hour.
*   Simple and easy-to-use graphical user interface built with Tkinter.

## Requirements

*   Python 3.x
*   `requests` library
*   `requests-cache` library
*   `tkinter` library (usually included with Python)

## Installation

1.  **Clone the repository:** If you are using git, clone this repo to your local machine: git clone htps://github.com/bwuny/python-weather-GUI. If you are not using git, download the files and extract them to a new directory.

2.  **Install required libraries:**

    ```bash
    pip install requests requests-cache
    ```
    Tkinter is usually included with Python installations. If for some reason you don't have it, you may need to install it separately depending on your operating system.

## Usage

1.  **Run the script:**

    ```bash
    python weather_app.py
    ```

2.  **Enter a location:** Enter the desired location (city name, zip code, etc.) in the input field.

3.  **Click "Get Weather":** Click the button to fetch and display the weather information for the specified location.


## Custom Format Codes
The application uses custom format codes provided by `wttr.in` to specify the desired weather parameters in the output. Refer to [wttr.in](https://github.com/chubin/wttr.in) documentation for a complete list of available codes. The format string used in this application is:


`%c+%t(%f)°C+%w+%V+%p`


Which fetches weather parameters in the following order:


`weather condition + temperature(feels like) + wind + visibility + precipitation`




## Caching
The `requests-cache` library is used to cache API responses for one hour. This means that if you request weather data for the same location multiple times within an hour, the app will use the cached data instead of making new requests to `wttr.in`. This helps to:

*   Reduce the load on the `wttr.in` service.
*   Improve the application's performance by avoiding unnecessary network requests.




## License

This project is licensed under the Apache License, Version 2.0 - see the [LICENSE](LICENSE) file for details.  You can find a copy of the license [here](https://www.apache.org/licenses/LICENSE-2.0)
