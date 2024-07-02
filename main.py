queue = []
entry_start = "Customer Electric Billing System" \
"\n\nEnter the choice of the menu selection\n '1' Enter the consumer's name " \
"\n '2' to see the consumer list" \
" \n '3' to find a consumer by name \n '4' show Consumer Info \n '5' show Receipt \n '6' to quit: "\

#This method adds the consumer
def add_customer():
    name = input("Enter the name of consumer: ")
    month = input("Enter the Month: ")
    kilowatt = int(input("Enter your kilowatt: "))
    bill= (kilowatt*18)
    queue.append({
        'name': name,
        'month': month,
        'kilowatt': kilowatt,
        'bill': bill,
    })
#This method shows the 1st inputted consumer
def customer_list():
    quantity = len(queue)
    cusname = [x['name'] for x in queue]
    cusname = ', '.join(cusname)

    if quantity:
        print(f'Here is the Consumer List: {cusname}. In total you have {quantity} {"Consumer" if quantity == 1 else "Consumers"}.')
    else:
        print('There are no Consumer')

#This method shows the 1st inputted consumer's information
def print_customer_info(x):
    print('Here is information about the Consumer')
    print(f'Name: {x["name"]}')
    print(f'Month: {x["month"]}')
    print(f'Kilowatt: {x["kilowatt"]}')
    print(f'Your Bill: P{x["bill"]}')

#This method looks for the 1st inputted consumer and its corresponding information
def find_name():
    search_name = input('Enter the name you are looking for: ')
    for x in queue:
        if x['name'] == search_name:
            print_customer_info(x)
        elif x['name'] != search_name:
            print("Consumer is not found")
        else:
            menu()
#This gets the inputted consumer's information
def getinfo():
    print("Consumer's Information:", queue[0])
#This method shows that the consumer paid the bill
def payment():
    print("Succesfully Paid")
    queue.pop(0)
#This method checks if the consumer can be found or not in the queue
def is_empty():
    if not queue:
        print("Consumer is not found.")
    else:
        getinfo(),payment()

user_selection = {
    '1': add_customer,
    '2': customer_list,
    '3': find_name,
    '4': getinfo,
    '5': is_empty
}

#This method is for the menu
def menu():
    selection = input(entry_start)
    while selection != '6':
        if selection in user_selection:
            selected_action = user_selection[selection]
            selected_action()
        else:
            print("Unknown command. Please choose within available options: '1', '2', '3', '4', '5' or '6' to close the app.")
        selection = input(entry_start)
    print('Thank you and see you again!')


if __name__ == '__main__':
    menu()