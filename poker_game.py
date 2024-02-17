import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]

class PokerGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = Deck()
        self.deck.shuffle()
        self.players = {f"Player {i+1}": [] for i in range(num_players)}

    def deal_cards(self, num_cards):
        for _ in range(num_cards):
            for player in self.players:
                self.players[player].append(self.deck.cards.pop())

    def display_hands(self):
        for player, hand in self.players.items():
            print(f"{player}'s Hand: {', '.join(map(str, hand))}")

def main():
    num_players = int(input("Enter the number of players: "))
    game = PokerGame(num_players)
    game.deal_cards(5)
    game.display_hands()

if __name__ == "__main__":
    main()
