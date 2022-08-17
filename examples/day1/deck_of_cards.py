import random

type = ["Dimond", "heart", "Spade", "Clubs"]
number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck_of_cards = []
for i in type:
    for j in number:
        deck_of_cards.append(j + i)
print(deck_of_cards)
random.shuffle(deck_of_cards)
print(deck_of_cards)
