from math import log
from Girls import Girl

class girlChoosy(Girl):

    """Girl class for girlType = 'Choosy'"""

    def __init__(self, girl):
        "constructor"
        Girl.__init__(self,girl)
        self.happiness = 0
        self.costOfGiftsRec = 0
        self.bfName = ""
        self.blackList = ""


    def happinessCalculator(self, giftBasket, amount):
        "Calculates the happiness for girls of type Choosy"
        self.costOfGiftsRec = amount
        for i in range(0,len(giftBasket)):
            if(giftBasket[i][0] == "Luxury"):
                amount += giftBasket[i][1]

        if((amount/self.maintainanceCost) > 0):
            self.happiness = log(amount/self.maintainanceCost)
        else:
            self.happiness = 0

        return self.happiness

