class Card():

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'Jack', 'Queen', 'King']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank


class Deck():

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self, i=-1):
        return self.cards.pop(i)

    def remove_card(self, card):
        self.cards.remove(card)

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_hand, num_cards):
        d = Deck()
        d.shuffle()
        hands = dict()
        for i in range(num_hand):
            name = 'hand_'+str(i)
            h = Hand(label=name)
            d.move_cards(h, num_cards)
            hands[f'hand_{i}'] = h
        return list(hands.values())

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label


class PokerHand(Hand):

    def suit_hist(self):
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self, num_pair=2):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= num_pair:
                return True
        return False

    def two_pair(self):
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                count += 1
        if count >=2: return True
        else: return False

    def tree_of_kind(self, num_pair=3):
        return self.has_pair(self, 3)

    def straight(self):
        self.rank_hist()
        self.ranks.values().sort()
        if len(self.ranks.value()) < 5:
            return False

d = Deck()
a = d.deal_hands(2, 3)
print(a)
