products = [
    {"id": 1, "name": "SkyGame", "price": 24},
    {"id": 2, "name": "GalaxyGame", "price": 24},
    {"id": 3, "name": "AdventaireGame", "price": 24},
    {"id": 4, "name": "Cards", "price": 16},
    {"id": 5, "name": "SeeraBoardGame", "price": 32},
]

print("\nthe products:")

for p in products:
    print(f"{p['id']}. {p['name']} - price: {p['price']} sr")

userinput = int(input("\nenter the product number: "))

found = False
for p in products:
    if p["id"] == userinput:
        price_with_tax = round(p["price"] * 1.15)
        print(f"\nyou chose {p['name']} and the price is {price_with_tax} sr")
        found = True
        break

if not found:
    print("\nthe product is not available")
