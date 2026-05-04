# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for ind in range(len(prices)):
        revenue.append(prices[ind] * quantities_sold[ind])
    return revenue

def formatted_output (revenue_per_product):
    product_name = sorted (revenue_per_product)
    for int, zn in product_name:
        print (f'{int} has total revenue of ${zn}')
        
revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip (products, revenue))
formatted_output(revenue_per_product)

#print(f"{revenue[0]} has total revenue of ${revenue[1]}")
