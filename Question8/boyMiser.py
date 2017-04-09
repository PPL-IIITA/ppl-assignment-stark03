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

    def NewGifting(self, gMaintainanceCost, Gifts, giftBasket):

        """Allocates gifts with the new gifting Strategy"""

        index = []
        index.append(self.getGift("Essential", Gifts, giftBasket))
        index.append(self.getGift("Luxury", Gifts, giftBasket))
        index.append(self.getGift("Utility", Gifts, giftBasket))

        index.sort()
        j = index[2]

        cost = gMaintainanceCost
        while (j < int(Gifts.__len__()) and cost > 0):
                self.amountSpent += Gifts[j].price
                temp = [Gifts[j].giftType, Gifts[j].price, Gifts[j].value]
                giftBasket.append(temp)
                cost -= Gifts[j].price
                j += 1

    def getGift(self, type, Gifts, giftBasket):

        """Allocates one gift of each type"""

        Gifts.sort(key=operator.attrgetter('price'))
        i = 0
        while (Gifts[i].giftType != type):
            i += 1

        self.amountSpent += Gifts[i].price
        temp = [Gifts[i].giftType, Gifts[i].price, Gifts[i].value]
        giftBasket.append(temp)

        return i