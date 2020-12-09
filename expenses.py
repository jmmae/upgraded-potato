itemList = []

class Item: 
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
        
def createObject(): 
    newItem = str(input("Enter the name of the product: "))
    itemList.append(newItem)
    newDescription = str(input("Enter description of product: "))
    itemList.append(newDescription)
    newCategory = str(input("Enter category of product: "))
    itemList.append(newCategory)
    newAmount = int(input("Enter amount of product: "))
    itemList.append(newAmount)
    newPrice = int(input("Enter price of product: "))
    itemList.append(newPrice)
    newItem = Item(newDescription,newCategory,newAmount,newPrice)
    print("The itemList is now", itemList)
    

def deleteObject(delete):
    itemList.remove(delete) #making something inaccessible is totally the same thing as deleting it
    print("The itemList is now", itemList)

def editMode():
    while True:
        print("Choose between:")
        print("1. createObject ")
        print("2. deleteObject ")
        print("3. Exit to menu screen")
        userInp = int(input("Please enter your choice: "))
        if userInp == 1:
            createObject()
        if userInp == 2:
            toDelete = str(input("Enter the name of the product to be deleted: "))
            deleteObject(toDelete)
        elif userInp == 3: 
            print("Bye!")
            SystemExit
            break
    

#find total costs of objects
#analysis
#average total spend


def categorySpend():
    print("Test")
def averageSpend():
    return newPrice / newAmount
def totalSpend():
    //print 


def analysisMode():
    while True:
        print("Choose between:")
        print("1. categorySpend ")
        print("2. averageSpend ")
        print("3. totalSpend")
        print("4. Exit to menu screen")
        userInp = int(input("Please enter your choice: "))
        if userInp == 1:
            categorySpend()
        elif userInp == 2:
            averageSpend()
        elif userInp == 3:
            totalSpend()
        elif userInp == 4:
            print("Bye!")
            menu()
            break
    

def menu():
    while True:
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


menu()


    #comment
    
    
