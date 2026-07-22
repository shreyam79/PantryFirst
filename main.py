import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("SPOONACULAR_KEY")

# Broad search -> specific id

def search_recipes(query):
    url = 'https://api.spoonacular.com/recipes/complexSearch'

    param = {
        "apiKey": api_key,
        "query": f'{query}'
    }

    response = requests.get(url, params=param)
    return response.json()['results']


# ID -> ingredient list

def get_ingredients(recipe_id):
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'

    params = {
        "apiKey": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()
    ingredients = data['extendedIngredients']

    ingredientsList = []

    for ingredient in ingredients:
        name = ingredient['name']
        amount = ingredient['measures']['us']['amount']
        unit = ingredient['measures']['us']['unitShort']
        ingredientsList.append((name, amount, unit))
    return ingredientsList

def main():
    query = input('What do you want to cook? ')
    results = search_recipes(query)

    for i, result in enumerate(results):
        print(i+1, result['title'])
    
    choice = int(input('Which one would you like to cook? '))
    chosen_recipe = results[choice-1]
    recipe_id = chosen_recipe['id']
    print(get_ingredients(recipe_id))

main()