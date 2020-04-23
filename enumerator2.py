from fractions import Fraction
import os
import sys

vegetables = {"bok choy" : 0, "bean" : 1, "sorrel leaves" : 2, "rocket leaves" : 3, "drumstick" : 4, "tomato" : 5, "kaffir lime" : 6, "plantain" : 7, "turnip" : 8, "sweet potato" : 9, "round gourd" : 10, "ridge gourd": 11, "pimiento": 12, "spinach" : 13, "onion" : 14, "mustard leaves" : 15, "mushroom" : 16, "radish" : 17, "shallots" : 18, "lettuce" : 19, "leek" : 20, "pumpkin" : 21, "yam" : 22, "jalapeno" : 23, "jackfruit" : 24, "horseradish" : 25, "spring onion" : 26, "peas" : 27, "chiles" : 28, "gherkin" : 29, "garlic" : 30, "fenugreek" : 31, "cucumber" : 32, "zucchini" : 33, "corn" : 34, "celery":35,"cauliflower":36,"carrot":37,"capers":38,"broccoli":39,"lotus":40,"bell pepper":41,"beetroot":42,"cabbage":43,"avocado":44,"eggplant":45,"asparagus":46,"artichoke":47,"potato":48,"ginger":49,"kale":50,"shallot":51,"squash":52, "cayenne pepper": 53, "beet": 54}
spices_herbs = {"chives":0,"galangal":1,"sage":2,"rosemary":3,"oregano":4,"nasturtium":5,"salt":6,"mustard":7,"paprika":8,"mint":9,"marjoram":10,"lemongrass":11,"saffron":12,"nutmeg":13,"herbs":14,"thyme":15,"turmeric":16,"fennel":17,"dill":18,"cumin":19,"coriander":20,"cloves":21,"cinnamon":22,"cayenne":23,"caraway":24,"cajun":25,"pepper":26,"bay leaf":27,"basil":28,"parsley":29,"cilantro":30,"italian seasoning":31,"tarragon":32,"masala":33,"pesto":34,"curry powder":35}
cereals_pulses = {"flour":0,"amaranth":1,"oats":2,"jowar":3,"brown rice":4,"tapioca":5,"puffed rice":6,"kidney beans":7,"lentils":8,"couscous":9,"cornmeal":10,"breadcrumbs":11,"bread":12,"black beans":13,"chickpeas":14,"basmati rice":15,"barley":16,"millet":17,"bean sprouts":18}
meats = {"beef":0,"chicken":1,"turkey":2,"pork":3,"partridge":4,"stock":5,"liver":6,"ham":7,"crab":8,"chicken stock":9,"chops":10,"lamb":11,"venison":12,"sausage":13,"bacon":14,"mutton":15,"quail":16, "egg white":17, "egg yolk":18}
dairy = {"gruyere cheese":0,"gouda cheese":1,"feta cheese":2,"milk":3,"brie cheese":4,"cream cheese":5,"ricotta cheese":6,"parmesan cheese":7,"blue cheese":8,"cheddar":9,"cream":10,"provolone":11,"mozzarella":12,"yogurt":13,"cottage cheese":14,"condensed milk":15,"butter":16,"margarine":17,"buttermilk":18}
fruits = {"cranberr":0,"kiwi":1,"blueberr":2,"mango":3,"watermelon":4,"strawberr":5,"water chestnut":6,"papaya":7,"orange":8,"olive":9,"pear":10,"mulberr":11,"lemon juice":12,"lemon":13,"raisins":14,"tamarind":15,"grapefruit":16,"gooseberr":17,"dates":18,"apple":19,"apples":20,"coconut":21,"cherries":22,"cherry":23,"banana":24,"apricot":25,"grapes":26,"pomegranate":27,"pineapple":28,"fig":29,"guava":30,"plum":31,"raspberr":32,"blackberr":33,"lime":34,"berr":35,"peach":36}
seafood = {"shrimp":0,"tuna fish":1,"shellfish":2,"shark":3,"sardine":4,"salmon":5,"prawns":6,"pomfret":7,"perch":8,"mussel":9,"mullet":10,"squid":11,"haddock":12,"flounder":13,"fish":14,"fish filet":15,"cod":16,"clam":17,"cat fish":18,"mackeral":19,"anchovies":20}
sugar_products = {"brown sugar":0,"sugar candy":1,"confectionary sugar":2,"powdered sugar":3,"icing sugar":4,"honey":5,"jaggery":6,"syrup":7,"sugar":8,"cane sugar":9,"caramel":10,"castor sugar":11,"white sugar":12}
nuts_oils = {"canola oil":0,"cooking spray":1,"chia seeds":2,"hazelnut":3,"pine nuts":4,"mustard oil":5,"sunflower seeds":6,"sesame oil":7,"pistachio":8,"olive oil":9,"mustard seeds":10,"poppy seeds":11,"sesame seeds":12,"peanuts":13,"chironji":14,"cashew":15,"almond":16,"walnuts":17,"walnuts":18,"pecan":19,"baking spray":20}
other = {"almond milk":0,"red wine":1,"vinegar":2,"white wine":3,"soy milk":4,"yeast":5,"white pepper":6,"rice vinegar":7,"sea salt":8,"hoisin sauce":9,"malt vinegar":10,"chocolate chips":11,"quinoa":12,"baking powder":13,"baking soda":14,"rice flour":15,"wheat flour":16,"oyster sauce":17,"teriyaki":18,"soy sauce":19,"noodle":20,"pasta":21,"lasagne":22,"spaghetti":23,"macaroni":24,"rigatoni":25,"ravioli":26,"penne":27,"balsamic vinegar":28,"coconut oil":29,"rice noodles":30,"coffee":31,"beer":32,"chocolate":33,"sake":34,"vinaigrette":35,"vanilla":36,"tortilla":37,"tomato puree":38,"vegetable oil":39,"sharbat":40,"rum":41,"paan":42,"meringue":43,"mayonnaise":44,"melon seeds":45,"lotus seeds":46,"jelly":47,"gold leaves":48,"glycerine":49,"gelatin":50,"fish sauce":51,"cranberry sauce":52,"cornflour":53,"cognac":54,"coconut water":55,"coconut milk":56,"cocoa":57,"tea":58,"brown sauce":59,"tofu":60,"egg":61,"marzipan":62,"agar":63,"peanut butter":64,"flax seed":65,"water":66,"ice":67,"protein powder":68,"cornstarch":69,"roll":70,"worcestershire sauce":71,"pancake mix":72,"marshmellow":73,"barbeque sauce":74, "salsa": 75, "salt and pepper": 76}

actions = {"fill":0,"preheat":1,"place":2,"mix":3,"cook":4,"garnish":5,"stir":6,"pulse":7,"puree":8,"season":9,"spread":10,"serve":11,"cover":12,"bake":13,"arrange":14,"lay":15,"sprinkle":16,"drizzle":17,"toss":18,"coat":19,"flip":20,"heat":21,"drop":22,"whisk":23,"form":24,"turn":25,"pour":26,"punch":27,"scoop":28,"beat":29,"refrigerate":30,"combine":31,"blend":32,"brush":33,"roll":34,"cool":35,"add":36,"spray":37,"simmer":38,"chill":39,"break":40, "roast":41, "saute": 42, "microwave": 43, "boil": 44, "drain": 45, "broil": 46, "steam": 47, "mash": 48, "sift": 49, "grease": 50, "wrap": 51, "slide": 52}  # cut, squeeze
temperatures = {'300':300,'325':325,'350':350,'375':375,'400':400,'425':425,'450':450,'475':475,'500':500,'525':525,'550':550,'medium-high':1000, 'high-heat':1100, 'medium-heat':900, 'low-heat':700,'medium-low':800}

# array of dictionaries
ingredients_list = [vegetables, spices_herbs, cereals_pulses, meats, dairy, fruits, seafood, sugar_products, nuts_oils, other]
num_ingredients = sum(len(s) for s in ingredients_list)

# array of ALL ingredients
all_ingredients = list(vegetables.keys()) + list(spices_herbs.keys()) + list(cereals_pulses.keys()) + list(meats.keys()) + list(dairy.keys()) + list(fruits.keys()) + list(seafood.keys()) + list(sugar_products.keys()) + list(nuts_oils.keys()) + list(other.keys())
num_actions = len(actions)
num_attributes = len(ingredients_list)

MAX_ID_COUNT = 77
MAX_TEMPERATURE = 1100
MAX_TIME = 36000
MAX_QUANTITY = 200

attributes = ['vegetables', 'spices_herbs', 'cereals_pulses', 'meats', 'dairy', 'fruits', 'seafood', 'sugar_products', 'nuts_oils', 'other']
time_units = ['second','seconds','minute','minutes','hour','hours']

# conversions
lbs_to_cups = 2.25
ozs_to_cups = .125
cans_to_cups = .125 # given an ounces of the cans so should be the same
heads_to_cups = 3.5
teasp_to_cups = 0.0208333
tablesp_to_cups = 0.0625

# encode_recipes:
#
# This function takes plaintext ingredient and steps files
# and returns a file with encoded recipes. The encoding is
# one-hot, based on the above numbers. Recall that for the 
# input files, each line MUST correlate to the same recipe
#
def encode_recipes(ingredients_in, steps_in, recipes_out):
    ingredients_file = open(ingredients_in,"r",errors="ignore")
    steps_file = open(steps_in,"r", errors="ignore")
    ingredients_lines = ingredients_file.readlines()
    steps_lines = steps_file.readlines()

    recipe_ingredients_info = []
    recipe_steps_info = []

    #len(ingredients_lines)
    for line_i in range(len(ingredients_lines)):
        try:
            ingredients = ingredients_lines[line_i].split('~')[:-1]
            steps = steps_lines[line_i].split('@')[:-1]
            for step_i in range(len(steps)):
                if ';' in steps[step_i]:
                    temp = []
                    if step_i + 1 < len(steps):
                        temp = steps[step_i + 1:]
                    steps = steps[:step_i] + steps[step_i].split(';') + temp
            steps_info = []
            for step in steps:

                # check if we've already reached max steps
                if len(steps_info) == 10*(num_actions + 2 + num_ingredients):
                    break

                # each step requires 4 elements:
                action_one_hot = [0 for _ in range(num_actions)]
                time = 0
                temperature = 0
                ingredients_one_hot = [0 for _ in range(num_ingredients)]

                # run through each word in the step to find the action
                action = ''
                words = step.split(' ')
                for word in words:
                    word = word.lower()
                    if word in actions.keys():
                        action = word
                        break
                    elif word[:-1] in actions.keys(): # check w/o comma, semi-colon, or any punctation
                        action = word[:-1]
                        break
                
                if action == '':
                    continue

                action_one_hot[actions[action]] = 1

                # check temperature if appropriate action word
                if action == 'preheat' or action == 'heat':
                    for word in words: # check for single temp words: '375' or '425'
                        word = word.lower()
                        if word in temperatures.keys():
                            temperature = temperatures[word]
                        elif word[:-1] in temperatures.keys():
                            temperature = temperatures[word[:-1]]
                    for word_i in range(1,len(words)): # check for bi-gram temp words: 'medium heat' or 'low heat'
                        bigram = words[word_i - 1] + ' ' + words[word_i]
                        if bigram in temperatures.keys():
                            temperature = temperatures[bigram]
                        elif bigram[:-1] in temperatures.keys():
                            temperature = temperatures[bigram[:-1]]

                # check time, looking at bigrams
                for word_i in range(1,len(words)):
                    is_numeral = 1
                    for c in words[word_i - 1]:
                        if not c.isdigit():
                            is_numeral = 0
                    if is_numeral:
                        if len(words[word_i-1]) > 0 and words[word_i].lower() in time_units:
                            time = int(words[word_i - 1])
                            if words[word_i].lower() == 'minute' or words[word_i].lower() == 'minutes':
                                time *= 60
                            elif words[word_i].lower() == 'hour' or words[word_i].lower() == 'hours':
                                time *= 3600
                        elif len(words[word_i-1]) > 0 and words[word_i][:-1].lower() in time_units:
                            time = int(words[word_i - 1])
                            if words[word_i][:-1].lower() == 'minute' or words[word_i][:-1].lower() == 'minutes':
                                time *= 60
                            elif words[word_i][:-1].lower() == 'hour' or words[word_i][:-1].lower() == 'hours':
                                time *= 3600

                # check for bi-grams ingredients
                blacklist = []
                if len(words) > 1:
                    for f_i in range(num_ingredients):
                        for word_i in range(1,len(words))[::-1]:
                            bigram = words[word_i-1] + ' ' + words[word_i]
                            if bigram == all_ingredients[f_i]:
                                ingredients_one_hot[f_i] = 1
                                blacklist += [word_i-1, word_i]
                            elif bigram[:-1] == all_ingredients[f_i]:
                                ingredients_one_hot[f_i] = 1
                                blacklist += [word_i-1, word_i]
                            elif len(bigram) > 1 and bigram[:-2] == all_ingredients[f_i]:
                                ingredients_one_hot[f_i] = 1
                                blacklist += [word_i-1, word_i]
                            elif len(bigram) > 2 and bigram[:-3] == all_ingredients[f_i]:
                                ingredients_one_hot[f_i] = 1
                                blacklist += [word_i-1, word_i]

                # finally, check for ingredients
                for f_i in range(num_ingredients): 
                    for word_i in range(len(words))[::-1]:
                        if word_i in blacklist:
                            continue
                        word = words[word_i].lower()
                        if word == all_ingredients[f_i]:
                            ingredients_one_hot[f_i] = 1
                        elif len(word) > 0 and word[:-1] == all_ingredients[f_i]:
                            ingredients_one_hot[f_i] = 1
                        elif len(word) > 1 and word[:-2] == all_ingredients[f_i]:
                            ingredients_one_hot[f_i] = 1
                        elif len(word) > 2 and word[:-3] == all_ingredients[f_i]:
                            ingredients_one_hot[f_i] = 1
                
                steps_info += action_one_hot + [temperature/MAX_TEMPERATURE, time/MAX_TIME] + ingredients_one_hot

            while len(steps_info) < 10*(num_actions + 2 + num_ingredients):
                steps_info += [0 for _ in range(num_actions + 2 + num_ingredients)]
            
            ingredients_info = []
            for ingredient in ingredients:
                # check if we've already reached max steps
                if len(ingredients_info) == 10*(num_attributes + MAX_ID_COUNT + 1):
                    break
                # elements in ingredients
                attribute = [0 for _ in range(num_attributes)]
                id = [0 for _ in range(MAX_ID_COUNT)]
                quantity = temp = conversion = 0

                # divide into sub ingredients
                sub_ingredients = ingredient.split(' ')

                starts_with_number = 1
                for c in sub_ingredients[0]:
                    if not c.isdigit():
                        starts_with_number = 0

                if len(sub_ingredients[0]) >= 1 and starts_with_number:
                    temp += int(sub_ingredients[0])

                    # handles fractions
                    if len(sub_ingredients) > 1: # if theres a second element, lets analyze

                        if len(sub_ingredients[1]) == 3 and sub_ingredients[1][0].isdigit and sub_ingredients[1][1] == '/' and sub_ingredients[1][2].isdigit:
                            temp += float(Fraction(sub_ingredients[1]))
                            #conversions take place where, find the unit that follows the integer index 0 and fraction index 1
                            if sub_ingredients[2] == "pound" or sub_ingredients[2] == "pounds" or sub_ingredients[2] == "lb." or sub_ingredients[2] == "lb" or sub_ingredients[2] == "lbs" or sub_ingredients[2] == "lbs":
                                conversion = temp * lbs_to_cups
                            elif sub_ingredients[2] == "ounce" or sub_ingredients[2] == "ounces" or sub_ingredients[2] == "oz" or sub_ingredients[2] == "oz.":
                                conversion = temp * ozs_to_cups
                            elif sub_ingredients[2] == "head" or sub_ingredients[2] == "heads":
                                conversion = temp * heads_to_cups
                            elif sub_ingredients[2] == "teaspoon" or sub_ingredients[2] == "teaspoons" or sub_ingredients[2] == "tsp" or sub_ingredients[2] == "tsp.":
                                conversion = temp * teasp_to_cups
                            elif sub_ingredients[2] == "tablespoon" or sub_ingredients[2] == "tablespoons" or sub_ingredients[2] == "tbspn":
                                conversion = temp * tablesp_to_cups
                            elif sub_ingredients[2] == "cup" or sub_ingredients[2] == "cups":
                                conversion = temp

                        #handles the special cases of the (xx ounces)
                        elif sub_ingredients[1][0] == '(' and len(sub_ingredients[1]) == 3:
                            #if this happens, we already have added '1' so we should get the correct value
                            if sub_ingredients[1][1].isdigit and sub_ingredients[1][2].isdigit:
                                temp = float(sub_ingredients[1][1:3])
                                conversion = temp * ozs_to_cups

                        #handles the special cases of the (.xx ounces)        
                        elif sub_ingredients[1][0] == '(' and sub_ingredients[1][1] == '.' and len(sub_ingredients[1]) > 3:
                                temp = float(sub_ingredients[1][2:4])
                                conversion = temp * ozs_to_cups

                        #handles the special cases of the (xx.xx ounces)
                        elif sub_ingredients[1][0] == '(' and len(sub_ingredients[1]) == 6:
                                temp = float(sub_ingredients[1][2:6])
                                conversion = temp * ozs_to_cups

                        # handles case where it is just 1 tablespoon, etc
                        elif sub_ingredients[1] == "pound" or sub_ingredients[1] == "pounds" or sub_ingredients[1] == "lb." or sub_ingredients[1] == "lb" or sub_ingredients[1] == "lbs" or sub_ingredients[1] == "lbs":
                            conversion = temp * lbs_to_cups
                        elif sub_ingredients[1] == "ounce" or sub_ingredients[1] == "ounces" or sub_ingredients[1] == "oz" or sub_ingredients[1] == "oz.":
                            conversion = temp * ozs_to_cups
                        elif sub_ingredients[1] == "head" or sub_ingredients[1] == "heads":
                            conversion = temp * heads_to_cups
                        elif sub_ingredients[1] == "teaspoon" or sub_ingredients[1] == "teaspoons" or sub_ingredients[1] == "tsp" or sub_ingredients[1] == "tsp.":
                            conversion = temp * teasp_to_cups
                        elif sub_ingredients[1] == "tablespoon" or sub_ingredients[1] == "tablespoons" or sub_ingredients[1] == "tbspn":
                            conversion = temp * tablesp_to_cups
                        elif sub_ingredients[1] == "cup" or sub_ingredients[1] == "cups":
                            conversion = temp

                        # otherwise you have one/two/tree whole:
                        else:
                            conversion = temp

                #handles the fraction as the first index
                elif len(sub_ingredients[0]) == 3 and len(sub_ingredients) > 1 and sub_ingredients[0][0].isdigit and sub_ingredients[0][1] == '/' and sub_ingredients[0][2].isdigit:
                    temp += float(Fraction(sub_ingredients[0]))

                    #check to see what the units that follow the fraction from index of 0
                    if sub_ingredients[1] == "pound" or sub_ingredients[1] == "pounds" or sub_ingredients[1] == "lb." or sub_ingredients[1] == "lb" or sub_ingredients[1] == "lbs" or sub_ingredients[1] == "lbs":
                        conversion = temp * lbs_to_cups
                    elif sub_ingredients[1] == "ounce" or sub_ingredients[1] == "ounces" or sub_ingredients[1] == "oz" or sub_ingredients[1] == "oz.":
                        conversion = temp * ozs_to_cups
                    elif sub_ingredients[1] == "head" or sub_ingredients[1] == "heads":
                        conversion = temp * heads_to_cups
                    elif sub_ingredients[1] == "teaspoon" or sub_ingredients[1] == "teaspoons" or sub_ingredients[1] == "tsp" or sub_ingredients[1] == "tsp.":
                        conversion = temp * teasp_to_cups
                    elif sub_ingredients[1] == "tablespoon" or sub_ingredients[1] == "tablespoons" or sub_ingredients[1] == "tbspn":
                        conversion = temp * tablesp_to_cups
                    elif sub_ingredients[1] == "cup" or sub_ingredients[1] == "cups":
                        conversion = temp
                    # otherwise you have one half whole
                    else:
                        conversion = temp
                quantity = conversion

                # now we've found quantity (not normalized yet)
                for i in range(len(sub_ingredients)):
                    sub_ingredients[i] = sub_ingredients[i].lower()

                # check for word matches
                for sub_ingredient in sub_ingredients[::-1]:
                    done = False
                    for food_type_i in range(len(ingredients_list)):
                        if sub_ingredient in ingredients_list[food_type_i].keys():
                            attribute[food_type_i] = 1
                            id[ingredients_list[food_type_i][sub_ingredient]] = 1
                            done = True
                            break
                        # remove end character (could be ',' or 's')
                        elif len(sub_ingredient) > 0 and sub_ingredient[:-1] in ingredients_list[food_type_i].keys():
                            attribute[food_type_i] = 1
                            id[ingredients_list[food_type_i][sub_ingredient[:-1]]] = 1
                            done = True
                            break
                        # remove 2 end characters (could be 's,')
                        elif len(sub_ingredient) > 1 and sub_ingredient[:-2] in ingredients_list[food_type_i].keys():
                            attribute[food_type_i] = 1
                            id[ingredients_list[food_type_i][sub_ingredient[:-2]]] = 1
                            done = True
                            break
                            # remove 2 end characters (could be 'es,')
                        elif len(sub_ingredient) > 2 and sub_ingredient[:-3] in ingredients_list[food_type_i].keys():
                            attribute[food_type_i] = 1
                            id[ingredients_list[food_type_i][sub_ingredient[:-3]]] = 1
                            done = True
                            break
                    if done:
                        break

                # if more than one word, check for any matching bi-grams in ingredients_list
                if len(sub_ingredients) > 1:
                    for sub_ingre_index in range(1, len(sub_ingredients))[::-1]:
                        done = False
                        bigram = sub_ingredients[sub_ingre_index - 1] + ' ' + sub_ingredients[sub_ingre_index]
                        for food_type_i in range(len(ingredients_list)):
                            if bigram in ingredients_list[food_type_i].keys():
                                # Clear any 1-word finds
                                attribute = [0.0 for i in attribute]
                                id = [0 for i in id]
                                
                                attribute[food_type_i] = 1
                                id[ingredients_list[food_type_i][bigram]] = 1

                                done = True
                                break

                            # remove end character, could be ',' or 's'
                            elif bigram[:-1] in ingredients_list[food_type_i].keys():
                                # Clear any 1-word finds
                                attribute = [0.0 for i in attribute]
                                id = [0 for i in id]

                                attribute[food_type_i] = 1
                                id[ingredients_list[food_type_i][bigram[:-1]]] = 1

                                done = True
                                break

                            # remove 2 end characters, could be 's,'
                            elif len(bigram) > 1 and bigram[:-2] in ingredients_list[food_type_i].keys():
                                # Clear any 1-word finds
                                attribute = [0.0 for i in attribute]
                                id = [0 for i in id]

                                attribute[food_type_i] = 1
                                id[ingredients_list[food_type_i][bigram[:-2]]] = 1

                                done = True
                                break

                            # remove 3 end characters, could be 's,'
                            elif len(bigram) > 2 and bigram[:-3] in ingredients_list[food_type_i].keys():
                                # Clear any 1-word finds
                                attribute = [0.0 for i in attribute]
                                id = [0 for i in id]

                                attribute[food_type_i] = 1
                                id[ingredients_list[food_type_i][bigram[:-3]]] = 1

                                done = True
                                break

                        if done:
                            break

                # Check for special cases

                # salt AND pepper
                if 'salt' in sub_ingredients and 'pepper' in sub_ingredients:
                    # Clear any 1-word finds
                    attribute = [0.0 for i in attribute]
                    id = [0 for i in id]

                    attribute[9] = 1
                    id[ingredients_list[9]['salt and pepper']] = 1

                # if it hasn't found a matching ingredient, :(
                found_ingred = 0
                for a in attribute:
                    if a:
                        found_ingred = 1
                        ingredients_info += attribute + id + [quantity/MAX_QUANTITY]

            while len(ingredients_info) < 10*(num_attributes + MAX_ID_COUNT + 1):
                ingredients_info += [0 for _ in range(num_attributes + MAX_ID_COUNT + 1)]

            # This fixes a glitch where ingredients take up step space
            ingredients_info = ingredients_info[:10*(num_attributes + MAX_ID_COUNT + 1)]

            # THE ERROR IS THAT INGREDIENTS ARE OVERWRITING STEPS WHEN INGREDIENTS > 10

            if found_ingred: 
                recipe_ingredients_info.append(ingredients_info)
                recipe_steps_info.append(steps_info)
        
        # Something went wrong with this encoding, let's not break for now...
        except Exception as e:
            print(e)
            continue

    # Remove old output file
    if os.path.exists(recipes_out):
        os.remove(recipes_out)

    # Write 1 encoded recipe per line to new file
    with open(recipes_out, "a") as recipes:
        for i in range(len(recipe_ingredients_info)):
            recipes.write( str(recipe_ingredients_info[i]+recipe_steps_info[i]).strip('[]') + "\n" )

    return recipe_ingredients_info, recipe_steps_info


if __name__ == "__main__":
    #sys.argv[1] = "recipes/ingredients.txt"
    #sys.argv[2] = "recipes/steps.txt"
    #sys.argv[3] = "recipes/encoded.txt"

    encode_recipes(sys.argv[1], sys.argv[2], sys.argv[3])
