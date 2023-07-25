import pyowm
token = "07e12b4f9430603641a80889201a8fc9" #Your token goes here
own= pyowm.OWM(token).weather_manager()

def get_weather():
    zip_code = "140301" #Update this to your zip code
    weather = own.weather_at_zip_code(zip_code, 'IN').weather
    temperature = int(round(weather.temperature(unit='celsius')['temp'], 0))
    return f"Currently, the temperature is {temperature} degrees"
