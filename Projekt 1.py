"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Zdeněk Pavliš
email: zdenek-pavlis@seznam.cz
discord: Zdeněk P.#2297
"""




TEXTS = [
'''
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


# Funkce pro analýzu textu
def analyze_text(text):
    slovo = text.split()
    slovo_count = len(slovo)

# počet slov
    kompletslov_count = sum(1 for slovo in slovo if slovo.istitle())

# počet slov začínajících velkým písmenem
    velkepismena_count = sum(1 for slovo in slovo if slovo.isupper())

# počet slov psaných velkými písmeny    
    malepismena_count = sum(1 for slovo in slovo if slovo.islower())

# počet slov psaných malými písmeny    
    pocet_count = sum(1 for slovo in slovo if slovo.isnumeric())

# počet čísel (ne cifer)    
    numeric_sum = sum(int(slovo) for slovo in slovo if slovo.isnumeric())

# sumu všech čísel (ne cifer) v textu    
    slovo_lengths = [len(slovo) for slovo in slovo]


# vytisknutí vět podle zadání

    print(f"There are {slovo_count} words in the selected text.")
    print(f"There are {kompletslov_count} titlecase words.")
    print(f"There are {velkepismena_count} uppercase words.")
    print(f"There are {malepismena_count} lowercase words.")
    print(f"There are {pocet_count} numeric strings.")
    print(f"The sum of all the numbers {numeric_sum}")

# tabulka pro projekt
    print("LEN| OCCURRENCES | NR.")
    print("------------------------")
    for length in range(1, max(slovo_lengths) + 1):
        count = slovo_lengths.count(length)
        bar = "*" * count
        print(f"{length:2}| {bar:11}| {count}")

# Část pro uživatele:
def lidi():
    reg_uzivatel = {
        "bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"
    }

    jmeno = input("jmeno:")
    heslo = input("heslo:")

    if jmeno in reg_uzivatel and reg_uzivatel[jmeno] == heslo :
        print("----------------------------------------")
        print(f"Welcome to the app, {jmeno}")
        print(f"We have {len(TEXTS)} texts to be analyzed.")
        print("----------------------------------------")

        while True:
            try:
                selection = int(input("Enter a number between 1 and 3 to select: "))
                if 1 <= selection <= len(TEXTS):
                    selected_text = TEXTS[selection - 1]
                    analyze_text(selected_text)
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    else:
        print("Unregistered user, terminating the program..")

if __name__ == "__main__":
    lidi()