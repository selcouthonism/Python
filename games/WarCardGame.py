import random

class Card():
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} - {self.suit}"
        #return f"Suit is {self.suit}, Rank is {self.rank}"

class Deck():
    def __init__(self):
        self.card_list = []
    
    def __create(self):
        suits = ["Clubs (¦)", "Diamonds (¦)", "Hearts (¦)", "Spades (¦)"]
    
        for suit in suits:
            for value in range(2,11):
                self.card_list.append(Card(suit,str(value),value))
            self.card_list.append(Card(suit,"J",11))
            self.card_list.append(Card(suit,"Q",12))
            self.card_list.append(Card(suit,"K",13))
            self.card_list.append(Card(suit,"A",14))
    
    def __shuffle(self):
        random.shuffle(self.card_list)
    
    def split_cards(self):
        self.__create()
        self.__shuffle()
        '''return list in tuple'''
        index = int(len(self.card_list)/2)
        return (self.card_list[0 : index], self.card_list[index : ])

class Player():
    #def __init__(self):
        #self.card_queue = card_queue
    
    def take_deck(self,card_queue):
        self.card_queue = card_queue
        
    def add_to_queue(self,won_cards):
        ''' This method will take cards in list '''
        for card in won_cards:
            self.card_queue.append(card)
    
    def is_card_available(self):
        return self.card_queue
    
    def reveal_the_top_card(self):
        return self.card_queue.pop(0)
    
    def battle_cards(self, number_of_cards):
        return [self.card_queue.pop(0) for number in range(0,number_of_cards) if self.is_card_available()]
    
    def __str__(self):
        return f"Player has {len(self.card_queue)} number of cards"
    
    def __len__(self):
        return len(self.card_queue)

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def start(self):
        deck = Deck()
        first_half, second_half = deck.split_cards()
        self.player1.take_deck(first_half)
        self.player2.take_deck(second_half)
    
    def __display_card_and_player(self,card1,card2, player1, player2, winner="No One",):
        print(f"{card1} : {card2}  -> winner is {winner}\t |P1: {len(player1)} P2: {len(player2)}|")
    
    def __display(self,card1,card2, winner="No One", war = ''):
        print(f"{card1} : {card2}  -> winner is {winner}  {war}")
    
    def play(self):
        while self.player1.is_card_available() and self.player2.is_card_available():
            card1 = self.player1.reveal_the_top_card()
            card2 = self.player2.reveal_the_top_card()
            
            if card1.value > card2.value:
                self.player1.add_to_queue([card1,card2])
                winner = "Player 1"
            elif card1.value < card2.value:
                self.player2.add_to_queue([card1,card2])
                winner = "Player 2"
            else:
                battle_list = []
                while card1.value == card2.value:
                    self.__display(card1, card2, war="WAR")
                    battle_list.append(card1)
                    battle_list.append(card2)
                    battle_list.extend(self.player1.battle_cards(3))
                    battle_list.extend(self.player2.battle_cards(3))
                    
                    card1 = self.player1.reveal_the_top_card()
                    card2 = self.player2.reveal_the_top_card()
                
                winning_player = self.player1 if card1.value > card2.value else self.player2
                winning_player.add_to_queue(battle_list)
                winning_player.add_to_queue([card1,card2])
                winner = "Player 1" if card1.value > card2.value else "Player 2"

            self.__display(card1, card2, winner)
            #self.__display_card_and_player(card1, card2, self.player1, self.player2, winner)
        
        game_winner = "Player 1" if self.player1.is_card_available() else "Player 2"
        print(f"Winner of the game is {game_winner}")

game = Game(Player(),Player())
game.start()
game.play()
