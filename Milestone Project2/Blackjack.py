'''
Falta definir deck.deal     hand.adjust_for_ace

continuar con el resto
'''



import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


playing = True


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
            
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    
    def __str__(self):
        '''
        i=0
        for card in self.deck:
            print(i)
            i+=1
            print(f"Card is {card} and its value is {values[card.rank]}")
        '''

        return ' --'.join(str (e) for e in self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.card = card
        self.cards.append(self.card)
        self.value += values[self.card.rank]
        if self.card.rank == 'Ace':
            self.aces += 1
        

    
    def adjust_for_ace(self,):

        pass

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        print(f"You won. You have {self.total} remaining chips.")
        
    
    def lose_bet(self):
        self.total -= self.bet
        print(f"You lost. You have {self.total} remaining chips.")


def take_bet(Chips):
    while True:
        try:
            Chips.bet = int(input("Enter your bet:"))
        except:
            print("Enter a number")
        else:
            if Chips.bet > Chips.total:
                print("You can't bet more than you have...")
                
            else:
                print("Ok, beat taken.")
                break





def hit(deck,hand):
    
    card_played = test_deck.deal()
    hand.add_card(card_played)
    print(f"This card is {card_played}")
    print(values[card_played.rank])

#************************************************************************

test_deck = Deck()
player_chips = Chips()
print("going to print")
print(test_deck)
test_deck.shuffle()
print("...Shuffling....")
print(test_deck)

print("...Shuffled....")

take_bet(player_chips)

print("****test hit***")
test_hand = Hand()


hit(test_deck,test_hand)


