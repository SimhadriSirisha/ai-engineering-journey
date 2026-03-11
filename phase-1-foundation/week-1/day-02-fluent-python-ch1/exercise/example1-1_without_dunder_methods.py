import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]


deck = FrenchDeck()
# print(len(deck)) - this is not possible without dunder methods, need to define __len__ method
# print(deck[0]) - this is not possible without dunder methods, need to define __getitem__ method

# to get the len now without dunder methods
print(len(deck._cards))

# to get the item now without dunder methods
print(deck._cards[0])