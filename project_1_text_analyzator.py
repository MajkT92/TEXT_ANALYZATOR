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

if login_username in username:
    user_index = username.index(login_username)
    if login_password == password[user_index]:
        print(f"Welcome to the app, {login_username}")
    else:
        print("Incorrect password, terminating the program..")
        quit()  # v případě, že heslo je nesprávné
else:
    print("Unregistered user, terminating the program..")
    quit()  # v případě, že uživatel není registrovaný


print("We have 3 texts to be analyzed.")
print(cara) #dekorace, grafika

user_choice_index = input("Enter a number btw. 1 and 3 to select: 1: ")
if user_choice_index.isdigit():
    user_choice_index = int(user_choice_index) - 1
else:
    print("wrong input, terminating the program..")
    quit()
print(cara) #dekorace, grafika

user_choice = TEXTS[user_choice_index]

pocet_slov = 0
title_pocet = 0
uppercase_pocet = 0
lower_pocet = 0
number_pocet = 0
number_soucet_textu = 0
number_soucet = 0

for analyze in user_choice.split(): #for loop pro analýzu
    pocet_slov += 1
    if analyze.istitle():
        title_pocet += 1
    if analyze.isupper():
        uppercase_pocet += 1
    if analyze.islower():
        lower_pocet += 1
    if analyze.isdigit():
        number_pocet += 1
        number_soucet += int(analyze)


print(f"There are {pocet_slov} words in the selected text.") #Celkový počet slov
print(f"There are {title_pocet} titlecase words.") #Počet slov začínající velkým
print(f"There are {uppercase_pocet} uppercase words.") #Počet slov psaný velkými
print(f"There are {lower_pocet} lowercase words.") #Počet slov psaný malými
print(f"There are {number_pocet} numeric strings.") #Počet stringu v textu
print(f"The sum of all the numbers {number_soucet}") #Součet

delka_slova = {}  # deklace pro slova
for word in user_choice.split():
    delka = len(word)
    delka_slova[delka] = delka_slova.get(delka, 0) + 1

print(cara)  # grafika
print("LEN|     OCCURRENCES     |NR.")
print(cara)

for length, count in sorted(delka_slova.items()):  # zobrazení grafu
    print(f"{length:3}| {"*" * count:19} | {count}")



















