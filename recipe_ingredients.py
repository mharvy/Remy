from enumerator2 import *

def write_ingredients(recipe_info):
    length = num_attributes + MAX_ID_COUNT + 1
    ingredients = []
    bad_apples = []

    for i in range(10):
        offset = length*i
        attrib = id_ = -1
        # find attrib
        for j in range(num_attributes):
            if recipe_info[offset + j] == 1:
                attrib = j
                break
        # find id
        for j in range(len(ingredients_list[attrib])):
            if recipe_info[offset + num_attributes + j] == 1:
                id_ = j
        # find quantity
        quantity = recipe_info[offset + num_attributes + MAX_ID_COUNT]
        ingredient = ""
        for name, num in ingredients_list[attrib].items():
            if id_ == num:
                ingredient = name
        ingredients.append(f"{quantity*MAX_QUANTITY} {ingredient}")
    return ingredients, bad_apples
