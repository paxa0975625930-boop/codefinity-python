prices = [29.99, 45.50, 12.75, 38.20]
for ind in range(len(prices)):
    if ind == 0:
        prices[ind] -= prices[ind] * 0.1
    if ind == 1:
        prices[ind] -= prices[ind] * 0.2
    if ind == 2:
        prices[ind] -= prices[ind] * 0.15
    if ind == 3:
        prices[ind] -= prices[ind] * 0.05
    print (f'Updated price for item {ind+1} : ${prices[ind]:.2f}')


