# <--Modules Section--> #
from pyfiglet import Figlet
from tabulate import tabulate

# <--Global Variables Section--> #
logo = Figlet(font = 'isometric3')
logo = logo.renderText('Kyloz\nKickz')
greeting = Figlet(font = 'larry3d')
greeting = greeting.renderText('Bye Bye!')
menu_header = f'''+{'=' * 66}+\n|:{' ' * 20}Kylo'z Kickz - Main Menu{' ' * 20}:|\n+{'=' * 66}+'''
menu_header += f'''\n| "cap"\t\t-  Capture New Shoe Item{' ' * 27}|'''
menu_header += f'''\n| "vas"\t\t-  View All Shoes{' ' * 34}|'''
menu_header += f'''\n| "res"\t\t-  Replenish Low Stock{' ' * 29}|'''
menu_header += f'''\n| "ss"\t\t-  Shoe Search{' ' * 37}|'''
menu_header += f'''\n| "vsv"\t\t-  View Stock Values{' ' * 31}|'''
menu_header += f'''\n| "ios"\t\t-  Items on Sale{' ' * 35}|'''
menu_header += f'''\n| "e"\t\t-  Exit{' ' * 44}|\n+{'=' * 66}+'''

# <--Classes Section--> #
class Shoes():
    '''Shoes class initialises and contains the Shoes objects

    Args:
        country (str)   :   Country the object is in.
        code (complex)  :   Unique object Identifyer(SKUxxxxx)
        product (str)   :   Object Name
        cost (int)      :   Price representation of the object
        quantity (int)  :   Number of objects on hand

    '''
    def __init__(self, country:str, code:str, product:str, cost:str, quantity:str):
        '''Creates an instance of the Shoe object.'''

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''Returns the cost parameter of the object of class Shoes'''

        return self.cost

    def get_quantity(self):
        '''Returns the quantity parameter of the object of class Shoes .'''

        return self.quantity

    def __str__(self):
        '''Str representation of the Shoes class'''

        return f'''{self.country}\n{self.code}\n{self.product}\n{self.cost}\n{self.quantity}'''

# <--Functions Section--> #
def read_shoes_data(shoe_list):
    '''
    Reads in the raw data from file and initialises the Shoes objects from the data.

    Parameters (emptylist)  :   Initialised objects are appended to the list.

    Returns (object list)    :  A list of initialised objects.
    '''
    # Read in shoe data from file.
    with open('inventory.txt', 'r', encoding='utf-8') as shoe_data:
        shoe_data = [(item.rstrip('\n')).split(',') for item in shoe_data]

    # Iterate over data and assign values to parameter variables. Initialise
    # objects with variables and append to list.
    row_len = len(shoe_data)
    for row in range(row_len):

        col_len = len(shoe_data[row])
        for col in range(col_len):

            try:

                if row == 0:

                    country = shoe_data[row][col]
                    code = shoe_data[row][col + 1]
                    product = shoe_data[row][col + 2]
                    cost = shoe_data[row][col + 3]
                    quantity = shoe_data[row][col + 4]
                    new_shoe_obj = Shoes(country,code,product,cost,quantity)
                    shoe_list.append(new_shoe_obj)

                else:

                    country = shoe_data[row][col]
                    code = shoe_data[row][col + 1]
                    product = shoe_data[row][col + 2]
                    cost = shoe_data[row][col + 3]
                    quantity = shoe_data[row][col + 4]
                    new_shoe_obj = Shoes(country, code, product, cost, quantity)
                    shoe_list.append(new_shoe_obj)

            except IndexError:

                break

def capture_shoes(shoe_list):
    '''
    Captures new object paremeters as inputs.Initialises and appends new object to list.

    Parameters (object list)    :   Represents the old object list version.

    Returns (object list)       :   Returns updated version of object the list.
    '''
    count = 0
    file_str = ''

    # Loop that handles user inputs, initialises captured objects and appends objects to list
    while True:

        try:

            country = input('\n|: Country\t\t=> ').title()
            code = input('\n|: Code(SKUxxxxx)\t=> SKU')
            if len(code) != 5:

                raise ValueError

            code = 'SKU' + code
            product = input('\n|: Product\t\t=> ')
            cost =  input('\n|: Cost\t\t\t=> ')
            if len(cost) > 4:

                raise ValueError

            quantity = input('\n|: Quantity\t\t=> ')
            if len(quantity) > 2:

                raise ValueError

            add_more = input('\n  Add More shoes(y/n)? ').lower()
            print(f"+{'-' * 66}+")
            if add_more == 'y':

                shoe_obj = Shoes(country, code, product, cost, quantity)
                shoe_list.append(shoe_obj)

            elif add_more == 'n':

                shoe_obj = Shoes(country, code, product, cost, quantity)
                shoe_list.append(shoe_obj)
                break

            else:
                raise ValueError

        except ValueError:

            print('\n[Err-CAPin] Please check input and try again!!')
            break

    # Loop that creates string version of objects.
    while True:

        try:
            file_str += f"{shoe_list[count].country},"
            file_str += f"{shoe_list[count].code},"
            file_str += f"{shoe_list[count].product},"
            file_str += f"{shoe_list[count].cost},"
            file_str += f"{shoe_list[count].quantity}\n"
            count += 1

        except IndexError:

            break

    # Writes strings to file, returns shoe object list.
    file_data = open('inventory.txt', 'w', encoding='utf-8')
    file_data.write(file_str.rstrip('\n'))
    file_data.close()
    print('  Shoe Object added successfully!')
    return shoe_list

def view_all(shoe_list):
    '''
    Displays all of the objects on screen in a tabulated format.

    Parameters (object list)    -   String version of objects read in from list.

    Returns (none)              -   Data is displayed to screen.
    '''
    # Data is read in from shoe object list.
    table_data = [str(item).split('\n') for item in shoe_list]

    # Tabulated Data is displayed to screen
    print(tabulate(table_data, headers = 'firstrow' , tablefmt='pretty'))
    input('\nAny key to continue...')

def re_stock(shoe_list):
    '''
    Displays object with the lowest quantity value and updates the value via user input.

    Parameters (object list)    :   Quantity values are read in from the list.

    Returns (none)              :   Updated object list is written to file.
    '''
    lowest_qty_list = []
    count = 0

    # Convert objects to str lists
    shoe_lists = [str(item).split('\n') for item in shoe_list]

    # Fetch quantity values from objects
    quantity = [item.get_quantity() for item in shoe_list if 'Quantity' not in item.get_quantity()]

    # Convert quantity str values to ints, sort values, slice lowest value, convert back to str.
    lowest = str(sorted([int(item) for item in quantity])[0])

    # Use lowest value to filter out lowest quantity object indexes
    lowest_list_objs = [shoe_lists.index(item) for item in shoe_lists if lowest in item]

    # Using object indexes add lowest quantity objects to new list.
    while count < len(lowest_list_objs):

        if len(lowest_list_objs) > 1:

            lowest_list_objs[count] =  shoe_list[lowest_list_objs[count]]

        elif len(lowest_list_objs) == 1:

            lowest_list_objs[count] = shoe_list[lowest_list_objs[count]]

        count += 1

    # Convert objects to string instances.
    lowest_qty_list = [str(item).split('\n') for item in lowest_list_objs]

    # Tabulate data
    headers = [' Country ', ' Code ',' Product ',' Cost ','Low on Stock!']
    print(tabulate(lowest_qty_list, headers, tablefmt='pretty'))

    # Loop to handle user replenish stock input.
    while True:

        try:
            print(f"+{'-' * 66}+")
            print(f'''{' ' * 9}<==> Would you like to replenish stock (y/n)? <==>''')
            print(f"+{'-' * 66}+")
            replenish_bool = input(': ')
            print(f"+{'-' * 66}+")

            if replenish_bool == 'y':
                print(f'''{' ' * 17}<==> Number of units to order <==>\n+{'-' * 66}+''')
                order_num= int(input(': '))
                print(f"+{'-' * 66}+")
                order_num = str(order_num + int(lowest))
                break

            if replenish_bool == 'n':

                return

            raise TypeError

        except TypeError:

            print('[ERR] Please check input and try again!!')

        count += 1

    # Loop to update quantity values at the object level
    count = 0
    while count < len(lowest_list_objs):

        try:

            lowest_list_objs[count].quantity = order_num  # type: ignore
            count += 1

        except IndexError:

            break

    print(f"{' ' * 13}<==> Inventory successfully updated!! <==>")

    # Updating shoe_list string list  and tabulate
    shoe_lists = [str(item).split('\n') for item in shoe_list]
    input('\nAny key to continue...')

    # Creating string file from object list
    count = 0
    shoe_obj_str = ''
    while True:

        try:

            country = shoe_lists[count][0]
            code = shoe_lists[count][1]
            product = shoe_lists[count][2]
            cost = shoe_lists[count][3]
            quantity = shoe_lists[count][4]
            shoe_obj_str += f'{country},{code},{product},{cost},{quantity}\n'
            count += 1

        except IndexError:

            break

    # Writing string file to output file
    file_data = open('inventory.txt', 'w', encoding = 'utf-8')
    file_data.write(shoe_obj_str.rstrip('\n'))
    file_data.close()

def search_shoe(shoe_list):
    '''
    Searches for objects in the list using its object code parameter taken in as an input.

    Parameters (object list)    -   Object search is conducted against objects in the list.

    Returns (str object)        -   String version of object is returned for printing.
    '''

    print(f'''+{'=' * 28}+\n|:{' ' * 7}Kicks Search{' ' * 7}:|''')
    print(f'''| Search Kicks by SKU number |\n+{'=' * 28}+''')
    user_search = f"SKU{input('  >--> SKU')}"
    print(f"+{'-' * 28}+")
    search_result = [str(item).split('\n') for item in shoe_list]
    search_result = [item for item in search_result if user_search in item]
    headers = str(shoe_list[0]).split('\n')
    print(f"{' ' * 4}>=> Search Results <=<")
    print(tabulate(search_result, headers, tablefmt='pretty'))
    input('\nAny key to continue...')
    return search_result

def value_per_item(shoe_list):
    ''''
    Calculates the value of value of shoe objects using quantity and cost values.

    Parameters (object list)    -   Cost and quantity values are taken in from objects in the list.

    Returns (none)
    '''
    count = 0
    value_list = []

    # Quantity and Cost values taken from objects in the list
    shoe_str_list = [str(item).split('\n') for item in shoe_list]
    shoe_obj = [item.pop(3) for item in shoe_str_list]
    cost_list = [int(item) for item in shoe_obj if item != 'Cost']
    shoe_obj = [item.pop(3) for item in shoe_str_list]
    qty_list = [int(item )for item in shoe_obj if item != 'Quantity']

    # Loop calculates the values of each object in the list and appends to empty list
    while True:

        try:

            cost = cost_list[count]
            qty = qty_list[count]
            value = cost * qty
            value_list.append(f'{value}')
            count += 1

        except IndexError:

            break

    value_list.insert(0, 'Cost x Quantity\n   =   \nValue')

    # Loop that appends the value of each object in the value list to the string
    # versioned list of objects
    count = 0
    while True:

        try:

            shoe_str_list[count].append(value_list[count])
            count += 1

        except IndexError:

            break

    # Tabulate and display data
    headers = 'firstrow'
    print(f"{' ' * 15}<==> Total Value of stock on hand <==>")
    print(tabulate(shoe_str_list, headers, tablefmt='pretty'))
    input('\nAny key to continue...')


def highest_qty(shoe_list):
    '''
    Finds the object with the highest Quantity value and displays to screen.

    Parameters (object list)    -   Quantity values is taken from the object list.

    Returns (none)
    '''
    # Convert objects to str lists
    shoe_lists = [str(item).split('\n')for item in shoe_list]

    # Fetch quantity values from objects and sort items
    table_quantity = [item.get_quantity() for item in shoe_list]
    table_quantity = sorted([int(item) for item in table_quantity if 'Quantity' not in item])

    # slice last value in list which equates to higest num andconvert back to str.
    highest = str(table_quantity[-1])

    # Use highest value to filter out highest quantity objects
    highest_list_objs = [item for item in shoe_lists if item[4] == highest]

    # Tabulate data
    print(f"{' ' * 16}<==> Shoe Is Currently On Sale! <==>")
    headers = [' Country ', '  Code  ','  Product  ','  Cost  ',' Units on sale! ']
    print(tabulate(highest_list_objs, headers, tablefmt='pretty'))
    input('\nAny key to continue...')

def main():
    '''Hosts Menu Interface and all subsequent function calls.'''
    shoe_list = []

    # Initialise data read in and object creation
    read_shoes_data(shoe_list)

    # Loop that nests menu interface and function calls based on user input.
    while True:

        print(logo)
        print(menu_header)
        try:

            menu = input('  >--> ')
            print(f"+{'=' * 66}+")

            if menu == 'cap':

                capture_shoes(shoe_list)

            elif menu == 'vas':

                view_all(shoe_list)

            elif menu == 'res':

                re_stock(shoe_list)

            elif menu == 'ss':

                search_shoe(shoe_list)

            elif menu == 'vsv':

                value_per_item(shoe_list)

            elif menu == 'ios':

                highest_qty(shoe_list)

            elif menu == 'e':

                print(greeting)
                exit()

            else:

                raise ValueError

        except ValueError:
            pass

main()