This app runs on local machine with python 3.8 and django 3 installed, and it uses  https://www.weatherapi.com/ to get 
the weather data and displays it on the html template.

The app validates if the number of days entered is greater than 3 and pops an error message, 
as the free api does not allow us to forecast for more than 3 days

If you would like to change the api key please do it from the settings.py file.

To run this app:
1. Clone this project to you local computer
2. Create a virtual environment with the command "python3.8 -m venv any-name" or "virtualenv -p python3.8 any-name"
3. Activate the virtual environment with the command "source any-name/bin/active"
4. Navigate to where you cloned the project and make sure you are the project folder
5. Install the requirement with the command "pip -r requirements.txt"
5. Run the project with the command "python manage.py runserver"
6. Open the project on your favorite browser with http://localhost:8000/
7. And test it by filling in the city and the number of days fields, and submit

Thanks