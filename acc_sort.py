import json
from item import Item

items = []
with open('ear.txt', 'r', encoding='utf-8') as f:
    items = [Item.from_dict(i) for i in json.loads(f.read())]

for item in sorted(items, reverse=True):
    if item.get_total_option_grade() < 5:
        continue
    if item.price > 30000:
        continue
    print(item)