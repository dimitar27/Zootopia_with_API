import requests

API_KEY = "FuF6U+IVQEQQFEuS9cfH0g==jkMXxC0hPbETw9P6"
URL = f"https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
      Fetches the animals data for the animal 'animal_name'.
      Returns: a list of animals, each animal is a dictionary:
      {
        'name': ...,
        'taxonomy': {
          ...
        },
        'locations': [
          ...
        ],
        'characteristics': {
          ...
        }
      },
      """
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}
    response = requests.get(URL, headers=headers, params=params)
    response.encoding = "utf-8"
    data = response.json()
    return data