import requests

# Define the API URL for Bengaluru's coordinates
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 12.9719,   # Bengaluru's latitude
    "longitude": 77.5937,  # Bengaluru's longitude
    "current": "temperature_2m"  # Request current temperature
}

try:
    # Send the GET request
    response = requests.get(url, params=params)
    response.raise_for_status()  # Check for HTTP errors
    
    # Parse the JSON response
    data = response.json()
    
    # Extract the current temperature
    current_temp = data["current"]["temperature_2m"]
    unit = data["current_units"]["temperature_2m"]
    
    print("Json output is: ",data)
    print(f"Current temperature in Bengaluru: {current_temp} {unit}")
    
except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")
except KeyError:
    print("Error: Unexpected response format from API")