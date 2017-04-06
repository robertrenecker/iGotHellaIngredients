#!/usr/bin/python
import json

foodIngredients = {
    "Chicken Soup": ['Chicken', 'Water', 'Noodles', 'Carrots'],
    "Fried Rice": ['Rice', 'Chicken', 'Egg'],
    "Spaghetti": ['Noodles', 'Tomatoes', 'Cheese']
}

def main():
    menuInput = 0
    ingredients = []
    while(menuInput != 3):
        menuInput = input("1. add an item to ingredients \n2. search recipe \n3. quit\n")
        if(menuInput == 1):
            temp = raw_input("enter a item please: ")
            ingredients.append(temp)
        elif(menuInput == 2):
            break
        elif(menuInput == 3):
            exit()

    for key, value in foodIngredients.items():
        for item in value:
            for ing in ingredients:
                if(ing == item):
                    print ing + " is in " + key

if __name__ == '__main__':
    main()
