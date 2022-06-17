BJ_WIN = 21
BJ_DEALER_MAX = 17
BJ_FACE = 10
BJ_ACE_MIN = 1
BJ_ACE_MAX = 11

SUITS = [
    '♠', '♥', '♦', '♣'
]

FACES = [
    num + 2 for num in range(9)
] + ['A', 'J', 'K', 'Q']

class Outcome():
    def __init__(self, WIN, LOSS, TIE, OTHER):
        self.WIN = WIN
        self.LOSS = LOSS
        self.TIE = TIE
        self.OTHER = OTHER

class Outcomes:
    def __init__(self, outcome):
        m = [{ 'message' : 'You win!', 'color': 0x4CAF50 },
            { 'message' : 'You lost ):', 'color': 0xE53935 },
            { 'message' : 'You tied.', 'color': 0xFFB300 },
            { 'message' : '', 'color': 0xFFB300 }]
        self.outcome = (m[0] if outcome.WIN else m[1] if outcome.LOSS else m[2] if outcome.TIE else m[3])

class OutcomeResult:
    def __init__(self, outcome: Outcome, reason: str, extra: str = None):
        self.outcome = outcome
        self.reason = reason
        self.extra = extra
        
