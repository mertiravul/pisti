# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
cardList = []
cardChooseList = []
playerCards = []
botCards = []
middleCards = []
class Card:
    def __init__(self, number, kind):
        self.number = number
        if kind == 1:
            self.kind = "♣ "
        elif kind == 2:
            self.kind = "♦ "
        elif kind == 3:
            self.kind = "♥ "
        elif kind == 4:
            self.kind = "♠ "

        if number == 1:
            self.display = "A "
        elif number == 11:
            self.display = "J "
        elif number == 12:
            self.display = "Q "
        elif number == 13:
            self.display = "K "
        elif number == 10:
            self.display = "10"
        else:
            self.display = str(number) + " "
            
    def CardValue(self):
        return self.kind + " " + str(self.display)
        
def CardSelect():
    card = random.choice(cardChooseList)
    cardChooseList.remove(card)
    return card

def PlayerCardImage(card1, card2, card3, card4):
    return """
(^^^^(^^^^(^^^^(^^^^^^^^^^^^^^^)
| """ + card1.display + """ | """ + card2.display + """ | """ + card3.display + """ | """ + card4.display + """            |
| """ + card1.kind + """ | """ + card2.kind + """ | """ + card3.kind + """ | """ + card4.kind + """            |
|    |    |    |               |
|    |    |    |               |
|    |    |    |               |
|    |    |    |               |
|    |    |    |               |
|    |    |    |               |
|    |    |    |               |
(vvvv(vvvv(vvvv(vvvvvvvvvvvvvvv)
"""
def MiddleCardImage(card1):
    return """
(^^^^^^^^^^^^^^^)
| """ + card1.display + """            |
| """ + card1.kind + """            |
|               |
|               |
|               |
|               |
|               |
|               |
|               |
(vvvvvvvvvvvvvvv)
"""
           
def CardDeal():
    for i in range(4):
        playerCards.append(cardList[CardSelect()])
        botCards.append(cardList[CardSelect()])

for i2 in range(4):
    for i in range(13):
        cardList.append(Card(i + 1, i2 + 1))
                 
for i in range(52):
    cardChooseList.append(i)
             



for i in range(4):
    middleCards.append(cardList[CardSelect()])
CardDeal()


print(MiddleCardImage(middleCards[3]))
print(PlayerCardImage(playerCards[0], playerCards[1], playerCards[2], playerCards[3]))

    
    


                 
                 
                 
                 
