import requests
from bs4 import BeautifulSoup
import heapq


def worm(starting_URL):
	URLs = [starting_URL]
	visited = set()
	visited.add(starting_URL)

	while len(URLs) != 0:
		URL = URLs.pop()

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