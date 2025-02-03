import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')


output = "" # define an empty string
for animal in animals_data:
    # append information to each string
    output += '<li class="cards__item">'
    output += f"Name {animal['name']}<br/>\n"
    output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
    output += f"Location: {animal['locations'][0]}<br/>\n"

    if animal['characteristics'].get('type') is None:
        output += "\n"
        continue
    else:
        output += f"Type: {animal['characteristics'].get('type')}<br/>\n"

    output += "\n"


with open ("animals_template.html", "r") as fileobj:
    html_content = fileobj.read()


animal_info = html_content.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as fileobj:
    fileobj.write(animal_info)