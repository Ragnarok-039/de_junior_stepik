purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

total_revenue = 0
category = {}
min_price = min(i['price'] for i in purchases)
list_min_price = []
average_price_by_category = {}
most_frequent_category = {}

for now in purchases:
    add_sum = now['price'] * now['quantity']
    total_revenue += add_sum
    category[now['category']] = category.get(now['category'], []) + [now['item']]
    average_price_by_category[now['category']] = average_price_by_category.get(now['category'], []) + [now['price']]
    most_frequent_category[now['category']] = most_frequent_category.get(now['category'], []) + [now['quantity']]
    if now['price'] >= min_price:
        min_price = now['price']
        list_min_price.append(now)

for now in average_price_by_category:
    average_price_by_category[now] = sum(average_price_by_category[now]) / len(average_price_by_category[now])

for now in most_frequent_category:
    most_frequent_category[now] = sum(most_frequent_category[now])

print(f'Общая выручка: {total_revenue}')
print(f'Товары по категориям: {category}')
print(f'Покупки дороже {min_price}: {list_min_price}')
print(f'Средняя цена по категориям: {average_price_by_category}')
print(f'Категория с наибольшим количеством проданных товаров: {max(most_frequent_category, key=lambda x:most_frequent_category[x])}')
