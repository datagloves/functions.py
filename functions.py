import random

suits = ("Clubs", "Diamonds", "Hearts", "Spades")
ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")

def create_default_deck() -> list:
    """ Creates the standard deck of cards and returns it as a list.

    Returns:
        list: List of 52 cards in default (unshuffled) order. 
        Each card is a list of 2 cells that define suit and rank.
    """
    newDeck = []
    
    suit = 0
    rank = 0
    for i in range(52):
        newCard = [suit, rank]
        newDeck.append(newCard)
        rank += 1
        if (rank + 1 > len(ranks)):
            rank = 0
            suit += 1

    return newDeck

def shuffle_deck(deck:list) -> list:
    """ Shuffle a list of cards and return it as a new list.

    Args:
        deck (list): The deck to be shuffled.

    Returns:
        list: The shuffled deck.
    """
    shuffledDeck = []

    deckSize = len(deck)

    for i in range(deckSize):
        shuffledDeck.append(deck.pop(random.randint(0,len(deck)-1)))

    return shuffledDeck

def card_name(card:list) -> str:
    """ Takes a card as list of two numbers (suit and rank) and returns its name as a string.

    Args:
        card (list): List containing suit and rank as integers.

    Returns:
        str: Name of the card.
    """
    name = f"{ranks[card[1]]} of {suits[card[0]]}"

    return name

def list_cards(deck:list):
    for card in deck:
        print("\t"+card_name(card))

if __name__ == "__main__":
    deck = shuffle_deck(create_default_deck())

    print("Top card: "+card_name(deck[0]))
    print()

    print("Top five cards: ")
    list_cards(deck[:5])