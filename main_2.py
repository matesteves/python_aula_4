#1 
#list1 = list(range(1, 15))
#list2 = []
#for num in list1:
#    list2.append(num**2)
#print(list2)

#2
#book = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
#
#for key, value in book.items():
#    print(f"{key}: {value}")

#3
#def count():
#    string = str(input("Type your input. "))
#    string.lower().replace(" ", "")
#    characters = {}
#    for i in string:
#        characters[i] = characters.get(i, 0) + 1
#    print(characters)
#
#count()

#4
#items = ["apple", "banana", "grape", "banana"]
#price = {"apple": 0.45, "banana": 0.30, "grape": 0.65}
#
#total_price = 0
#
#for i in items:
#    total_price += price[i]
#print(total_price)
#
#total_price2 = sum(price[i] for i in items)
#print(total_price2)

#5
#emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.#com"]
#unique = list(set(emails))
#print(unique)

#6
#ages = [22, 15, 30, 17, 18]
#over_18 = [i for i in ages if i >=18]
#print(over_18)

#7
#ppl = [
#    {"name": "Alice", "age": 30},
#    {"name": "Bob", "age": 25},
#    {"name": "Carol", "age": 20}
#]
#ppl.sort(key= lambda ppl: ppl["age"])
#print(ppl)

#8
#nums = [10, 20, 30, 40, 50]
#avg = sum(nums)/ len(nums)
#print(avg)

#9
#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#odd = []
#even = []

#for i in nums:
#    if i % 2 == 0:
#        even.append(i)
#    else:
#        odd.append(i)
#odd = [i for i in nums if i % 2 == 0]
#even = [i for i in nums if i % 2 != 0]
#
#print(odd)
#print(even)

#10
#products = [
#    {"id": 1, "name": "Teclado", "price": 100},
#    {"id": 2, "name": "Mouse", "price": 80},
#    {"id": 3, "name": "Monitor", "price": 300}
#]
#id = int(input("What's the id of the item? "))
#
#position = None
#for product in products:
#    if product["id"] == id:
#        position = product
#        break
#
#new_price = float(input("What's the new price for the product? "))
#position["price"] = new_price
#print(products[position])

#12
#dict1 = {"a": 1, "b": 2}
#dict2 = {"c": 3, "d": 4}
#
#combined_dicts = {**dict1, **dict2}
#
#print(combined_dicts)

#13
#items = {"Keyboard": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
#valid_items = [i for i in items if items[i] > 0]
#
#print(valid_items)

#14
#dict = {"a": 1, "b": 2, "c": 3}
#keys = list(dict.keys())
#values = list(dict.values())
#
#print(keys)
#print(values)

#15
#text = "data engineering"
#count = {}
#for i in text:
#    if i in count:
#        count[i] += 1
#    else:
#        count[i] = 1
#print(count)