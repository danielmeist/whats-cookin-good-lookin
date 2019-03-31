def parser():

    with open("scrape.txt", "r", encoding="utf-8") as src_text_document:
        src_text = src_text_document.read()
        recipes = src_text.split("😀")

        for recipe in recipes:
            ingredients = find_ingredients(recipe)
            print(ingredients)


def find_ingredients(recipe):

    start_ingredients = 0
    end_ingredients = 0

    for char in recipe:
        if char == "😉":
            start_ingredients = recipe.find(char)

        if char == "😘":
            end_ingredients = recipe.find(char)
            break

    return recipe[start_ingredients:end_ingredients]


parser()

