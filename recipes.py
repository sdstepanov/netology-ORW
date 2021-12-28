def get_cook_book():
    cook_book = {}
    name_key = ['ingredient_name', 'quantity', 'measure']
    with open('recipes.txt', encoding='utf-8') as file:
        for line in file:
            cook_book[line.strip()] = []
            ingredients_quantity = int(file.readline())
            for ingredient in range(ingredients_quantity):
                ingredient_list = file.readline().strip().split(' | ')
                cook_book[line.strip()] += [dict(zip(name_key, ingredient_list))]
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person):
    cook_book = get_cook_book()
    shop_list = {}
    for dish in cook_book.keys():
        for name_dish in dishes:
            if dish == name_dish:
                get_ingredient_list(shop_list, cook_book[dish], person)

    return shop_list


def get_ingredient_list(shop_list, dish, person):
    for ingredient in dish:
        ingredient_name = ingredient['ingredient_name']
        measure = ingredient['measure']
        quantity = int(ingredient['quantity']) * person
        if len(shop_list) == 0:
            shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
        else:
            quantity = get_new_quantity(shop_list, quantity, ingredient_name)
            shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return shop_list


def get_new_quantity(shop_list, quantity, ingredient):
    ingredients_list = shop_list.keys()
    for ingredient_name in ingredients_list:
        if ingredient_name == ingredient:
            ingredient_dict = shop_list[ingredient]
            new_quantity = ingredient_dict['quantity'] + quantity
            return new_quantity
    return quantity


print(get_cook_book())
print(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Омлет'], 7))
