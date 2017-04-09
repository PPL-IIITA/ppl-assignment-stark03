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

