import constants as Constants
import random

def randomInArray(arr: list):
    return random.choice(arr)

class Card:
    def __init__(self, face, suit, baseValue):
        self.suit = suit
        self.face = face
        self.baseValue = baseValue

def countHandRaw(cards: list):
    return sum((curr.baseValue for curr in cards))

def countHand(hand: list):
    for card in hand:
        if card.face == 'A':
            card.baseValue = Constants.BJ_ACE_MAX

    lowerAce: Card = None
    aceCheck = lambda card: card.face == 'A' and card.baseValue != Constants.BJ_ACE_MIN
    lowerAce = next(filter(aceCheck, hand), False)
    
    while (
        countHandRaw(hand) > Constants.BJ_WIN and
        (next(filter(aceCheck, hand), False))
    ):
        lowerAce.baseValue = Constants.BJ_ACE_MIN
        break

    return countHandRaw(hand)

def deal(hand: list, initial: bool):
    face = randomInArray(Constants.FACES)
    suit = randomInArray(Constants.SUITS)

    cardCheck = lambda card: card.face == face and card.suit == suit

    if (next(filter(cardCheck, hand), False)):
        return deal(hand, initial)

    card = Card(face, suit, face if isinstance(face, int) else (Constants.BJ_ACE_MIN if face == 'A' else Constants.BJ_FACE))

    if initial and countHand((hand + [card])) >= Constants.BJ_WIN:
        return deal(hand, initial)
    
    return hand.append(card)
