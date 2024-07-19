import openmeteo_requests
from openmeteo_sdk.Variable import Variable

om = openmeteo_requests.Client()
params = {
	"latitude": -23.5475,
	"longitude": -46.6361,
    "hourly": "temperature_2m",
    "current": "temperature_2m",
    "minutely_15": "temperature_2m"
}

responses = om.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
response = responses[0]

# Current values
current = response.Current()
current_variables = list(map(lambda i: current.Variables(i), range(0, current.VariablesLength())))
current_temperature_minutely_15 = next(filter(lambda x: x.Variable() == Variable.temperature and x.Altitude() == 2, current_variables))

print(f"TEMP {current_temperature_minutely_15.Value():.2f}°C")
