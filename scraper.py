import requests
from bs4 import BeautifulSoup
import heapq


def worm(starting_URL):
	URLs = [starting_URL]
	visited = set()
	visited.add(starting_URL)

	ingredients_list = open("ingredients.txt","a")
	steps_list = open("steps.txt","a")
	lists_written = 0

	while len(URLs) != 0:
		URL = URLs.pop()

		# start of brennen code
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
						formatted_steps = step.get_text().strip().split('.')
						
						for sub_step in formatted_steps:
							if len(sub_step) != 0:
								if sub_step[0] == ' ': # if begins with space, chop off
									steps.append(sub_step[1:])
								else:
									steps.append(sub_step)
			except:
				continue

		# add steps and ingredients to files
		if len(ingredients) != 0 and len(steps) != 0:
			lists_written += 1
			print(f"Recipes written: {lists_written}")
			for ingredient in ingredients:
				ingredients_list.write(ingredient + "~")
			ingredients_list.write("\n")
			for step in steps:
				steps_list.write(step + "@")
			steps_list.write("\n")
			
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