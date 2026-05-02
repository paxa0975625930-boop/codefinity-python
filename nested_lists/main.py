vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove('onions')
if not ("carrots" in vegetables):
    vegetables.append('carrots')
if not ("cucumbers" in vegetables):
    vegetables.append('cucumbers')
vegetables.sort()
print (f"Updated Vegetable Inventory: {vegetables}")
if "carrots" in vegetables:
    print ("Carrots are already in the list.")
if "cucumbers" in vegetables:
    print ("Cucumbers are already in the list.")
