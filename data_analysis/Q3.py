import json

fruit_group = dict()

apple = dict()
apple["price"] = "1000"
apple["date"] = "2023-2-5"
fruit_group["apple"] = apple

banana = dict()
banana["price"] = "3000"
banana["date"] = "2023-3-12"
fruit_group["banana"] = banana

with open('Q3.json', 'w') as f:
    json.dump(fruit_group, f)

with open('Q3.json') as f:
    Q3 = json.load(f)
type(Q3)

print(Q3)