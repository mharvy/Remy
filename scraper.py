import requests
from bs4 import BeautifulSoup
import heapq


def worm(starting_URL):
	URLs = [starting_URL]
	visited = set()
	visited.add(starting_URL)

	ingredients_list = open("ingredients.txt","a")
	lists_written = 0

	while len(URLs) != 0:
		URL = URLs.pop()

		# start of brennen code
		ingredients = []
		result = requests.get(URL)
		src = result.content

		soup = BeautifulSoup(src, 'lxml')
		lists = soup.find_all("ul")

		for ls in lists:
			try:
				if "lst_ingredients" in ls.attrs['id']:
					for ingredient in ls.find_all("span"):
						if ingredient.attrs['itemprop'] == 'recipeIngredient':
							ingredients.append(ingredient.get_text())
			except:
				continue
		if len(ingredients) != 0:
			lists_written += 1
			print(f"Recipes written: {lists_written}")
			for ingredient in ingredients:
				ingredients_list.write(ingredient + "~")
			ingredients_list.write("\n")
		# end of brennen code

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


		#print(soup.prettify())


def main():
	starting_url = "https://www.allrecipes.com/recipe/257611/cauliflower-chicken-fried-rice/"
	worm(starting_url)


if __name__ == "__main__":
	main()