
from fractions import Fraction

def recipe_steps():
    actions = {"fill":0,"preheat":1,"place":2,"mix":3,"cook":4,"garnish":5,"stir":6,"pulse":7,"puree":8,"season":9,"spread":10,"serve":11,"cover":12,"bake":13,"arrange":14,"lay":15,"sprinkle":16,"drizzle":17,"toss":18,"coat":19,"flip":20,"heat":21,"drop":22,"whisk":23,"form":24,"turn":25,"pour":26,"punch":27,"scoop":28,"beat":29,"refrigerate":30,"combine":31,"blend":32,"brush":33,"roll":34,"cool":35,"add":36,"spray":37,"simmer":38,"chill":39,"break":40}
    temp_ = {'300':300,'325':325,'350':350,'375':375,'400':400,'425':425,'450':450,'475':475,'500':500,'525':525,'550':550,'medium-high heat':1000, 'high heat':1100, 'medium heat':900, 'low heat':700,'medium-low heat':800}
    time_units = ['second','seconds','minute','minutes','hour','hours']

    steps_file = open("steps.txt","r")
    lines = steps_file.readlines()

    for line in lines:
        steps = line.split('@')[:-1]
        for step in steps:
            action = ""
            temp = -1
            time = -1
            words = step.split(' ')
            for word in words:
                if word.lower() in actions.keys():
                    action = word.lower()
                    break
                if word.lower()[:-1] in actions.keys():
                    action = word.lower()[:-1]
                    break
            if action == 'preheat' or action == 'heat':
                for word in words:
                    if word in temp_.keys():
                        temp = temp_[word]
            # check bigrams for time
            for word_i in range(1,len(words)):
                is_numeral = 1
                for c in words[word_i-1]:
                    if not c.isdigit():
                        is_numeral = 0
                if len(words[word_i -1]) != 0 and is_numeral:
                    if words[word_i] in time_units:
                        time = int(words[word_i - 1])
                        if words[word_i] == 'minute' or words[word_i] == 'minutes':
                            time *= 60
                        elif words[word_i] == 'hour' or words[word_i] == 'hours':
                            time *= 3600
            #print(step)
            #if action != "":
            #    print(f"{action},{temp},{time}")

        print('\n')

vegetables = {"bok choy" : 0, "bean" : 1, "sorrel leaves" : 2, "rocket leaves" : 3, "drumstick" : 4, "tomato" : 5, "kaffir lime" : 6, "plantain" : 7, "turnip" : 8, "sweet potato" : 9, "round gourd" : 10, "ridge gourd": 11, "pimiento": 12, "spinach" : 13, "onion" : 14, "mustard leaves" : 15, "mushroom" : 16, "radish" : 17, "shallots" : 18, "lettuce" : 19, "leek" : 20, "pumpkin" : 21, "yam" : 22, "jalapeno" : 23, "jackfruit" : 24, "horseradish" : 25, "spring onion" : 26, "peas" : 27, "chiles" : 28, "gherkin" : 29, "garlic" : 30, "fenugreek" : 31, "cucumber" : 32, "zucchini" : 33, "corn" : 34, "celery":35,"cauliflower":36,"carrot":37,"capers":38,"broccoli":39,"lotus":40,"bell pepper":41,"beetroot":42,"cabbage":43,"avocado":44,"eggplant":45,"asparagus":46,"artichoke":47,"potato":48,"ginger":49,"potatoes":50,"sweet potatoes":51,"tomatoes":52,"kale":53,"shallot":54,"squash":55}
spices_herbs = {"chives":0,"galangal":1,"sage":2,"rosemary":3,"oregano":4,"nasturtium":5,"salt":6,"mustard":7,"paprika":8,"mint":9,"marjoram":10,"lemongrass":11,"saffron":12,"nutmeg":13,"herbs":14,"thyme":15,"turmeric":16,"fennel":17,"dill":18,"cumin":19,"coriander":20,"cloves":21,"cinnamon":22,"cayenne":23,"caraway":24,"cajun":25,"pepper":26,"bay leaf":27,"basil":28,"parsley":29,"cilantro":30,"italian seasoning":31,"tarragon":32,"masala":33,"pesto":34,"curry powder":35}
cereals_pulses = {"flour":0,"amaranth":1,"oats":2,"jowar":3,"brown rice":4,"tapioca":5,"puffed rice":6,"kidney beans":7,"lentils":8,"couscous":9,"cornmeal":10,"breadcrumbs":11,"bread":12,"black beans":13,"chickpeas":14,"basmati rice":15,"barley":16,"millet":17,"bean sprouts":18}
meats = {"beef":0,"chicken":1,"turkey":2,"pork":3,"partridge":4,"stock":5,"liver":6,"ham":7,"crab":8,"chicken stock":9,"chops":10,"lamb":11,"venison":12,"sausage":13,"bacon":14,"mutton":15,"quail":16}
dairy = {"gruyere cheese":0,"gouda cheese":1,"feta cheese":2,"milk":3,"brie cheese":4,"cream cheese":5,"ricotta cheese":6,"parmesan cheese":7,"blue cheese":8,"cheddar":9,"cream":10,"provolone":11,"mozzarella":12,"yogurt":13,"cottage cheese":14,"condensed milk":15,"butter":16,"margarine":17,"buttermilk":18}
fruits = {"cranberries":0,"kiwi":1,"blueberries":2,"mango":3,"watermelon":4,"strawberry":5,"water chestnut":6,"papaya":7,"orange":8,"olive":9,"pear":10,"mulberries":11,"lemon juice":12,"lemon":13,"raisins":14,"tamarind":15,"grapefruit":16,"gooseberries":17,"dates":18,"apple":19,"apples":20,"coconut":21,"cherries":22,"cherry":23,"banana":24,"pear":25,"apricot":26,"grapes":27,"pomegranate":28,"pineapple":29,"fig":30,"guava":31,"plum":32,"strawberries":33,"raspberries":34,"blackberries":35,"lime":36,"berries":37,"peach":38}
seafood = {"shrimp":0,"tuna fish":1,"shellfish":2,"shark":3,"'sardine":4,"salmon":5,"prawns":6,"pomfret":7,"perch":8,"mussel":9,"mullet":10,"squid":11,"haddock":12,"flounder":13,"fish":14,"fish filet":15,"cod":16,"clam":17,"cat fish":18,"mackeral":19,"anchovies":20}
sugar_products = {"brown sugar":0,"sugar candy":1,"confectionary sugar":2,"powdered sugar":3,"icing sugar":4,"honey":5,"jaggery":6,"syrup":7,"sugar":8,"cane sugar":9,"caramel":10,"castor sugar":11,"white sugar":12}
nuts_oils = {"canola oil":0,"cooking spray":1,"chia seeds":2,"hazelnut":3,"pine nuts":4,"mustard oil":5,"sunflower seeds":6,"sesame oil":7,"pistachio":8,"olive oil":9,"mustard seeds":10,"poppy seeds":11,"sesame seeds":12,"peanuts":13,"chironji":14,"cashew":15,"almond":16,"walnuts":17,"walnunts":18,"pecan":19,"baking spray":20}
other = {"almond milk":0,"red wine":1,"vinegar":2,"white wine":3,"soy milk":4,"yeast":5,"white pepper":6,"rice vinegar":7,"sea salt":8,"hoisin sauce":9,"malt vinegar":10,"chocolate chips":11,"quinoa":12,"baking powder":13,"baking soda":14,"rice flour":15,"wheat flour":16,"oyster sauce":17,"teriyaki":18,"soy sauce":19,"noodle":20,"pasta":21,"lasagne":22,"spaghetti":23,"macaroni":24,"rigatoni":25,"ravioli":26,"penne":27,"balsamic vinegar":28,"coconut oil":29,"rice noodles":30,"coffee":31,"beer":32,"chocolate":33,"sake":34,"vinaigrette":35,"vanilla":36,"tortilla":37,"tomato puree":38,"vegetable oil":39,"sharbat":40,"rum":41,"paan":42,"meringue":43,"mayonnaise":44,"melon seeds":45,"lotus seeds":46,"jelly":47,"gold leaves":48,"glycerine":49,"gelatin":50,"fish sauce":51,"cranberry sauce":52,"cornflour":53,"cognac":54,"coconut water":55,"coconut milk":56,"cocoa":57,"tea":58,"brown sauce":59,"tofu":60,"egg":61,"marzipan":62,"agar":63,"peanut butter":64,"flax seed":65,"water":66,"ice":67,"protein powder":68,"cornstarch":69,"roll":70,"worcestershire sauce":71,"pancake mix":72,"marshmellow":73,"barbeque sauce":74}
all_ingredients = [vegetables, spices_herbs, cereals_pulses, meats, dairy, fruits, seafood, sugar_products, nuts_oils, other]
num_ingredients = sum(len(s) for s in all_ingredients)

def recipe_ingredients():
    foodtypes = ['vegetables', 'spices_herbs', 'cereals_pulses', 'meats', 'dairy', 'fruits', 'seafood', 'sugar_products', 'nuts_oils', 'other']

    ingredients_file = open("ingredients.txt","r")

    # big poppa
    recipe_info = [] # 3 things for each ingredient: (attrib, id, amount)

    lines = ingredients_file.readlines()
    bad = 0
    for line in lines:
        ingredients = line.split('~')[:-1]
        recipe = []
        recipe_valid = 1
        for ingredient in ingredients:
            ingredient_info = [-1 for _ in range(3)]
            sub_ingredients = ingredient.split(' ')
            for i in range(len(sub_ingredients)):
                sub_ingredients[i] = sub_ingredients[i].lower()
            # check for word matches
            for sub_ingredient in sub_ingredients:
                for food_type_i in range(len(all_ingredients)):
                    if sub_ingredient in all_ingredients[food_type_i].keys():
                        ingredient_info[0] = food_type_i
                        ingredient_info[1] = all_ingredients[food_type_i][sub_ingredient]
                    # remove end character (could be ',' or 's')
                    elif len(sub_ingredient) >= 1 and sub_ingredient[:-1] in all_ingredients[food_type_i].keys():
                        ingredient_info[0] = food_type_i
                        ingredient_info[1] = all_ingredients[food_type_i][sub_ingredient[:-1]]
                    # remove 2 end characters (could be 's,')
                    elif len(sub_ingredient) > 1 and sub_ingredient[:-2] in all_ingredients[food_type_i].keys():
                        ingredient_info[0] = food_type_i
                        ingredient_info[1] = all_ingredients[food_type_i][sub_ingredient[:-2]]
            # if more than one word, check for any matching bi-grams in all_ingredients
            if len(sub_ingredients) > 1:
                for sub_ingre_index in range(1, len(sub_ingredients)):
                    bigram = sub_ingredients[sub_ingre_index - 1] + ' ' + sub_ingredients[sub_ingre_index]
                    for food_type_i in range(len(all_ingredients)):
                        if bigram in all_ingredients[food_type_i].keys():
                            ingredient_info[0] = food_type_i
                            ingredient_info[1] = all_ingredients[food_type_i][bigram]
                        # remove end character, could be ',' or 's'
                        elif bigram[:-1] in all_ingredients[food_type_i].keys():
                            ingredient_info[0] = food_type_i
                            ingredient_info[1] = all_ingredients[food_type_i][bigram[:-1]]
                        # remove 2 end characters, could be 's,'
                        elif len(bigram) > 1 and bigram[:-2] in all_ingredients[food_type_i].keys():
                            ingredient_info[0] = food_type_i
                            ingredient_info[1] = all_ingredients[food_type_i][bigram[:-2]]
            # if it hasn't found a matching ingredient, :(
            if ingredient_info[0] == -1:
                recipe_valid = 0
                break
            #print(ingredient_info)
            recipe.append(ingredient_info)
        #print("\n")
        if recipe_valid:
            recipe_info.append(recipe)
    """
    for recipe in recipe_info:
        for ingredient in recipe:
            food = ""
            for name, id_ in all_ingredients[ingredient[0]].items():
                if ingredient[1] == id_:
                    food = name
            print(f"{foodtypes[ingredient[0]]}:{food}",end=', ')          
        print('\n')
    """
    return recipe_info

def main():
    a = recipe_ingredients()
    #recipe_steps()
    print('done.')

if __name__ == "__main__":
    main()