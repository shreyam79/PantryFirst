weekly_totals = {}

egg_pack_sizes = [6, 12]
egg_pack_price = {6: 1.09, 12: 1.69}

def buy_and_use(item, needed, pantry, pack_sizes, prices):
    # check how much is already in pantry for this item
    # if enough, use it, cost = 0, update pantry
    # if not enough, figure out how much more is needed,
        # buy the smallest pack that covers that gap,
        # add cost, update pantry with new leftovers
    pass

def get_price_for_ingredient(name):
    print(f'No price on file for {name}')
    pack_options = []

    while True:
        size_input = input("Enter pack size (e.g. '2.5 oz', or 'n' if done)")
        if size_input.lower() == 'n':
            break

        amount = size_input.split[0]
        unit = size_input.split[1]

        price_input = float(input('Price for that pack: '))

        pack_options.append({
            'amount': amount
            'unit': unit
            'price': price_input
        })
    return pack_options