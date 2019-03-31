import time
import requests
from bs4 import BeautifulSoup

def ingredient_scrape():

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ingredients = []

    for letter in alphabet:
        time.sleep(5)
        page = requests.get("http://www.bbc.co.uk/food/ingredients/by/letter/" + letter)
        soup = BeautifulSoup(page.content, 'lxml')

        pre_ingredient_list = soup.findAll('li', {'class': 'resource food'})
        for ingredient_list in pre_ingredient_list:
            ingredient = ingredient_list.get("id")
            ingredients.append(ingredient)
            print(ingredient)

    with open("ingredient_list.txt", "a", encoding="utf-8") as ingredient_list_document:

        for ingredient in ingredients:
            ingredient_list_document.write(ingredient)
            ingredient_list_document.write("\n")

ingredient_scrape()







