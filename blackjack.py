class BlackJackGame:
    def __init__(self, num_players):
        self.players = []
        for i in range(num_players):
            name = input(f"Enter player {i + 1}'s name: ")
            self.players.append(name)
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        scores = {}
        for player in self.players:
            score = self.play_hand(player)
            scores[player] = score
            print(f"{player}'s total score: {score}")

        # Determine the winner
        winner = max(scores, key=scores.get)
        print(f"The winner is {winner} with a score of {scores[winner]}")

    def play_hand(self, player):
        total_value = 0
        hand_cards = []

        while True:
            new_card = self.deck.get_card()
            if new_card:
                hand_cards.append(new_card)
                card_value = self.get_card_value(new_card)
                total_value += card_value
                print(f"{player} draws: {new_card} - Total score: {total_value}")

                if total_value >= 21:
                    break

                another_card = input(f"{player}, do you want another card? (yes/no): ")
                if another_card.lower() != 'yes':
                    break
            else:
                print("No more cards in the deck.")
                break

        return 0 if total_value > 21 else total_value

    def get_card_value(self, card):
        if card.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif card.rank == 'Ace':
            return 11 if sum([self.get_card_value(c) for c in hand_cards]) <= 10 else 1
        else:
            return int(card.rank)
