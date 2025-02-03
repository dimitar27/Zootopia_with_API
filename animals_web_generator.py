import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')


for animal in animals_data:
    print(f"Name {animal['name']}")
    print(f"Diet: {animal['characteristics']['diet']}")
    print(f"Location: {animal['locations'][0]}")
    if animal['characteristics'].get('type') is None:
        print()
        continue
    else:
        print(f"Type: {animal['characteristics'].get('type')}")
    print()