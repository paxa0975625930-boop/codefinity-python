# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"
if product_type == 'Perishable':
    if stock_level > 50:
        if days_until_expiration <= 3:
            print ('30% discount applied')
        if days_until_expiration >=4 and days_until_expiration <= 6:
            print ("20% discount applied")
    elif stock_level<=50: 
        if days_until_expiration > 6:
            print ("10% discount applied")
else:
    print ("No discount available for non-perishable items.")





