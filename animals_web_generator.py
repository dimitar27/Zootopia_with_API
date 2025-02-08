import requests


API_KEY = "FuF6U+IVQEQQFEuS9cfH0g==jkMXxC0hPbETw9P6"
URL = f"https://api.api-ninjas.com/v1/animals"


def load_data(url, animal_name):
  """ Loads a JSON file """
  headers = {"X-Api-Key": API_KEY}
  params = {"name": animal_name}
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


def animal_not_found(animal_name):
    return (
        f"<h2 style = 'color: #696969;font-weight: 400;'> "
        f"The animal {animal_name} doesn't exist.</h2>"
    )


def update_html_template(animal_info):
    """Updates the HTML template"""
    with open("animals_template.html", "r") as fileobj:
        html_content = fileobj.read()

    animal_info_template = html_content.replace("__REPLACE_ANIMALS_INFO__", animal_info)

    with open("animals.html", "w") as fileobj:
        fileobj.write(animal_info_template)
    print("Website was successfully generated to the file animals.html.")


def main():
    animal_name = input("Enter a name of an animal: ")
    animals_data = load_data(URL, animal_name)

    if not animals_data:
        animal_info =  animal_not_found(animal_name)
        update_html_template(animal_info)

    else:
        output = ''
        for animal_obj in animals_data:
        #Append information to each string
            output += serialize_animal(animal_obj)

        update_html_template(output)


if __name__ == "__main__":
    main()