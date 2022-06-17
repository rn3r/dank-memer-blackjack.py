import cards as util
import constants as Constants
import logic
import os

stood = False
outcome = None

hands = {
    "Player": [],
    "Dealer": []
}

def displayRender(render):
    print(f'{render["description"]}\n')
    for field in render["fields"]:
        print(f"{field['title']}\n{field['value']}\n")

for i in range(2):
    util.deal(hands["Player"], True)
    util.deal(hands["Dealer"], True)

while 1:
    getRender = logic.renderData(hands["Player"], hands["Dealer"], stood, outcome)
    os.system("clear")
    displayRender(getRender)

    outcome = logic.getOutcome(hands["Player"], hands["Dealer"], stood)
    print((Constants.Outcomes(outcome.outcome).outcome["message"], outcome.reason) if outcome else None)

    choice = input("hit/stand/end\n>> ")

    if choice.lower() == "hit":
        util.deal(hands["Player"], False)
    elif choice.lower() == "stand":
        stood = True
        while(util.countHand(hands["Dealer"]) < Constants.BJ_DEALER_MAX):
            util.deal(hands["Dealer"], False)
    elif choice.lower() == "end":
        exit("Requested exit")
