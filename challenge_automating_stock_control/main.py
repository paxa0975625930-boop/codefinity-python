# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}
discount_threshold = 100
print('Processing started')
for inv in inventory:
    print ('Processing',inv)
    data = inventory[inv]
    while data[0] < data[1]:
        data[0] += data[2]
    if data[0] > discount_threshold and data[3] == False:
        data[3] = True
    inventory.update({inv:data})


print ('Processing completed')
    


