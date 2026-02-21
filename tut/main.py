import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data

    else:
        print(f"ERROR. Failed to retrieve data. {response.status_code}")
    

pokemon_name = str(input("Enter the name of the Pokemon: "))
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Primary-Type: {pokemon_info["types"][0]["type"]["name"]}")
