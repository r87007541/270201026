'''import random
deck = [['b',1],['b',1],['b',1],['b',2],['b',2],['b',3],['b',3],['b',4],['w',1],['w',1],['w',1],['w',2],['w',2],['w',3],['w',3],['w',4]]

def shuffle(deck):
    shuffled_deck = []

    len_deck = len(deck) 

    for x in range(len_deck):  
        index = random.randint(0, len_deck-1) #random number from 0 to the length of the deck minus 1 
        shuffled_deck.append(deck[index])  #get random item from the deck using the index and append it to the output list
    return shuffled_deck
print(shuffle(deck))'''

print()