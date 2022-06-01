import random

changedir = [('CHANGEDIRECTION', 'RED'), ('CHANGEDIRECTION', 'RED'), ('CHANGEDIRECTION', 'GREEN'), ('CHANGEDIRECTION', 'GREEN'), ('CHANGEDIRECTION', 'BLUE'), ('CHANGEDIRECTION', 'BLUE'),
 ('CHANGEDIRECTION', 'YELLOW'), ('CHANGEDIRECTION', 'YELLOW')]


unoCards = [(1, 'RED'), (2, 'RED'), (3, 'RED'), (4, 'RED'), (5, 'RED'), (6, 'RED'), (7, 'RED'), (8, 'RED'), (9, 'RED'),
            (1, 'GREEN'), (2, 'GREEN'), (3, 'GREEN'), (4, 'GREEN'), (5, 'GREEN'), (6, 'GREEN'), (7, 'GREEN'), (8, 'GREEN'), (9, 'GREEN'),
            (1, 'BLUE'), (2, 'BLUE'), (3, 'BLUE'), (4, 'BLUE'), (5, 'BLUE'), (6, 'BLUE'), (7, 'BLUE'), (8, 'BLUE'), (9, 'BLUE'),
            (1, 'YELLOW'), (2, 'YELLOW'), (3, 'YELLOW'), (4, 'YELLOW'), (5, 'YELLOW'), (6, 'YELLOW'), (7, 'YELLOW'), (8, 'YELLOW'), (9, 'YELLOW'),
            ('+2', 'RED'), ('STOP', 'RED'),  ('+2', 'RED'), ('STOP', 'RED'), 
            ('+2', 'GREEN'), ('STOP', 'GREEN'),  ('+2', 'GREEN'), ('STOP', 'GREEN'), 
            ('+2', 'BLUE'), ('STOP', 'BLUE'),  ('+2', 'BLUE'), ('STOP', 'BLUE'), 
            ('+2', 'YELLOW'), ('STOP', 'YELLOW'),  ('+2', 'YELLOW'), ('STOP', 'YELLOW'), 
            ('WILD', 'COLORCHANGE'), ('WILD', 'COLORCHANGE'), ('WILD', 'COLORCHANGE'), ('WILD', 'COLORCHANGE'), ('WILD', '+4'), ('WILD', '+4'), ('WILD', '+4'), ('WILD', '+4')
            ]

backupUnoCards = [(1, 'RED'), (2, 'RED'), (3, 'RED'), (4, 'RED'), (5, 'RED'), (6, 'RED'), (7, 'RED'), (8, 'RED'), (9, 'RED'),
            (1, 'GREEN'), (2, 'GREEN'), (3, 'GREEN'), (4, 'GREEN'), (5,
                                                                     'GREEN'), (6, 'GREEN'), (7, 'GREEN'), (8, 'GREEN'), (9, 'GREEN'),
            (1, 'BLUE'), (2, 'BLUE'), (3, 'BLUE'), (4, 'BLUE'), (5,
                                                                 'BLUE'), (6, 'BLUE'), (7, 'BLUE'), (8, 'BLUE'), (9, 'BLUE'),
            (1, 'YELLOW'), (2, 'YELLOW'), (3, 'YELLOW'), (4, 'YELLOW'), (5,
                                                                         'YELLOW'), (6, 'YELLOW'), (7, 'YELLOW'), (8, 'YELLOW'), (9, 'YELLOW'),
            ('+2', 'RED'), ('STOP', 'RED'), ('CHANGEDIRECTION', 'RED'), ('+2',
                                                                'RED'), ('STOP', 'RED'), ('CHANGEDIRECTION', 'RED'),
            ('+2', 'GREEN'), ('STOP', 'GREEN'), ('CHANGEDIRECTION', 'GREEN'), ('+2',
                                                                      'GREEN'), ('STOP', 'GREEN'), ('CHANGEDIRECTION', 'GREEN'),
            ('+2', 'BLUE'), ('STOP', 'BLUE'), ('CHANGEDIRECTION', 'BLUE'), ('+2',
                                                                   'BLUE'), ('STOP', 'BLUE'), ('CHANGEDIRECTION', 'BLUE'),
            ('+2', 'YELLOW'), ('STOP', 'YELLOW'), ('CHANGEDIRECTION', 'YELLOW'), ('+2',
                                                                         'YELLOW'), ('STOP', 'YELLOW'), ('CHANGEDIRECTION', 'YELLOW'),
            ('WILD', 'COLORCHANGE'), ('WILD', 'COLORCHANGE'), ('WILD', 'COLORCHANGE'), ('WILD',
                                                                                        'COLORCHANGE'), ('WILD', '+4'), ('WILD', '+4'), ('WILD', '+4'), ('WILD', '+4')
            ]

startCards = [(1, 'RED'), (2, 'RED'), (3, 'RED'), (4, 'RED'), (5, 'RED'), (6, 'RED'), (7, 'RED'), (8, 'RED'), (9, 'RED'),
             (1, 'GREEN'), (2, 'GREEN'), (3, 'GREEN'), (4, 'GREEN'), (5,
                                                                      'GREEN'), (6, 'GREEN'), (7, 'GREEN'), (8, 'GREEN'), (9, 'GREEN'),
             (1, 'BLUE'), (2, 'BLUE'), (3, 'BLUE'), (4, 'BLUE'), (5,
                                                                  'BLUE'), (6, 'BLUE'), (7, 'BLUE'), (8, 'BLUE'), (9, 'BLUE'),
             (1, 'YELLOW'), (2, 'YELLOW'), (3, 'YELLOW'), (4, 'YELLOW'), (5,
                                                                          'YELLOW'), (6, 'YELLOW'), (7, 'YELLOW'), (8, 'YELLOW'), (9, 'YELLOW'),
             ]


player1Deck = [('DRAW')]
player2Deck = [('DRAW')]
player3Deck = [('DRAW')]
player4Deck = [('DRAW')]

lastCards = [('4p', 'UNO!'), ('3p', 'UNO!'), ('2p', 'UNO!'), ('1p', 'UNO!')]

colorchanges = [('-', 'RED'), ('-', 'BLUE'), ('-', 'GREEN'), ('-', 'YELLOW')]
plus4 = [('-', 'RED'), ('-', 'BLUE'), ('-', 'GREEN'), ('-', 'YELLOW')]


def shuffle_cards():
    # shuffling the whole main deck of cards
    random.shuffle(unoCards)


def add_cards_to_deck(playerDeckNumber, amountOfCards):
    # adding cards to player's deck
    for _ in range(amountOfCards):
        randomCard = random.choice(unoCards)
        playerDeckNumber.append(randomCard)
        unoCards.remove(randomCard)
        shuffle_cards()


def play_card(playerDeckNumber, card):
    playerDeckNumber.remove(card)


def show_hand(playerDeckNumber):
    print(playerDeckNumber)


def uno(playerDeckNumber):
    if playerDeckNumber == player1Deck:
        print('========================')
        print('        Player 1        ')
        print('          UNO           ')
        print('========================')
    elif playerDeckNumber == player2Deck:
        print('========================')
        print('        Player 2        ')
        print('          UNO           ')
        print('========================')
    elif playerDeckNumber == player3Deck:
        print('========================')
        print('        Player 3        ')
        print('          UNO           ')
        print('========================')
    elif playerDeckNumber == player4Deck:
        print('========================')
        print('        Player 4        ')
        print('          UNO           ')
        print('========================')


def valid_move(pileCard, playerDeck, indexOfCardToPlay):
    # split card into 2 parts (number, color)
    # check if at least one part is playable
    # if so change top card on pile and remove card from players deck
    # if not print message and give another try
    # add 'take card' move to options
    pass


print("""
        This is the UNO game.
        In this game you have to get rid of all cards in your deck.
        But obviously there are some rules.
        You can only throw card with the same color or number as card before you.
        Black card is the exception. You can use black cards whenever your want.
        To chose card you have to enter index of the card if asked (draw card is 0, then start counting from 1)
""")


cards_amount = int(input('Please enter how many cards in one deck (6-10): '))
add_cards_to_deck(player1Deck, cards_amount)
add_cards_to_deck(player2Deck, cards_amount)
add_cards_to_deck(player3Deck, cards_amount)
add_cards_to_deck(player4Deck, cards_amount)


playing = True
movingPlayer = 1
pile = []
pile.append(random.choice(startCards))
if 3 <= cards_amount <= 10:
    while playing:
        playDirection = 1
        topCard = pile[-1]

        if movingPlayer == 1:
            if len(player4Deck) == 2:
                uno(player4Deck)
        elif movingPlayer == 2:
            if len(player1Deck) == 2:
                uno(player1Deck)
        elif movingPlayer == 3:
            if len(player2Deck) == 2:
                uno(player2Deck)
        elif movingPlayer == 4:
            if len(player3Deck) == 2:
                uno(player3Deck)

        print('===================================')
        print(f'Card on top of the pile: {pile[-1]}')

        if movingPlayer > 4:
            movingPlayer = 1

        if movingPlayer == 1:
            show_hand(f'Player\'s 1 deck - {player1Deck}')
            
        elif movingPlayer == 2:
            show_hand(f'Player\'s 2 deck - {player2Deck}')
            
        elif movingPlayer == 3:
            show_hand(f'Player\'s 3 deck - {player3Deck}')
            
        elif movingPlayer == 4:
            show_hand(f'Player\'s 4 deck - {player4Deck}')
            

        if len(player1Deck) == 1:
            print('========================')
            print('       Game Over        ')
            print('========================')
            print(' Player 1 Won The Game! ')
            playing == False


        elif len(player2Deck) == 1:
            print('========================')
            print('       Game Over        ')
            print('========================')
            print(' Player 2 Won The Game! ')
            playing == False


        elif len(player3Deck) == 1:
            print('========================')
            print('       Game Over        ')
            print('========================')
            print(' Player 3 Won The Game! ')
            playing == False


        elif len(player4Deck) == 1:
            print('========================')
            print('       Game Over        ')
            print('========================')
            print(' Player 4 Won The Game! ')
            playing == False
            
        

        cardToPlayIndex = int(input('Choose card to play: '))


        if movingPlayer == 1: 
            if cardToPlayIndex > len(player1Deck) - 1:
                print('Wrong card index! Try again.')
                continue
   
            elif player1Deck[cardToPlayIndex][0] == topCard[0] or player1Deck[cardToPlayIndex][1] == topCard[1]:
                if player1Deck[cardToPlayIndex][0] == '+2':
                    pile.append(player1Deck[cardToPlayIndex])
                    player1Deck.pop(cardToPlayIndex)
                    add_cards_to_deck(player2Deck, 2)
                    print('Added 2 cards to Next Player\'s deck')
                    movingPlayer += playDirection
                elif player1Deck[cardToPlayIndex][0] == 'STOP':
                    pile.append(player1Deck[cardToPlayIndex])
                    player1Deck.pop(cardToPlayIndex)
                    print('Oh no! Next player has been blocked... Skipping to player no. 3.')
                    movingPlayer += (playDirection * 2)
                elif player1Deck[cardToPlayIndex][0] == 'CHANGEDIRECTION':
                    pile.append(player1Deck[cardToPlayIndex])
                    player1Deck.pop(cardToPlayIndex)
                    print('Changing direction... Done!')
                    playDirection * -1
                else:
                    pile.append(player1Deck[cardToPlayIndex])
                    player1Deck.pop(cardToPlayIndex)
                    print('Card has been successfully played.')
                    movingPlayer += playDirection

            elif player1Deck[cardToPlayIndex][0] == 'WILD':
                if player1Deck[cardToPlayIndex][1] == 'COLORCHANGE':
                    color = int(input("""
                                What color do you want to change to? 
                                1 - RED
                                2 - BLUE
                                3 - GREEN
                                4 - YELLOW
                    """))
                    if color == 1:
                        pile.append(colorchanges[0])
                        player1Deck.pop(cardToPlayIndex)
                        movingPlayer += playDirection
                        print(f'Color changed to {colorchanges[0][1]}')
                    elif color == 2:
                        pile.append(colorchanges[1])
                        player1Deck.pop(cardToPlayIndex)
                        movingPlayer += playDirection
                        print(f'Color changed to {colorchanges[1][1]}')
                    elif color == 3:
                        pile.append(colorchanges[2])
                        player1Deck.pop(cardToPlayIndex)
                        movingPlayer += playDirection
                        print(f'Color changed to {colorchanges[2][1]}')
                    elif color == 4:
                        pile.append(colorchanges[3])
                        player1Deck.pop(cardToPlayIndex)
                        movingPlayer += playDirection
                        print(f'Color changed to {colorchanges[3][1]}')
                    else:
                        print('Wrong number! Choose between (1-4)')

                elif player1Deck[cardToPlayIndex][1] == '+4':
                    color = int(input("""
                                What color do you want to change to? 
                                1 - RED
                                2 - BLUE
                                3 - GREEN
                                4 - YELLOW
                    """))
                    if color == 1:
                        pile.append(plus4[0])
                        player1Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player2Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer += playDirection
                        print(f'Color changed to {plus4[0][1]}')
                    elif color == 2:
                        pile.append(plus4[1])
                        player1Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player2Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer += playDirection
                        print(f'Color changed to {plus4[1][1]}')
                    elif color == 3:
                        pile.append(plus4[2])
                        player1Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player2Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer += playDirection
                        print(f'Color changed to {plus4[2][1]}')
                    elif color == 4:
                        pile.append(plus4[3])
                        player1Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player2Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer += playDirection
                        print(f'Color changed to {plus4[3][1]}')
                    else:
                        print('Wrong number! Choose between (1-4)')

            elif topCard[0] == 'WILD':
                pile.append(player1Deck[cardToPlayIndex])
                player1Deck.pop(cardToPlayIndex)
                print('Card has been successfully played.')
                movingPlayer += playDirection

            elif cardToPlayIndex == 0:
                add_cards_to_deck(player1Deck, 1)
                movingPlayer += playDirection

            else:
                print('Card can\'t be played. Try another one or use the draw card.')
                show_hand(player1Deck)


        elif movingPlayer == 2:
            if cardToPlayIndex > len(player2Deck) - 1:
                print('Wrong card index! Try again.')
                continue

            elif player2Deck[cardToPlayIndex][0] == topCard[0] or player2Deck[cardToPlayIndex][1] == topCard[1]:
                if player2Deck[cardToPlayIndex][0] == '+2':
                    pile.append(player2Deck[cardToPlayIndex])
                    player2Deck.pop(cardToPlayIndex)
                    add_cards_to_deck(player3Deck, 2)
                    print('Added 2 cards to Next Player\'s deck')
                    movingPlayer += playDirection
                elif player2Deck[cardToPlayIndex][0] == 'STOP':
                    pile.append(player2Deck[cardToPlayIndex])
                    player2Deck.pop(cardToPlayIndex)
                    print('Oh no! Next player has been blocked... Skipping to player no. 4.')
                    movingPlayer += (playDirection * 2)
                elif player2Deck[cardToPlayIndex][0] == 'CHANGEDIRECTION':
                    pile.append(player2Deck[cardToPlayIndex])
                    player2Deck.pop(cardToPlayIndex)
                    print('Changing direction... Done!')
                    playDirection * -1
                else:
                    pile.append(player2Deck[cardToPlayIndex])
                    player2Deck.pop(cardToPlayIndex)
                    print('Card has been successfully played.')
                    movingPlayer += playDirection

            elif player2Deck[cardToPlayIndex][0] == 'WILD':
                if player2Deck[cardToPlayIndex][1] == 'COLORCHANGE':
                    color = int(input("""
                                What color do you want to change to? 
                                1 - RED
                                2 - BLUE
                                3 - GREEN
                                4 - YELLOW
                    """))
                    if color == 1:
                        pile.append(colorchanges[0])
                        player2Deck.pop(cardToPlayIndex)
                        movingPlayer += playDirection
                        print(f'Color changed to {colorchanges[0][1]}')
                    elif color == 2:
                        pile.append(colorchanges[1])
                        player2Deck.pop(cardToPlayIndex)
                        movingPlayer += playDirection
                        print(f'Color changed to {colorchanges[1][1]}')
                    elif color == 3:
                        pile.append(colorchanges[2])
                        player2Deck.pop(cardToPlayIndex)
                        movingPlayer += playDirection
                        print(f'Color changed to {colorchanges[2][1]}')
                    elif color == 4:
                        pile.append(colorchanges[3])
                        player2Deck.pop(cardToPlayIndex)
                        movingPlayer += playDirection
                        print(f'Color changed to {colorchanges[3][1]}')
                    else:
                        print('Wrong number! Choose between (1-4)')

                elif player2Deck[cardToPlayIndex][1] == '+4':
                    color = int(input("""
                                What color do you want to change to? 
                                1 - RED
                                2 - BLUE
                                3 - GREEN
                                4 - YELLOW
                    """))
                    if color == 1:
                        pile.append(plus4[0])
                        player2Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player3Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer += playDirection
                        print(f'Color changed to {plus4[0][1]}')
                    elif color == 2:
                        pile.append(plus4[1])
                        player2Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player3Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer += playDirection
                        print(f'Color changed to {plus4[1][1]}')
                    elif color == 3:
                        pile.append(plus4[2])
                        player2Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player3Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer += playDirection
                        print(f'Color changed to {plus4[2][1]}')
                    elif color == 4:
                        pile.append(plus4[3])
                        player2Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player3Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer += playDirection
                        print(f'Color changed to {plus4[3][1]}')
                    else:
                        print('Wrong number! Choose between (1-4)')

            elif topCard[0] == 'WILD':
                pile.append(player2Deck[cardToPlayIndex])
                player2Deck.pop(cardToPlayIndex)
                print('Card has been successfully played.')
                movingPlayer += playDirection

            elif cardToPlayIndex == 0:
                add_cards_to_deck(player2Deck, 1)
                movingPlayer += playDirection

            else:
                print('Card can\'t be played. Try another one or use the draw card.')
                show_hand(player2Deck)

        elif movingPlayer == 3:
            if cardToPlayIndex > len(player3Deck) - 1:
                print('Wrong card index! Try again.')
                continue

            elif player3Deck[cardToPlayIndex][0] == topCard[0] or player3Deck[cardToPlayIndex][1] == topCard[1]:
                if player3Deck[cardToPlayIndex][0] == '+2':
                    pile.append(player3Deck[cardToPlayIndex])
                    player3Deck.pop(cardToPlayIndex)
                    add_cards_to_deck(player4Deck, 2)
                    print('Added 2 cards to Next Player\'s deck')
                    movingPlayer += playDirection
                elif player3Deck[cardToPlayIndex][0] == 'STOP':
                    pile.append(player3Deck[cardToPlayIndex])
                    player3Deck.pop(cardToPlayIndex)
                    print('Oh no! Next player has been blocked... Skipping to player no. 1.')
                    movingPlayer += (playDirection * 2)
                elif player3Deck[cardToPlayIndex][0] == 'CHANGEDIRECTION':
                    pile.append(player3Deck[cardToPlayIndex])
                    player3Deck.pop(cardToPlayIndex)
                    print('Changing direction... Done!')
                    playDirection * -1
                else:
                    pile.append(player3Deck[cardToPlayIndex])
                    player3Deck.pop(cardToPlayIndex)
                    print('Card has been successfully played.')
                    movingPlayer += playDirection

            elif player3Deck[cardToPlayIndex][0] == 'WILD':
                if player3Deck[cardToPlayIndex][1] == 'COLORCHANGE':
                    color = int(input("""
                                What color do you want to change to? 
                                1 - RED
                                2 - BLUE
                                3 - GREEN
                                4 - YELLOW
                    """))
                    if color == 1:
                        pile.append(colorchanges[0])
                        player3Deck.pop(cardToPlayIndex)
                        movingPlayer += playDirection
                        print(f'Color changed to {colorchanges[0][1]}')
                    elif color == 2:
                        pile.append(colorchanges[1])
                        player3Deck.pop(cardToPlayIndex)
                        movingPlayer += playDirection
                        print(f'Color changed to {colorchanges[1][1]}')
                    elif color == 3:
                        pile.append(colorchanges[2])
                        player3Deck.pop(cardToPlayIndex)
                        movingPlayer += playDirection
                        print(f'Color changed to {colorchanges[2][1]}')
                    elif color == 4:
                        pile.append(colorchanges[3])
                        player3Deck.pop(cardToPlayIndex)
                        movingPlayer += playDirection
                        print(f'Color changed to {colorchanges[3][1]}')
                    else:
                        print('Wrong number! Choose between (1-4)')

                elif player3Deck[cardToPlayIndex][1] == '+4':
                    color = int(input("""
                                What color do you want to change to? 
                                1 - RED
                                2 - BLUE
                                3 - GREEN
                                4 - YELLOW
                                    """))
                    if color == 1:
                        pile.append(plus4[0])
                        player3Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player4Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer += playDirection
                        print(f'Color changed to {plus4[0][1]}')
                    elif color == 2:
                        pile.append(plus4[1])
                        player3Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player4Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer += playDirection
                        print(f'Color changed to {plus4[1][1]}')
                    elif color == 3:
                        pile.append(plus4[2])
                        player3Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player4Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer += playDirection
                        print(f'Color changed to {plus4[2][1]}')
                    elif color == 4:
                        pile.append(plus4[3])
                        player3Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player4Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer += playDirection
                        print(f'Color changed to {plus4[3][1]}')
                    else:
                        print('Wrong number! Choose between (1-4)')

            elif topCard[0] == 'WILD':
                pile.append(player3Deck[cardToPlayIndex])
                player3Deck.pop(cardToPlayIndex)
                print('Card has been successfully played.')
                movingPlayer += playDirection

            elif cardToPlayIndex == 0:
                add_cards_to_deck(player3Deck, 1)
                movingPlayer += playDirection

            else:
                print('Card can\'t be played. Try another one or use the draw card.')
                show_hand(player3Deck)

        elif movingPlayer == 4:
            if cardToPlayIndex > len(player4Deck) - 1:
                print('Wrong card index! Try again.')
                continue

            elif player4Deck[cardToPlayIndex][0] == topCard[0] or player4Deck[cardToPlayIndex][1] == topCard[1]:
                if player4Deck[cardToPlayIndex][0] == '+2':
                    pile.append(player4Deck[cardToPlayIndex])
                    player4Deck.pop(cardToPlayIndex)
                    add_cards_to_deck(player1Deck, 2)
                    print('Added 2 cards to Next Player\'s deck')
                    movingPlayer = 1
                elif player4Deck[cardToPlayIndex][0] == 'STOP':
                    pile.append(player4Deck[cardToPlayIndex])
                    player4Deck.pop(cardToPlayIndex)
                    print('Oh no! Next player has been blocked... Skipping to player no. 2.')
                    movingPlayer = 2
                elif player4Deck[cardToPlayIndex][0] == 'CHANGEDIRECTION':
                    pile.append(player4Deck[cardToPlayIndex])
                    player4Deck.pop(cardToPlayIndex)
                    print('Changing direction... Done!')
                    playDirection * -1
                else:
                    pile.append(player4Deck[cardToPlayIndex])
                    player4Deck.pop(cardToPlayIndex)
                    print('Card has been successfully played.')
                    movingPlayer = 1

            elif player4Deck[cardToPlayIndex][0] == 'WILD':
                if player4Deck[cardToPlayIndex][1] == 'COLORCHANGE':
                    color = int(input("""
                                What color do you want to change to? 
                                1 - RED
                                2 - BLUE
                                3 - GREEN
                                4 - YELLOW
                    """))
                    if color == 1:
                        pile.append(colorchanges[0])
                        player4Deck.pop(cardToPlayIndex)
                        movingPlayer = 1
                        print(f'Color changed to {colorchanges[0][1]}')
                    elif color == 2:
                        pile.append(colorchanges[1])
                        player4Deck.pop(cardToPlayIndex)
                        movingPlayer = 1
                        print(f'Color changed to {colorchanges[1][1]}')
                    elif color == 3:
                        pile.append(colorchanges[2])
                        player4Deck.pop(cardToPlayIndex)
                        movingPlayer = 1
                        print(f'Color changed to {colorchanges[2][1]}')
                    elif color == 4:
                        pile.append(colorchanges[3])
                        player4Deck.pop(cardToPlayIndex)
                        movingPlayer = 1
                        print(f'Color changed to {colorchanges[3][1]}')
                    else:
                        print('Wrong number! Choose between (1-4)')

                elif player4Deck[cardToPlayIndex][1] == '+4':
                    color = int(input("""
                                What color do you want to change to? 
                                1 - RED
                                2 - BLUE
                                3 - GREEN
                                4 - YELLOW
                    """))
                    if color == 1:
                        pile.append(plus4[0])
                        player4Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player1Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer = 1
                        print(f'Color changed to {plus4[0][1]}')
                    elif color == 2:
                        pile.append(plus4[1])
                        player4Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player1Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer = 1
                        print(f'Color changed to {plus4[1][1]}')
                    elif color == 3:
                        pile.append(plus4[2])
                        player4Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player1Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer = 1
                        print(f'Color changed to {plus4[2][1]}')
                    elif color == 4:
                        pile.append(plus4[3])
                        player4Deck.pop(cardToPlayIndex)
                        add_cards_to_deck(player1Deck, 4)
                        print('Added 4 cards to Next Player\'s deck.')
                        movingPlayer = 1
                        print(f'Color changed to {plus4[3][1]}')
                    else:
                        print('Wrong number! Choose between (1-4)')

            elif topCard[0] == 'WILD':
                pile.append(player4Deck[cardToPlayIndex])
                player4Deck.pop(cardToPlayIndex)
                print('Card has been successfully played.')
                movingPlayer = 1

            elif cardToPlayIndex == 0:
                add_cards_to_deck(player4Deck, 1)
                movingPlayer = 1

            else:
                print('Card can\'t be played. Try another one or use the draw card.')
                show_hand(player4Deck)
else:
    print('Wrong amount of cards! Choose between (6-10).')