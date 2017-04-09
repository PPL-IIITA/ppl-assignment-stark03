import operator
from Boys import Boy

class boyGenerous(Boy):

    """Boy class for boyType = 'Generous'"""

    def __init__(self, boy):
        """constructor , calls the parent constructor and initializes other attributes as:-
            happiness = happiness of the boy
            amountSpent = amount spent on gifting
            gfName = name of the girlfriend
        """
        Boy.__init__(self,boy)
        self.happiness = 0
        self.amountSpent = 0
        self.gfName = ""


    def happinessCalculator(self, gHappiness):
        "Calculates happiness for Generous boys"
        self.happiness = gHappiness

    def gifting(self, gMaintainanceCost, Gifts, giftBasket):

        "Sets up the gift basket for Generous boys"

        Gifts.sort(key=operator.attrgetter('price'), reverse=True)

        if self.budget < Gifts[0].price:
            temp = [Gifts[0].giftType, Gifts[0].price, Gifts[0].value]
            self.budget = Gifts[0].price
            self.amountSpent = self.budget
            giftBasket.append(temp)

        else:
            tempBudget = self.budget
            i = 0
            while(True):
                if(self.amountSpent < self.budget):
                    if((self.amountSpent + Gifts[i].price) > self.budget):
                        break
                    else:
                        temp = [Gifts[i].giftType, Gifts[i].price, Gifts[i].value]
                        giftBasket.append(temp)
                        self.amountSpent += Gifts[i].price
                        i+=1

    def NewGifting(self, gMaintainanceCost, Gifts, giftBasket):

        """Allocates gifts with the new gifting strategy"""

        index = []
        index.append(self.getGift("Essential", Gifts, giftBasket))
        index.append(self.getGift("Luxury", Gifts, giftBasket))
        index.append(self.getGift("Utility", Gifts, giftBasket))

        index.sort()
        j = index[2]

        while (j < int(Gifts.__len__()) and self.budget > self.amountSpent):
            if ((self.amountSpent + Gifts[j].price) > self.budget):
                break
            else:
                temp = [Gifts[j].giftType, Gifts[j].price, Gifts[j].value]
                giftBasket.append(temp)
                self.amountSpent += Gifts[j].price
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