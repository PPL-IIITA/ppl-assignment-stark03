import operator
from Boys import Boy

class boyMiser(Boy):

    """Boy class for boyType = 'Miser'"""
    def __init__(self, boy):
        """constructor , calls the parent constructor and initializes other attributes as:-
            happiness = happiness of the boy
            amountSpent = amount spent on gifting
            gfName = name of the girlfriend
        """
        Boy.__init__(self,boy)
        self.amountSpent = 0
        self.gfName = ""
        self.happiness = 0



    def gifting(self, gMaintainanceCost , Gifts , giftBasket):

        "Sets up the gift basket for Miser boys"

        Gifts.sort(key=operator.attrgetter('price'))
        if gMaintainanceCost < Gifts[0].price:
            self.amountSpent = Gifts[0].price
            temp = [Gifts[0].giftType, Gifts[0].price, Gifts[0].value]
            giftBasket.append(temp)

        else:
            cost = gMaintainanceCost
            i = 0
            while cost > 0:
                self.amountSpent += Gifts[i].price
                temp = [Gifts[i].giftType, Gifts[i].price, Gifts[i].value]
                giftBasket.append(temp)
                cost -= Gifts[i].price
                i += 1

    def happinessCalculator(self):

        "Calculates happiness for Miser boys"

        rem = self.budget - self.amountSpent
        if rem > 0:
            self.happiness = rem
        else:
            self.happiness = 0
