

def profit_or_loss(cost_price, selling_price):
    diff = selling_price - cost_price
    if diff > 0:
        print(f'we have profit of: {abs(diff)}')
    elif diff < 0:
        print(f'we have loss of: {abs(diff)}')
    else:
        print('selling price is same as cost price')


if __name__ == '__main__':
    cost_p = int(input(f'Enter cost price: '))
    selling_p = int(input(f'Enter selling price: '))
    profit_or_loss(cost_p, selling_p)
