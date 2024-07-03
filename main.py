queue = []
entry_start = "**** Welcome to 123Cinema ****\n***** Movie ticket price: 400 ****" \
"\n\nEnter the choice of the menu selection\n '1' Enter the name of the customer, " \
"\n '2' to see the customer list," \
" \n '3' to find a customer by name, \n '4' First Customer Pay\n or '5' to quit: "\


def add_customer():#add details
    name = input("Enter the name of customer: ")
    movie = input("Enter movie name:")
    snacks = input("Enter the snack: ")
    psnacks = int(input("Enter the price of the snack:"))
    drinks = input("Enter the drinks: ")
    pdrinks = int(input("Enter the price of the drinks:"))
    global total    #Global variable
    total = (psnacks + pdrinks + 400)
    queue.append({  #insert elements
        'name': name,
        'snacks': snacks,
        'drinks': drinks,
        'movie': movie,
        'total': total,
        'psnacks': psnacks,
        'pdrinks': pdrinks,

    })

def customer_list():    #List of the number of customers
    quantity = len(queue)   #length og queue
    names = [xyz['name'] for xyz in queue] #Names value will be the names inputted
    names = ', '.join(names)    #join method takes all items in an iterable and joins them into one string.

    if quantity:
        print(f'Here is the customer List: {names}. In total you have {quantity} {"Customer" if quantity == 1 else "Customers"}.')
    else:
        print('There are no Customers')


def print_customer_info(xyz):#info about the customer
    print('Here is information about the Customer')
    print(f'Name: {xyz["name"]},')
    print(f'Movie: {xyz["movie"]},')
    print(f'Snack: {xyz["snacks"]},')
    print(f'Snack Price: {xyz["psnacks"]},')
    print(f'Drinks: {xyz["drinks"]},')
    print(f'Drinks Price: {xyz["pdrinks"]},')
    print(f'Total: {xyz["total"]},')


def find_name():    #search for the name of customer
    search_name = input('Enter the name you are looking for: ')
    for xyz in queue: #for loop
        if xyz['name'] == search_name:

            print_customer_info(xyz)#call print_customer_info method
        else:
            print('Name not Found')


def getorder():#dequeue the first customer since this is a queue
            print("The total bill is: ",total)
            pay = int(input("Customer Payment: "))
            change = pay - total
            print("Change: ",change)
            print("Succesfully paid")
            print("Receipt: ")
            print(queue[0],"payment: ",pay,"change: ",change)
            queue.pop(0)    #dequeue the first element


def order():
        if not queue: #boolean
            print("Customer List is empty")
        else:

            getorder()

user_selection = { # What the user has selected
    '1': add_customer,
    '2': customer_list,
    '3': find_name,
    '4': order,

}

def menu():#this is the menu
    selection = input(entry_start).lower()
    while selection != '5': #while loop
        if selection in user_selection:
            selected_action = user_selection[selection]
            selected_action()
        else:
            print("Unknown command. Please choose within available options: '1', '2', '3', '4' or '5' to close the app.")
        selection = input(entry_start)



if __name__ == '__main__':
    menu()

