class Item: 
    def __init__(self, description, category, amount):
        self.description = description
        self.category = category 
        self.amount = amount 

    def get_description(self):
        return self.description

    def get_category(self):
        return self.category

    def get_amount(self):
        return self.amount

    def set_description(self, description):
        self.description = description

    def set_category(self, category):
        self.category = category

    def set_amount(self, amount):
        self.amount = amount


print("Choose between:")
print("1. Edit Mode")
print("2. Analysis Mode")
print("3. Exit")
userInp = int(input("Please enter your choice: "))

while True:
    if userInp == 1:
        editMode()
    elif userInp == 2:
        analysisMode()
    elif userInp == 3:
        print("Bye!")
        break

def editMode():
    pass

def analysisMode():
    pass




    
