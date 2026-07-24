import json

def load_price_list():
    try:
        with open('price_list.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def get_price_for_ingredient(name, price_list):
    print(f'No price on file for {name}')
    pack_options = []

    while True:
        size_input = input("Enter pack size (e.g. '2.5 oz', or 'n' if done): ")
        if size_input.lower() == 'n':
            break

        x = size_input.split()
        amount = float(x[0])
        if len(x) != 1:
            unit = x[1]
        else:
            unit = 'items'

        price_input = float(input('Price for that pack: '))

        pack_options.append({
            'amount': amount,
            'unit': unit,
            'price': price_input
        })

    price_list[name] = pack_options
    return price_list

def save_price_list(price_list):
    with open('price_list.json', 'w') as f:
        json.dump(price_list, f)

def build_weekly_totals():
    pass