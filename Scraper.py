from lxml import html
import requests
from bs4 import BeautifulSoup
import urllib
import time

def pre_url_scrape():
    url_homepage = "https://www.bbc.co.uk/food/recipes"
    page = requests.get(url_homepage)
    soup = BeautifulSoup(page.content, 'lxml')

    pre_things = []
    urls = soup.findAll('a', {'class': 'favourite-dishes__title-link'})
    for url in urls:
        ur = url.get("href")
        pre_things.append(ur)

    other_urls = soup.findAll('a', {'class': 'recipe-collections__title-link'})
    for url in other_urls:
        ur = url.get("href")
        pre_things.append(ur)

    return pre_things

def url_scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    #print(soup.prettify())

    food_things = []
    for links in soup.findAll('h4'):
        links = links.find("a")
        if links is not None:
            link = links.get("href")
            food_things.append(link)

    return food_things

def ingredient_scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    #print(soup.prettify())

    ingredient_fulls = soup.findAll('li', {'itemprop': "ingredients"})

    ingredient_types = soup.findAll('a', 'recipe-ingredients__link')

    ingredients_final = []

    ingredient_type_counter = 0

    #Clown Unicode U+1F921

    # for i in range(len(full_ingredients)):
    #
    #     if not full_ingredients[i].contains(ingredient_types[ingredient_type_counter]):
    #         ingredients_final.append(full_ingredients[i].text + "🤡" + full_ingredients[i].text)
    #         ingredient_type_counter = ingredient_type_counter - 1
    #
    #     else:
    #         ingredients_final.append(ingredient_types[ingredient_type_counter].text + "🤡" + full_ingredients[i].text)
    #
    #     ingredient_type_counter = ingredient_type_counter + 1

    # for ingredient_type in ingredient_types:
    #     print(ingredient_type.text)
    # for ingredient_full in ingredient_fulls:
    #     print(ingredient_full.text)
    #
    # itypecounter = 0
    # for i in range(len(ingredient_fulls)):
    #     if ingredient_types[itypecounter].text not in ingredient_fulls[i].text:
    #         ingredients_final.append(ingredient_fulls[i].text + "🤡" + ingredient_fulls[i].text)
    #
    #     else:
    #         ingredients_final.append(ingredient_types[itypecounter] + "🤡" + ingredient_fulls[i])
    #         itypecounter = itypecounter + 1



    return ingredient_fulls

def title_scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    title = soup.find('h1', {'itemprop': "name"})

    return title

def instruction_scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    instructions = soup.findAll('li', {'itemprop': 'recipeInstructions'})

    return instructions


def scraper():

    with open("used_urls1.txt", "r", encoding="utf-8") as used_urls_document:
        raw_urls = used_urls_document.read()
        used_urls = raw_urls.split("🙈")
        print(used_urls)

    for ur in pre_url_scrape():
        time.sleep(0.5)

        for url in url_scrape("https://bbc.co.uk" + ur):
            time.sleep(0.5)
            new_url = "https://www.bbc.co.uk" + url

            if new_url not in used_urls:
                used_urls.append(new_url)

                with open("used_urls1.txt", "a", encoding="utf-8") as used_urls_document:

                    used_urls_document.write(new_url)
                    #Indicates each url
                    #Unicode U+1F648
                    used_urls_document.write("🙈")

                with open("scrape1.txt", "a", encoding="utf-8") as text_document:

                    #Indicates when a new recipe is reached
                    #Unicode U+1F600
                    print("😀")
                    text_document.write("😀")

                    title = title_scrape(new_url)
                    time.sleep(1)

                    print("\n")
                    text_document.write("\n")

                    #Cowboy indicates error in title Unicode U+1F920
                    if title is None:
                        print("🤠")
                        text_document.write("🤠")

                    else:
                        print(title.text)
                        text_document.write(title.text)

                    #Indicates when the ingredients section begins
                    #Unicode U+1F609
                    print("\n")
                    print("😉")
                    text_document.write("\n")
                    text_document.write("😉")
                    for ingredient in ingredient_scrape(new_url):
                        time.sleep(1)
                        print("\n")
                        print(ingredient.text)
                        text_document.write("\n")
                        text_document.write(ingredient.text)

                    #Indicates when the instructions section begins
                    #Unicode U+1F618
                    print("\n")
                    print("😘")
                    text_document.write("\n")
                    text_document.write("😘")
                    for instruction in instruction_scrape(new_url):
                        time.sleep(1)
                        print("\n")
                        print(instruction.text)
                        text_document.write("\n")
                        text_document.write(instruction.text)

scraper()
#ingredient_scrape("https://www.bbc.co.uk/food/recipes/christmas_apple_tarts_28037")