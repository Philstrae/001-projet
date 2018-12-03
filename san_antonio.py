import random
import json

# -*- coding: utf8 -*-

quotes= [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

#characters = [
#   "alvin et les Chipmunks",
#    "Babar",
#    "betty boop",
#    "calimero",
#    "casper",
#   "le chat potté",
#   "kirikou"
#]

def read_value_from_json():
        values = []
        with open('characters.json') as f:
                data = json.load(f)
        for entry in data:
                values.append(entry['character'])
        return values

def get_random_item(my_list):
        rand_numb = random.randint(0,len(my_list) - 1)
        item = my_list[rand_numb]
        return item

def random_character():
        all_values = read_value_from_json()
        return get_random_item(all_values)        

def capitalize(words):
        for word in words:
                word.capitalize()

def message(character, quote):
        capitalize(character)
        capitalize(quote)
        return "{} a dit : {}".format(character, quote)

# Show random quoteinput()
user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

while user_answer != "B":
        print(message(get_random_item(characters), random_character()))
        user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")





