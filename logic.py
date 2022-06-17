from cards import Card, countHand
from constants import BJ_WIN, Outcome, OutcomeResult, Outcomes

def renderCard(card: Card, idx: int, hide: bool):
    return (
        "?" if idx > 0 and hide else f"{card.suit} {card.face}"
    )

def renderHand(hand, hide: bool):
    return (
        f"Cards - {' '.join( [renderCard(card, idx, hide) for idx, card in enumerate(hand)] )}\nTotal - {'?' if hide else countHand(hand)}"
    )

def renderData(playerHand, dealerHand, stood: bool, outcome: OutcomeResult):

    return {
        'description': 'Play blackjack' if not outcome else f'{Outcomes.outcome[outcome.outcome]["message"]} {outcome.reason}',
        'fields': [
            {
                "title": "Your hand",
                "value": renderHand(playerHand, False)
            },
            {
                "title": "Your hand",
                "value": renderHand(dealerHand, False if outcome else not stood)
            }
        ]
    }

def win(reason):
    outcome = Outcome(1, 0, 0, 0)
    return OutcomeResult(outcome, reason)

def loss(reason):
    outcome = Outcome(0, 1, 0, 0)
    return OutcomeResult(outcome, reason)

def tie(reason):
    outcome = Outcome(0, 0, 1, 0)
    return OutcomeResult(outcome, reason)

def getOutcome(playerHand, dealerHand, stood: bool):
    playerScore = countHand(playerHand)
    dealerScore = countHand(dealerHand)
    
    if playerScore == BJ_WIN:
        return win("You got to 21.")
    elif dealerScore == BJ_WIN:
        return loss("The dealer got to 21 before you.")
    elif playerScore <= BJ_WIN and len(playerHand) == 5:
        return win("You took 5 cards without going over 21.")
    elif dealerScore <= BJ_WIN and len(dealerHand) == 5:
        return win("You took 5 cards without going over 21.")
    elif playerScore > BJ_WIN:
        return loss("You went over 21 and busted.")
    elif dealerScore > BJ_WIN:
        return win("The dealer went over 21 and busted.")
    elif stood and playerScore > dealerScore:
        return win("You stood with a higher score than the dealer")
    elif stood and playerScore < dealerScore:
        return loss("You stood with a lower score than the dealer")
    elif stood and playerScore == dealerScore:
        return tie("You tied with the dealer")

    return None
