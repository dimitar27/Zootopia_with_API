import requests

API_KEY = "FuF6U+IVQEQQFEuS9cfH0g==jkMXxC0hPbETw9P6"
URL = f"https://api.api-ninjas.com/v1/animals"

def load_data(url):
  """ Loads a JSON file """
  headers = {"X-Api-Key": API_KEY}
  params = {"name": "fox"}
  response = requests.get(url, headers=headers, params=params)
  response.encoding = "utf-8"
  data = response.json()
  return data


def serialize_animal(animal_obj):
    """ Handles serialization of a single animal object into HTML. """
    output = "" # define an empty string
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj["name"]}</div>'
    output += '<p class="card__text">'
    output += f'<strong>Diet: </strong>{animal_obj["characteristics"]["diet"]}<br/>'
    output += f'<strong>Location: </strong>{animal_obj["locations"][0]}<br/>'

    if animal_obj['characteristics'].get('type') is None:
        output += "<br/>"
        return output

    output += f'<strong>Type: </strong>{animal_obj["characteristics"].get("type")}<br/>'
    output = output.replace("’", "'")
    return output


def main():
    animals_data = load_data(URL)

    output = ''
    for animal_obj in animals_data:
    # Append information to each string
        output += serialize_animal(animal_obj)

    with open("animals_template.html", "r") as fileobj:
        html_content = fileobj.read()

    animal_info = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as fileobj:
        fileobj.write(animal_info)


if __name__ == "__main__":
    main()