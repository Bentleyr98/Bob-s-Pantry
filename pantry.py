from db_connect import DB_Connect

def main():
    db = DB_Connect()
    #create connection to the database
    db.initialize_firestore()
    print()
    print("---------Bob's Pantry---------")
    category = categories(db)
    if category != None:
        options(category, db)
        


def options(category, db):
    choice = None
    while choice != 0:
        print()
        print(f'Category: {category.upper()}')
        print("0. Exit")
        print("1. Add New Item")
        print("2. Add Stock")
        print("3. Pull from Stock")
        print("4. View Items")
        choice = input(f"> ")
        print()
        if int(choice) == 1:
            db.add_new_item(category)
        elif int(choice) == 2:
            db.update_qty(category)
        elif int(choice) == 3:
            db.pull_items(category)
        elif int(choice) == 4:
            db.view_stock(category)    
        elif int(choice) == 0:
            choice = 0
        else:
            print("Invalid selection.")
             


def categories(db):
    exit = 0

    while exit == 0:
        print('Categories:')
        print('1. Dairy')
        print('2. Dry Goods')
        print('3. Fruits')
        print('4. Meat')
        print('5. Oils')
        print('6. Sauces')
        print('7. Spices')
        print('8. Vegetables')
        print('9. Restock')
        print('0. Exit')
        select = int(input(f"> "))

        if select == 1:
            category = 'Dairy'
            exit = 1
        elif select == 2:
            category = 'Dry Goods'
            exit = 1
        elif select == 3:
            category = 'Fruits'
            exit = 1
        elif select == 4:
            category = 'Meat'
            exit = 1
        elif select == 5:
            category = 'Oils'
            exit = 1
        elif select == 6:
            category = 'Sauces'
            exit = 1
        elif select == 7:
            category = 'Spices'
            exit = 1
        elif select == 8:
            category = 'Vegetables'
            exit = 1
        elif select == 9:
            category = None
            db.order_items()  

        elif select == 0:
            print("Exiting...")
            return

        else:
            print('Wrong selection. Please enter the number associated with your choice.')
        return category


if __name__ == "__main__":
    main()
