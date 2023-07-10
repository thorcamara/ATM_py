print('=' * 30)
print('{:^40}'.format('\033[4;33mBANK ATM\033[m'))
print('=' * 30)
amount = int(input('What amount do you want to withdraw? $ '))
total = amount
bill = 50
totalBills = 0
while True:
    if total >= bill:
        total -= bill
        totalBills += 1
    else:
        if totalBills > 0:
            print(f'Total of \033[4;32m{totalBills}\033[m bills of \033[4;32m${bill}\033[m')
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        totalBills = 0
        if total == 0:
            break
print('=' * 30)
print('Thank you! Have a great day!')