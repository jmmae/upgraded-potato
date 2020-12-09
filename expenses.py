itemList = []

class Item: #class of an item. contains relevant getter / setter methods
    def __init__(self, description, category, amount, price):
        self.description = description
        self.category = category 
        self.amount = amount 
        self.price = price

    def get_description(self):
        return self.description

    def get_category(self):
        return self.category

    def get_amount(self):
        return self.amount
    
    def get_price(self):
        return self.price

    def set_description(self, description):
        self.description = description

    def set_category(self, category):
        self.category = category

    def set_amount(self, amount):
        self.amount = amount
    
    def set_price (self, price):
        self.price
        
def createObject():  #uh creates the object
    newItem = str(input("Enter the name of the product: "))
    newDescription = str(input("Enter description of product: "))
    newCategory = str(input("Enter category of product: "))
    newAmount = int(input("Enter amount of product: "))
    newPrice = int(input("Enter price of product: "))
    itemList.append(Item(newDescription,newCategory,newAmount,newPrice))
    print("The itemList is now", itemList)
    
def deleteObject(): #deletes the object 
    print("There are", len(itemList), "item(s) in the itemList.")
    toDelete = int(input("Enter the number of the product to be deleted"))
    toDelete = toDelete - 1 
    del itemList[toDelete] #making something inaccessible is totally the same thing as deleting it
    print("There are", len(itemList), "item(s) in the itemList.")

def editMode(): #lets you chose between adding / deleting an object
    while True:
        print("Choose between:")
        print("1. createObject ")
        print("2. deleteObject ")
        print("3. Exit to menu screen")
        userInp = int(input("Please enter your choice: "))
        if userInp == 1:
            createObject()
        if userInp == 2:
            deleteObject()
        elif userInp == 3: 
            break

def categorySpend(): #finds the total spending of items in a given category
    totalSpend = 0
    findCat = str(input("Please enter what category you want to find the total spend of: "))
    for obj in itemList:
        if obj.get_category() == findCat: 
            totalSpend = totalSpend + (obj.get_amount() * obj.get_price())
        else: 
            pass
    print("The total cost of items of category", findCat, "is", totalSpend)
            
            
        
        

def averageSpend(): #finds the total spending on items, then divide by types of item. 
    totalSpend = 0
    for obj in itemList:
        totalSpend = totalSpend + (obj.get_amount() * obj.get_price())  
    print ("The total cost is", (totalSpend/len(itemList))) 
        

def totalSpend(): #finds total spending on items. 
    totalSpend = 0
    for obj in itemList: 
        totalSpend = totalSpend + (obj.get_amount() * obj.get_price())    
    print ("The total cost is", totalSpend)

def analysisMode(): # a menu that lets the users choose between relevant functions. 
    while True:
        print("Choose between:")
        print("1. categorySpend ")
        print("2. averageSpend ")
        print("3. totalSpend")
        print("4. Exit to menu screen")
        userInp = int(input("Please enter your choice: "))
        if userInp == 1:
            categorySpend()
        if userInp == 2:
            averageSpend()
        if userInp == 3:
            totalSpend()
        elif userInp == 4: 
            break    


while True: #a menu that lets users choose between relevant functions. 
    print("Choose between:")
    print("1. Edit Mode")
    print("2. Analysis Mode")
    print("3. Exit")
    userInp = int(input("Please enter your choice: "))
    if userInp == 1:
        editMode()
    elif userInp == 2:
        analysisMode()
    elif userInp == 3:
        print("Bye!")
        break





    
