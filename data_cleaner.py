from enumerator import recipes, num_ingredients, num_actions
from recipe_steps import write_steps

ATTRIB_COUNT = 10
MAX_ID_COUNT = 75

MAX_TEMP = 1100
global max_weight

def data_cleaner():
    recipe_ingredient_info, recipe_step_info = recipes()

    out_ingred_info = []
    out_step_info = []

    # normalize weights
    max_weight = 0
    for recipe in recipe_ingredient_info:
        for (a,b, weight) in recipe:
            if weight > max_weight:
                max_weight = weight
    for recipe_i in range(len(recipe_ingredient_info)):
        for ingredient_i in range(len(recipe_ingredient_info[recipe_i])):
            recipe_ingredient_info[recipe_i][ingredient_i][2] = recipe_ingredient_info[recipe_i][ingredient_i][2] / max_weight

    # normalize time & temp
    max_seconds = 0
    for recipe in recipe_step_info:
        for step in recipe:
            if step[num_actions] == -1:
                step[num_actions] = 0
            if step[num_actions + 1] == -1:
                step[num_actions + 1] = 0
            if step[num_actions] > max_seconds:
                max_seconds = step[num_actions]
    for recipe_i in range(len(recipe_step_info)):
        for step_i in range(len(recipe_step_info[recipe_i])):
            recipe_step_info[recipe_i][step_i][num_actions] = recipe_step_info[recipe_i][step_i][num_actions] / MAX_TEMP
            recipe_step_info[recipe_i][step_i][num_actions+1] = recipe_step_info[recipe_i][step_i][num_actions+1] / max_seconds
    print(max_seconds)
    # (atrib, id, weight)
    for recipe_i in range(len(recipe_ingredient_info)):
        if len(recipe_ingredient_info[recipe_i]) > 10:
            continue
        # convert attrib and id to onehot, and fill in zeroes for non existant ingredients to get to 10
        out_ingreds = []
        for (atrib, id, weight_n) in recipe_ingredient_info[recipe_i]:
            atrib_one_hot = [0 for _ in range(ATTRIB_COUNT)]
            id_one_hot = [0 for _ in range(MAX_ID_COUNT)]

            atrib_one_hot[atrib] = 1
            id_one_hot[id] = 1
            out_ingreds += atrib_one_hot + id_one_hot + [weight_n]
        while(len(out_ingreds) < 10*(ATTRIB_COUNT + MAX_ID_COUNT + 1)):
            out_ingreds += [0 for _ in range(ATTRIB_COUNT + MAX_ID_COUNT + 1)]
        # format steps
        out_steps = []
        for step in recipe_step_info[recipe_i]:
            out_steps += step
            if len(out_steps) == 10:
                break
        while(len(out_steps) < 10*(num_actions + 2 + num_ingredients)):
            out_steps += [0 for _ in range(num_actions + 2 + num_ingredients)]
        out_ingred_info.append(out_ingreds)
        out_step_info.append(out_steps)
    return out_ingred_info, out_step_info



def main():
    out_ingred_info, out_step_info = data_cleaner()
    # print out first recipe raw data
    #print('\n')
    #for ingred in out_ingred_info[0]:
    #    print(ingred)
    print('\n')
    steps = write_steps(out_step_info[0])
    #for offset in range(0,3579,358):
    #    print('\n')
    #    print(out_step_info[0][offset:offset+num_actions])
    #    print(out_step_info[0][offset+num_actions])
    #    print(out_step_info[0][offset+num_actions+1])
    #    print(out_step_info[0][num_actions+offset+2:])
    for step in steps:
        print(step)
    print('done.')

if __name__ == "__main__":
    main()
