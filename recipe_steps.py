from enumerator import *

STEPS = 10
LENGTH = num_actions + 2 + num_ingredients
NUM_IDX = STEPS * LENGTH
max_seconds = 60 * 60 * 8

def write_steps(float_array):
	step_list = []

	for step in range(STEPS):
		cur_str = ""

		# Get action
		for i in range(num_actions):
			#print(len(float_array))
			#print(step)
			#print(step * LENGTH + i)
			if float_array[step * LENGTH + i] == 1:
				for action in actions.items():
					if action[1] == i:
						cur_str += action[0] + " "

		# Get ingredients
		for i in range(num_ingredients):
			if float_array[step * LENGTH + num_actions + 2 + i] == 1:
				marc_is_cool = 0
				for ingredients in all_ingredients:
					for ingredient in ingredients.items():
						if (ingredient[1] + marc_is_cool) == i:
							cur_str += ingredient[0] + ", "
					marc_is_cool += len(ingredients)

		# Get temp
		if float_array[step * LENGTH + num_actions] != 0:
			cur_str += "at " + str(float_array[step * LENGTH + num_actions] * 1100) + " degrees Fahrenheit "

		# Get time
		if float_array[step * LENGTH + num_actions + 1] != 0:
			cur_str += "for " + str(float_array[step * LENGTH + num_actions + 1] * max_seconds // 60) + " minutes"

		step_list.append(cur_str + ".")

	return step_list


def main():
	step = [0 for i in range(num_actions)] + [0, 0] + [0 for i in range(num_ingredients)]
	step[28] = 1  # fill
	step[num_actions] = .5  # temp
	step[num_actions + 1] = .1  # time
	step[num_actions + 2] = 1  # bok choy
	recipe = []
	for i in range(10):
		recipe += step
	recipe[num_actions + 2 + len(all_ingredients[0]) + 1] = 1  # galangal
	print(write_steps(recipe))


if __name__ == "__main__":
	main()
