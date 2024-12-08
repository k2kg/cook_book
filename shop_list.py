from cook_book import read_recipes

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = read_recipes('recipes.txt')
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list


# Пример вызова функции
if __name__ == "__main__":
    shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    print(shop_list)
