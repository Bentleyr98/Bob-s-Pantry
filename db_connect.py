#import libraries to run the database
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os


class DB_Connect:
    def __init__(self):
        self.db = None
        self.item = ""
        self.quantity = ""
        self.units = ""


    def initialize_firestore(self):
        """
        Create database connection
        """

        # Setup database
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = "dinerpantry-firebase-adminsdk-zpyu2-bd58d861fb.json"
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
            'projectId': 'dinerpantry',
        })

        # Get reference to database
        self.db = firestore.client()
        


    def add_new_item(self, category):
        self.item = input("Item Name: ")
        self.quantity = int(input("Quantity: "))
        self.units = input("Units: ")

        # Check if it already exists
        result = self.db.collection(category).document(self.item).get()
        if result.exists:
            print("Item already exists.")
            return

        # store details in a dictionary
        data = {"quantity" : self.quantity, 
                "units" : self.units}
        self.db.collection(category).document(self.item).set(data) 

        print(f"{self.item} was added successfully")
        

    def update_qty(self, category):
        self.item = input("Item Name: ")
        self.quantity = int(input("Add Quantity: "))

        result = self.db.collection(category).document(self.item).get()
        if not result.exists:
            print("Invalid Item Name")
            return

        # Convert data read to a dictionary
        data = result.to_dict()

        # Update the dictionary with the new quanity and save to the database
        data["quantity"] += self.quantity
        self.db.collection(category).document(self.item).set(data)

        print(f"{self.item} has been updated.")


    def pull_items(self, category):

        self.item = input("Item Name: ")
        self.quantity = int(input("Use Quantity: "))

        result = self.db.collection(category).document(self.item).get()
        if not result.exists:
            print("Invalid Item Name")
            return

        # Convert data read to a dictionary
        data = result.to_dict()

        # Check for sufficient quantity.
        if self.quantity > data["quantity"]:
            print(f"Not enough stock. Only {data['quantity']} left.")
            return

        # Update the dictionary with the new quanity and then save the 
        # updated dictionary to Firestore.
        data["quantity"] -= self.quantity
        self.db.collection(category).document(self.item).set(data)


    def view_stock(self, category):
        print(f"{category.upper()}: ")
        print()

        results = self.db.collection(category).get()

        print(f"{'Item':<20}  {'Quantity':<10} {'Units':<10}")
        for result in results:
            stock = result.to_dict()
            print(f"{result.id:<20}  {stock['quantity']:<10}  {str(stock['units']):<10}")
        print() 

        

    def order_items(self):
        # Display all the results from any of the queries
        cat1 = "Dairy"
        cat2 = "Dry Goods"
        cat3 = "Fruits"
        cat4 = "Meat"
        cat5 = "Oils"
        cat6 = "Sauces"
        cat7 = "Spices"
        cat8 = 'Vegetables'

        #get results for all of the categories
        results1 = self.db.collection(cat1).get()
        results2 = self.db.collection(cat2).get()
        results3 = self.db.collection(cat3).get()
        results4 = self.db.collection(cat4).get()
        results5 = self.db.collection(cat5).get()
        results6 = self.db.collection(cat6).get()
        results7 = self.db.collection(cat7).get()
        results8 = self.db.collection(cat8).get()

        #check if it's below desired quantity and print to the screen if so
        print("Search Results")
        print(f"{'Category':<20}  {'Item':<20}  {'Quantity':<10}   {'Units':<10}")
        for result in results1:
            stock = result.to_dict()
            if stock['quantity'] < 5:
                print(f"{cat1:<20} {result.id:<20}  {stock['quantity']:<10}  {str(stock['units']):<10}")
        for result in results2:
            stock = result.to_dict()
            if stock['quantity'] < 5:
                print(f"{cat2:<20} {result.id:<20}  {stock['quantity']:<10}  {str(stock['units']):<10}")

        for result in results3:
            stock = result.to_dict()
            if stock['quantity'] < 5:
                print(f"{cat3:<20} {result.id:<20}  {stock['quantity']:<10}  {str(stock['units']):<10}")

        for result in results4:
            stock = result.to_dict()
            if stock['quantity'] < 5:
                print(f"{cat4:<20} {result.id:<20}  {stock['quantity']:<10}  {str(stock['units']):<10}")

        for result in results5:
            stock = result.to_dict()
            if stock['quantity'] < 5:
                print(f"{cat5:<20} {result.id:<20}  {stock['quantity']:<10}  {str(stock['units']):<10}")

        for result in results6:
            stock = result.to_dict()
            if stock['quantity'] < 5:
                print(f"{cat6:<20} {result.id:<20}  {stock['quantity']:<10}  {str(stock['units']):<10}")

        for result in results7:
            stock = result.to_dict()
            if stock['quantity'] < 5:
                print(f"{cat7:<20} {result.id:<20}  {stock['quantity']:<10}  {str(stock['units']):<10}")

        for result in results8:
            stock = result.to_dict()
            if stock['quantity'] < 5:
                print(f"{cat8:<20} {result.id:<20}  {stock['quantity']:<10}  {str(stock['units']):<10}")
        print() 


