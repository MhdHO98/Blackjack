import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self._get_ranks() for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]]

    def _get_ranks(self):
        return [str(n) for n in range(1, 11)] + ['Jack', 'Queen', 'King']

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        return self.cards.pop() if self.cards else None
