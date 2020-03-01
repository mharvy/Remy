import torch
import requests
from fractions import Fraction
from bs4 import BeautifulSoup
import numpy as np

global lbs_to_cups 
global ozs_to_cups
global cans_to_cups 
global heads_to_cups
global teasp_to_cups
global tablesp_to_cups
global max_cups

ingredients_file = open("ingredients.txt","r")

#units
#lb = "pound"
#lbs = "pounds"
#oz = "ounce"
#ozs = "ounces"
#cup = "cup"
#cups = "cups"
#can = "can"
#cans = "cans"
#head = "head"
#heads = "heads"
#teasp = "teaspoon"
#teasps = "teaspoons"
#tablesp = "tablespoon"
#tablesp = "tablespoons"

#conversions
lbs_to_cups = 2.25
ozs_to_cups = .125
cans_to_cups = .125 #given an ounces of the cans so should be the same
heads_to_cups = 3.5
teasp_to_cups = 0.0208333
tablesp_to_cups = 0.0625

conversions = []

#read lines from the ingredient file
for line in ingredients_file.readlines():
    #breaks the ingredients into a direct list with removing '~' seperator
    ingredients = line.split('~')[:-1] #splits into seperate string with using spaces for easy parsing
    for ingredient in ingredients:
        subingredients = ingredient.split(' ')
        temp = 0 #storing variable
        conversion = 0 #what we want
        #case, example: 2 2/3 teaspoons of water... should handle 2 2/3 (units) and 2 (units)
        # handles a integer as the first index
        if len(subingredients[0]) == 1 and subingredients[0].isdigit:
            temp += int(subingredients[0])
            # handles fractions
            if len(subingredients[1]) == 3:
                if subingredients[1][0].isdigit and subingredients[1][1] == '/' and subingredients[1][2].isdigit:
                    temp += float(Fraction(subingredients[1][:]))
                    #conversions take place where, find the unit that follows the integer index 0 and fraction index 1
                    if "pound" in subingredients[2] or "pounds" in subingredients[2]:
                        conversion = temp * lbs_to_cups
                        conversions.append(conversion)
                    elif "ounce" in subingredients[2] or "ounces" in subingredients[2]:
                        conversion = temp * ozs_to_cups
                        conversions.append(conversion)
                    elif "head" in subingredients[2] or "heads" in subingredients[2]:
                        coversion = temp * heads_to_cups
                        conversions.append(conversion)
                    elif "teaspoon" in subingredients[2] or "teaspoons" in subingredients[2]:
                        conversion = temp * teasp_to_cups
                        conversions.append(conversion)
                    elif "tablespoon" in subingredients[2] or "tablespoons" in subingredients[2]:
                        conversion = temp * tablesp_to_cups
                        conversions.append(conversion)
                    elif "cup" in subingredients[2] or "cups" in subingredients[2]:
                        conversion = temp
                        conversions.append(conversion)
                #handles the special cases of the (xx ounces)
                elif subingredients[1][0] == '(' and len(subingredients[1]) == 3:
                    #if this happens, we already have added '1' so we should get the correct value
                    if subingredients[1][1].isdigit and subingredients[1][2].isdigit:
                        temp = float(subingredients[1][1:3])
                        conversion = temp * ozs_to_cups
                        conversions.append(conversion)
                #handles the special cases of the (.xx ounces)        
                elif subingredients[1][0] == '(' and subingredients[1][1] == '.' and len(subingredients[1]) > 3:
                        temp = float(subingredients[1][2:4])
                        conversion = temp * ozs_to_cups
                        conversions.append(conversion)
                #handles the special cases of the (xx.xx ounces)
                elif subingredients[1][0] == '(' and len(subingredients[1]) == 6:
                        temp = float(subingredients[1][2:6])
                        coversion = temp * ozs_to_cups
                        conversions.append(conversion)
        #handles the fraction as the first index
        elif len(subingredients[0]) == 3:
            if subingredients[0][0].isdigit and subingredients[0][1] == '/' and subingredients[0][2].isdigit:
                temp += float(Fraction(subingredients[0][:]))
                #check to see what the units that follow the fraction from index of 0
                if "pound" in subingredients[1] or "pounds" in subingredients[1]:
                    conversion = temp * lbs_to_cups
                    conversions.append(conversion)
                elif "ounce" in subingredients[1] or "ounces" in subingredients[1]:
                    conversion = temp * ozs_to_cups
                    conversions.append(conversion)
                elif "head" in subingredients[1] or "heads" in subingredients[1]:
                    coversion = temp * heads_to_cups
                    conversions.append(conversion)
                elif "teaspoon" in subingredients[1] or "teaspoons" in subingredients[1]:                        
                    conversion = temp * teasp_to_cups
                    conversions.append(conversion)
                elif "tablespoon" in subingredients[1] or "tablespoons" in subingredients[1]:
                    conversion = temp * tablesp_to_cups
                    conversions.append(conversion)

                  
max_cups = 12.375
normalized_conversions = []
i = 0
while i < len(conversions):
    normalized_conversions.append(conversions[i] / max_cups)
    i += 1


