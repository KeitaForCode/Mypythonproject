###############################################
######### ----------PROJECT ---------##########
###############################################



#FOR THIS PROJECT I WILL BE USING OOP TO CREATE A CARD GAME, THIS CARD GAME WILL BE THE
#CARD GAME 'WAR' FOR TWO PLAYERS, YOU AND THE COMPUTER. IF YOU DON'T KNOW HOW TO PLAY WAR
#HERE IS THE BASIC RULES

#THE DECK IS DEVIDED EVENLY, WITH EACH PLAYERS RECEIVING 26 CARDS, DEALT ONE AT A TIME
#FACE DOWN. ANYONE MAY DEAL FIRST. EACH PLAYER PLACES HIS STACK OF CARDS FACE DOWN.

#THE PLAY

#EACH PLAYER TURNS UP A CARD AT THE SAME TIME AND THE PLAYER WITH THE HIGHER CARD TAKES
#BOTH CARDS AND PUT THEM, FACE DOWN, ON THE BOTTOM OF HIS STACK.

#IF THE CARDS ARE THE SAME RANK, IT IS WAR, EACH PLAYER TURNS UP THREE CARDS FACE DOWN
#AND ONE CARD FACE UP, THE PLAYER WITH WITH HIGHER CARDS TAKES BOTH PILES(SIX CARDS).
#IF THE TURN UP CARDS ARE AGAIN THE SAME RANK, EACH PLAYER PLACES ANOTHER CARD FACE DOWN
#AND TURNS ANOTHER CARD FACE UP, THE PLAYER WITH THE HIGHER CARDS TAKES ALL TEN CARDS AND SO ON


from random import shuffle

#two useful variation for creating cards
suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

mycards = [(s,r) for s in suite for r in ranks]

class Deck:
    '''
    This is the deck class, this objeck will create the deck of cards to initiate play.
    You can use this Deck list of cards to split in half and give to the players. it
    will use suite and rank to create the deck, it should also have a method for splitting/
    cutting in half and shuffling the deck
    '''

    def __init__(self):
        print('Creating new ordered deck')
        self.allcards = [(s,r) for s in suite for r in ranks]

    def shuffle(self):
        print('shuffling deck')
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    '''
    This is the hand class, each player has a hand and can add or remove class from that hand
    there should be an add or remove card method here
    '''

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return 'contains {} cards'.format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    '''
    This is the player class, which take in a name and an instance of hand class object.
    The player can then play cards and check if they still have cards
    '''

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print('{} has placed: {}'.format(self.name, drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        '''
        This will return true if player still has card left
        '''
        return len(self.hand.cards) != 0


###############################################
######### ----------Game play ---------########
###############################################

print("WELCOME TO WAR, LET'S BEGIN")

# create a new deck and split it in half:

d = Deck()
d.shuffle()

half1, half2 = d.split_in_half()

#create both players:

comp = Player('Computer',Hand(half1))

name = input('What is your name?: ')

user = Player(name,Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print('Time for the new round')
    print('Here is the current standing')
    print(user.name + ' has the count: '+str(len(user.hand.cards)))
    print(comp.name + ' has the count: '+str(len(comp.hand.cards)))
    print('Play a card')
    print('\n')

    table_cards = []

    c_cards = comp.play_card()
    p_cards = user.play_card()

    table_cards.append(c_cards)
    table_cards.append(p_cards)


    if c_cards[1] == p_cards[1]:
        war_count +=1

        print('War!')

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if ranks.index(c_cards[1]) < ranks.index(p_cards[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if ranks.index(c_cards[1]) < ranks.index(p_cards[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print('Gave over, number of round: '+str(total_rounds))
print('a war happened '+str(war_count) + ' times')

print('Does the computer still has card? ')
print(str(comp.still_has_cards()))

print('Does the user still has card? ')
print(str(user.still_has_cards()))
