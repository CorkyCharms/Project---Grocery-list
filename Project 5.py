def main(superList):
    countList = int(input("How many items will be on your grocery list: "))

    for i in range(countList):
        print(countList)
        addItem = input("Enter the item you would like to add: ")
        superList.append(addItem)
        print(addItem)
        x = len(addItem)
        print(x)
        
def moreItems():
    userAdd = str(input("Would you like to add another item: "))
    if userAdd == 'yes':
        addMore = input("Add another item: ")
        newList.append(addMore)
        print("Here is your updated grocery list: ", newList)
        moreItems()
    else:
        pass

def deleteItems():
    userAdd = str(input("Remove an item from the grocery list: "))
    if userAdd == 'yes':
        deleteItem = input("What would you like to remove from the grocery list: ")
        newList.remove(deleteItem)
        print("Updated grocery list: ", newList)
        deleteItems()
    else:
        pass
        

def sortItems(newList):
    userAdd = str(input("Would you like to sort the items in your grocery list in reverse order?: "))
    if userAdd == 'yes':
        newList.sort(reverse=True)
        print("This is your sorted grocery list: ", newList)
    else:
        pass        

newList = []
main(newList)
print(newList)
moreItems()
deleteItems()
sortItems(newList)

