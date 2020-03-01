from enumerator2 import recipes
from recipe_ingredients import write_ingredients
from recipe_steps import write_steps

def main():
    recipe_ingredients_info, recipe_steps_info = recipes()
    
    

    #for i in range(80):
        #steps = write_steps(recipe_steps_info[i])
        #ingredients = write_ingredients(recipe_ingredients_info[i])
        #for step in steps: 
        #    print(step)
        #print('\n')
        #for ingredient in ingredients:
        #    print(ingredient)
        #print('\n\n')
        
if __name__ == "__main__":
    main()