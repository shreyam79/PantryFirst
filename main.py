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
        amount = ingredient['measures']['metric']['amount']
        unit = ingredient['measures']['metric']['unitShort']
        ingredientsList.append((name, amount, unit))
    return ingredientsList

def buildWeeklyTotals(cart):
    weekly_total = {}
    for recipe in cart:
        ingredients = get_ingredients(recipe['id'])
        for name, amount, unit in ingredients:
            name = name.lower().strip()
            if name in weekly_total:
                weekly_total[name]['amount'] += amount
            else:
                weekly_total[name] = {'amount': amount, 'unit': unit}
    return weekly_total

def main():
    cart = []
    while True:
        query = input('What do you want to cook? ')
        results = search_recipes(query)

        for i, result in enumerate(results):
            print(i+1, result['title'])
        
        choice = int(input('Which one would you like to cook? '))
        chosen_recipe = results[choice-1]
        cart.append(chosen_recipe)

        again = input('Add another recipe? (y/n) ')
        if (again.lower() != 'y'):
            break

    print(buildWeeklyTotals(cart))

main()