#!/usr/bin/python
import json
import unittest

class AlphaTest(unittest.TestCase):
    def test_1(self):
        ingredients = ['Egg']
        self.assertEqual(search(ingredients), "Egg is in Fried Rice")
    def test_2(self):
        ingredients = ['Noodles', 'Chicken']
        self.assertEqual(search(ingredients), "Chicken is in Chicken Soup")

foodIngredients = {
    "Chicken Soup": ['Chicken', 'Water', 'Noodles', 'Carrots'],
    "Fried Rice": ['Rice', 'Chicken', 'Egg'],
    "Spaghetti": ['Noodles', 'Tomatoes', 'Cheese']
}

def search(ingredients):
        for key, value in foodIngredients.items():
            for item in value:
                for ing in ingredients:
                    if(ing == item):
                        return ing + " is in " + key

def main():
    menuInput = 0
    ingredients = []
    while(menuInput != 3):
        menuInput = input("1. add an item to ingredients \n2. search recipe \n3. quit\n")
        if(menuInput == 1):
            temp = raw_input("enter a item please: ")
            ingredients.append(temp)
        elif(menuInput == 2):
            search(ingredients)
        elif(menuInput == 3):
            exit()

if __name__ == '__main__':
    unittest.main()
