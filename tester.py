from recipe_ingredients import write_ingredients
from recipe_steps import write_steps
import sys

def main():

    # sys.argv[1] = "recipes/encoded.txt"

    # out.txt
    with open(sys.argv[1], "r") as f:
        count = 1
        for line in f.readlines():
            print(count)
            str_list = line.split(",")
            float_list = [float(s) for s in str_list]
            for f in write_ingredients(float_list[:880])[0]:
                print(f)
            for f in write_steps(float_list[880:]):
                print(f)
            print("\n")
            count += 1
        
if __name__ == "__main__":
    main()
