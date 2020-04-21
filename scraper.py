import requests
from bs4 import BeautifulSoup
import heapq
import sys
from enumerator2 import *
from time import sleep


def worm(starting_URL, ingredients_out, steps_out, visited_urls):
    URLs = [starting_URL]
    visited = set()
    visited.add(starting_URL)

    ingredients_list = open(ingredients_out,"a")
    steps_list = open(steps_out,"a")
    visited_urls_list = open(visited_urls, "a")
    lists_written = 0

    # Start where we left off
    with open(visited_urls, "r") as old_urls:
        for line in old_urls.readlines():
            print(line[:-1])
            visited.add(line[:-1])  # Don't add newline!

    while len(URLs) != 0:

        URL = URLs.pop()
        failed = False
        visited_urls_list.write(URL + "\n")

        ingredients = []
        steps = []
        try:
            result = requests.get(URL)
        except:
            print("Request was denied :(")
            sleep(10)
            continue
        
        src = result.content

        soup = BeautifulSoup(src, 'lxml')
        # find ingredients
        unordered_lists = soup.find_all("ul")

        for ls in unordered_lists:
            try:
                if "lst_ingredients" in ls.attrs['id']:
                    for ingredient in ls.find_all("span"):
                        if ingredient.attrs['itemprop'] == 'recipeIngredient':
                            ingredients.append(ingredient.get_text())
            except:
                continue

        # find steps
        ordered_lists = soup.find_all("ol")
        for ls in ordered_lists:
            try:

                if "recipeInstructions" in ls.attrs['itemprop']:
                    for step in ls.find_all('span'):
                        formatted_steps = [""]
                        step_string = step.get_text().lower().strip()
                        step_string = step_string.replace("high heat", "high-heat")
                        step_string = step_string.replace("medium heat", "medium-heat")
                        step_string = step_string.replace("low heat", "low-heat")
                        for s in step_string.split(" "):
                            if "\n" in s:
                                failed = True
                                break

                            for char in s:
                                if char in " .,!;:":
                                    s = s.replace(char, '')

                            if s in actions:
                                formatted_steps.append("")
                            formatted_steps[-1] += (s + " ")

                        if "" in formatted_steps:
                            formatted_steps.remove("")
                        for sub_step in formatted_steps:
                            if len(sub_step) != 0:
                                if sub_step[0] == ' ': # if begins with space, chop off
                                    steps.append(sub_step[1:])
                                else:
                                    steps.append(sub_step)
            except Exception as e:
                print(e)
                continue

        # add steps and ingredients to files
        if len(ingredients) != 0 and len(steps) != 0 and not failed:
            lists_written += 1
            print(f"Recipes written: {lists_written}")
            for ingredient in ingredients:
                ingredients_list.write(ingredient + "~")
            ingredients_list.write("\n")
            for step in steps:
                if "\n" in step:
                    print("ALERT: here is the step %s" % step)
                steps_list.write(step + "@")
            steps_list.write("\n")

        page = requests.get(URL)
        html = str(page.content)

        soup = BeautifulSoup(page.content, 'html.parser')
        print("Current URL: %s" % URL)

        for link in soup.find_all("a"):
            new_URL = link.get("href")
            if new_URL != None:
                if "allrecipes.com/recipe/" in new_URL and \
                   "utm_source" not in new_URL and \
                   "reviews" not in new_URL and \
                   "photos" not in new_URL:
                    if new_URL not in visited:
                        URLs.append(new_URL)
                        visited.add(new_URL)
        
        if len(URLs) == 0:
            for link in soup.find_all("a"):
                new_URL = link.get("href")
                if new_URL != None:
                    if "allrecipes.com/recipes/" in new_URL:
                        if new_URL not in visited:
                            URLs.append(new_URL)
                            visited.add(new_URL)


def main():
    #starting_url = "https://www.allrecipes.com/recipe/257611/cauliflower-chicken-fried-rice/"
    #ingredients_out = "recipes/ingredients.txt"
    #steps_out = "recipes/steps.txt"

    worm(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


if __name__ == "__main__":
    main()