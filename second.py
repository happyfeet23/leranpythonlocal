import requests

def get_states(country_name):
    """
    Fetches the list of states/provinces for a given country using RESTCountries API.
    Note: Not all countries have state data in this API.
    """
    url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        
        data = response.json()
        print(data)
        country_data = data[0]
        
        # Check if states data exists
        if 'subdivisions' in country_data.get('translations', {}):
            # This API doesn't directly provide states, so we use this alternative
            print(f"States data not directly available for {country_name} in this API.")
            print("Try Method 2 with geopy instead.")
            return []
        else:
            # Some countries have states in different formats
            if 'states' in country_data:
                states = [state['name'] for state in country_data['states']]
                return states
            else:
                print(f"No states data available for {country_name}")
                return []
                
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

# Get user input
country = input("Enter country name: ").strip()
states_list = get_states(country)

if states_list:
    print(f"\nStates in {country}:")
    for i, state in enumerate(states_list, 1):
        print(f"{i}. {state}")
else:
    print(f"Could not retrieve states for {country}")