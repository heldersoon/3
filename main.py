file = open('recipes.txt', encoding='utf-8')
cook_book = {}
# запускаем построчное чтение открытого файла
for line in file:
# если встретилась пустая строка-разделитель, читаем следующую
    if line.isspace():
        line = file.readline()
# эта строка содержит наименование блюда
    dish_name = line.strip()
# следующая строка - количество инградиентов на одну порцию
    line = file.readline()
    ingredient_numbers = int(line.strip())
# используем его как счетчик цикла при создании списка инградиенто блюда
    ingredient_list = []
    ingredient_keys = ['ingredient_name', 'quantity', 'measure']
    while ingredient_numbers > 0:
# читаем строку и преобразуем в список значений инградиента
        line = file.readline()
        ingredient_values = line.strip().split(' | ')
# из списков ключей иполученных значений инградиента формируем словарь
        ingredient = dict(zip(ingredient_keys, ingredient_values))
# добавляем его в список инградиентов блюда и уменьшаем счетчик цикла
        ingredient_list.append(ingredient)
        ingredient_numbers -= 1
#
    dish = {dish_name: ingredient_list}
    cook_book.update(dish)
# после чтения последней строки файла рецептов закрываем его и выводим полученный словарь рецептов
file.close()
print(cook_book)

# Задание 2

def get_shop_list_by_dishes(dishes, person_count):
    count = int(person_count)
    shop_list = {}
# цикл по списку блюд при вызове функции
    for dish in dishes:
        ingredients = cook_book.get(dish)
# цикл по всем продуктам в рецепте блюда
        for ingredient in ingredients:
            ingr = {}
            measure = ingredient.get('measure')
            ingr.update({'measure': measure})
            name = ingredient.get('ingredient_name')
            total = int(ingredient.get('quantity'))*count
# проверяем  продукт в списке для покупки
# и изменяем количество продукта при наличии
            if name in shop_list.keys():
                s = shop_list.get(name)
                total = total + int(s.get('quantity'))
            ingr.update({'quantity': total})
# Заносим продукт в требуемом количестве в список на покупку
            shop_list.update({name: ingr})
    print(shop_list)
    return

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)


file_list = ['1.txt', '2.txt', '3.txt']
def file_lines(file_name):
    with open(file_name, encoding='utf-8') as file:
        lines = 0
        for line in file:
            lines += 1
        return lines
file_tuples = []
for file_name in file_list:
    t = (file_name, file_lines(file_name))
    file_tuples.append(t)
file_tuples_sorted = sorted(file_tuples, key=lambda x: x[1])
#
with open('result.txt', 'w', encoding='utf-8') as f:
    for item in file_tuples_sorted:
        file_name = item[0]
        lines = str(item[1])
        f.write(file_name + '\n')
        f.write(lines + '\n')
        with open(file_name, encoding='utf-8') as file:
            for line in file:
                f.write(line)
            f.write('\n ')
            f.write('\n ')

