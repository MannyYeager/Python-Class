inventory = {
    "Tomantoes" : {"Stock": 150, "Price_per_unit": 5.0},
    "Onions" : {"Stock": 80, "Price_per_unit": 3.5},
    "Garden Eggs" : {"Stock": 200, "Price_per_unit": 1.0}
}

while True:
    Item = input("Enter the item you want to buy(Tomantoes, Onions, Garden Eggs) or 'Exit':")
    if Item.capitalize() == 'Exit':
        print("Closing sales. Total transactions completed." )
        break
    if Item in inventory :
        quantity = int(input("Enter quantity you want to buy: "))
        
        if quantity > inventory[Item]["Stock"]:
            print(f"Sorry, only {inventory[Item]['Stock']} units of {Item} remaining." "")
        else:
            cost = quantity * inventory[Item]["Price_per_unit"]
            inventory[Item]["Stock"] -= quantity
            print(f"Sales Succesful! Cost: GHS {round(cost, 2)}")
            print(f"{inventory[Item]["Stock"]} units of {Item} remaining")    
    else:
        print("Item not found in stock. Check spelling.")    