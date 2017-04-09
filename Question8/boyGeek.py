import operator
from Boys import Boy

class boyGeek(Boy):

    """Boy class for boyType = 'Geek'"""

    def __init__(self, boy):
        """constructor , calls the parent constructor and initializes other attributes as:-
                    happiness = happiness of the boy
                    amountSpent = amount spent on gifting
                    gfName = name of the girlfriend
        """
        Boy.__init__(self,boy)
        self.happiness = 0
        self.gfName = ""
        self.amountSpent = 0

    def happinessCalculator(self , gIntelligence):
        "Calculates happiness for Geek boys"
        self.happiness = gIntelligence

    def gifting(self, gMaintainanceCost , Gifts , giftBasket ,index):


        "Sets up the gift basket for Miser boys"

        Gifts.sort(key=operator.attrgetter('price'))
        i = 0
        if(gMaintainanceCost < Gifts[0].price):
            self.amountSpent = Gifts[0].price
            temp = [Gifts[0].giftType, Gifts[0].price, Gifts[0].value]
            giftBasket.append(temp)

        else:
            cost = gMaintainanceCost
            while(cost > 0):
                self.amountSpent += Gifts[i].price
                temp = [Gifts[i].giftType, Gifts[i].price, Gifts[i].value]
                giftBasket.append(temp)
                cost -= Gifts[i].price
                i += 1

        rem = self.budget - self.amountSpent
        k = i
        if rem > 0:
            for j in range(k, int(Gifts.__len__())):
                if Gifts[j].giftType == 'Luxury':
                    if rem >= Gifts[j].price:
                        self.amountSpent += Gifts[j].price
                        temp = [Gifts[j].giftType, Gifts[j].price, Gifts[j].value]
                        giftBasket.append(temp)
                        break


    def NewGifting(self, gMaintainanceCost , Gifts , giftBasket):

        """Allocates gifts with the new gifting strategy"""


        index = []
        index.append(self.getGift("Essential" , Gifts , giftBasket))
        index.append(self.getGift("Luxury" , Gifts , giftBasket))
        index.append(self.getGift("Utility" , Gifts , giftBasket))

        index.sort()
        j = index[2]

        while (j < int(Gifts.__len__()) and self.budget > self.amountSpent):
            self.amountSpent += Gifts[j].price
            temp = [Gifts[j].giftType, Gifts[j].price, Gifts[j].value]
            giftBasket.append(temp)
            j+=1

    def getGift(self , type , Gifts , giftBasket):

        """Allocates one gift of each type"""

        Gifts.sort(key=operator.attrgetter('price'))
        i = 0
        while (Gifts[i].giftType != type):
            i += 1

        self.amountSpent += Gifts[i].price
        temp = [Gifts[i].giftType, Gifts[i].price, Gifts[i].value]
        giftBasket.append(temp)

        return i