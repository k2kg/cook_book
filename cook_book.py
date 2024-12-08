def read_recipes(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        while line := file.readline().strip():
            dish_name = line
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            file.readline()  # пропускаем пустую строку между рецептами
    return cook_book


# Пример вызова функции
cook_book = read_recipes('recipes.txt')
print(cook_book)
