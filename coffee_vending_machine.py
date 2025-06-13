menu = { #Dictionary for coffee menu
    'Espresso': 50.25,
    'Caramel Latte': 125.0,
    'Cappuccino': 200.75
} # for another function
ingredients = {
    'Water':1000, #100ml per cup of coffee
    'Milk': 1000, #50ml per cup of coffee
    'Coffee': 1000 #76 grams per cup of coffee
}
#created by John Lexter Reyes
def process():
    lines()
    print('Coffee Menu')
    lines()
    print('[1] Espresso\nPrice: 50.25')
    lines()
    print('[2] Caramel Latte\nPrice: 125.0')
    lines()
    print('[3] Cappuccino\nPrice: 200.75')
    lines()
def transaction_success(coffee,cash):
    print(f'Total: {menu[coffee]}')
    print(f'Cash: {cash}')
    lines()
    print(f'Change: {cash - menu[coffee]}')
    return 'Your latte is ready!'
def transaction_failure():
    return 'Sorry thats not enough money. Money refunded'
def coins_count():
    print("Please insert coins")
    bente = float(input('Number of 20 pesos coins: '))
    sampu = float(input('Number of 10 pesos coins: '))
    lima = float(input('Number of 5 pesos coins: '))
    isa = float(input('Number of 1 peso coins: '))
    centavo = float(input('Number of 25 centavos coins: '))

    total = (bente * 20) + (sampu * 10) + (lima * 5) + (isa * 1) + (centavo * 0.25)
    return total
def database_check():
    print('Checking database...')
def loop_trigger():
    choice = input('Do you want to order again? (yes/no): ')
    if choice.lower() == 'yes':
        return True
    else:
        print('Shutting down the coffee machine!')
        return False
def lines():
    print('--------------------------------')
loop = True

while loop:
    process()
    choice = input('Please select a coffee: ')
    if choice == '1':
        print('You selected Espresso')
        print(f'{menu["Espresso"]} pesos')
        coins = coins_count()
        if coins >= menu['Espresso']:
            print(transaction_success('Espresso', coins))
        else:
            print(transaction_failure())
    elif choice == '2':
        print('You selected Caramel Latte')
        print(f'{menu["Caramel Latte"]} pesos')
        coins = coins_count()
        if coins >= menu['Caramel Latte']:
            print(transaction_success('Caramel Latte', coins))
        else:
            print(transaction_failure())
    elif choice == '3':
        print('You selected Cappuccino')
        print(f'{menu["Cappuccino"]} pesos')
        coins = coins_count()
        if coins >= menu['Cappuccino']:
            print(transaction_success('Cappuccino', coins))
        else:
            print(transaction_failure())
    
    loop = loop_trigger()

#will create a way to make these efficient by putting the data in a separate file and importing it
 
   