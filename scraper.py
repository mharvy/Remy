import requests
from bs4 import BeautifulSoup
import heapq
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




def worm(starting_URL):
	http = urllib3.PoolManager()
	URLs = [starting_URL]
	visited = set()
	visited.add(starting_URL)

	while len(URLs) != 0:
		URL = URLs.pop()

		# print the recipe:
		response = http.request('GET',URL)
		html_file = response.data

		try:

			tag = "\"recipeIngredient\": "

			for c_in in range(len(html_file) - len(tag)):
				if html_file[c_in : c_in + len(tag) ] == tag.encode('ASCII'):
					break
			ingredients_list = []
			cur_str = ''
			begin = 0

			for index in range(c_in + len(tag), len(html_file) - 1):
				# if the end of an ingredient, add the ingredient and move index past quotation and comma
				if chr(html_file[index]) + chr(html_file[index + 1]) == '\",':
					ingredients_list.append(cur_str)
					cur_str = ''
					index += 2
				cur_str += chr(html_file[index])
				# if the end of the entire list, add the final ingredient, chop off the quotation and ]
				if(chr(html_file[index]) == ']'):
					ingredients_list.append(cur_str)
					break
			# clean up ingredients and append to final list
			final_list = []
			for ingredient in ingredients_list:
				ingredient = ingredient.strip('\n')
				for index in range(len(ingredient)):
					if ingredient[index] == '\"':
						break
				final_list.append(ingredient[index + 1 :])
			# fix crap at end of last ingredient
			if len(final_list) >= 1:
				last_word = final_list[-1]
				for char_i in range(len(last_word)):
					if last_word[char_i] == '\"':
						break
				final_list[-1] = last_word[:char_i]

			if len(final_list) != 0:
				print(final_list)
			else:
				print("didnt work for this url")
		except:
			print("didnt work for this url")
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