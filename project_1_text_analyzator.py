"""""
project_1_text_analyzator.py: první projekt do Engeto Online Python Akademie
author: Michal Toman
email: mtoman92@gmail.com
discord: majk923278

"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

cara = "-" * 40 #grafika

username = ["bob", "ann", "mike", "liz"]
password = ["123", "pass123", "password123", "pass123"]

login_username = input("Your username: ")
login_password = input("Your password: ")
print(cara) #dekorace, grafika

if login_username == username[0] and login_password == password[0]:
    print(f"Welcome to the app, {login_username}")
elif login_username != username[0]:
    print("unregistered user, terminating the program..")
    (quit()) #v případě, že uživatel není registrovaný

print("We have 3 texts to be analyzed.")
print(cara) #dekorace, grafika

user_choice_index = int(input("Enter a number btw. 1 and 3 to select: 1: ")) - 1
print(cara) #dekorace, grafika

user_choice = str(TEXTS[user_choice_index])
pocet_slov = len(user_choice.split()) #pocet slov

print(f"There are {pocet_slov} words in the selected text.") #Celkový počet slov

title_pocet = sum(1 for char in user_choice.split() if char.istitle())
print(f"There are {title_pocet} titlecase words.") #Počet slov začínající velkým

uppercase_pocet = sum(1 for char in user_choice.split() if char.isupper())
print(f"There are {uppercase_pocet} uppercase words.") #Počet slov psaný velkými

lower_pocet = sum(1 for char in user_choice.split() if char.islower())
print(f"There are {lower_pocet} lowercase words.") #Počet slov psaný malými

number_pocet = sum(1 for char in user_choice.split() if char.isnumeric())
print(f"There are {number_pocet} numeric strings.") #Počet stringu v textu

number_soucet_textu = [int(word) for word in user_choice.split() if word.isnumeric()]
number_soucet = sum(number_soucet_textu)
print(f"The sum of all the numbers {number_soucet}") #Součet

delka_slova = {}  # deklace pro slova
for word in user_choice.split():
    delka = len(word)
    delka_slova[delka] = delka_slova.get(delka, 0) + 1

print(cara)  # grafika
print("LEN|     OCCURRENCES     |NR.")
print(cara)

for length, count in sorted(delka_slova.items()):  # zobrazení grafu
    print(f"{length:3}| {"*" * count:<19} | {count}")




















