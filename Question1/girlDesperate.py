from math import exp
from Girls import Girl

class girlDesperate(Girl):

    """Girl class for girlType = 'Choosy'"""

    def __init__(self, girl):
        "constructor"
        Girl.__init__(self,girl)
        self.happiness = 0
        self.costOfGiftsRec = 0
        self.bfName = ""
        self.blackList = ""

    def happinessCalculator(self , giftBasket , amount):

        "Calculates happiness for girls of type Normal"

        self.costOfGiftsRec = amount
        self.happiness = exp(amount/self.maintainanceCost)
        return self.happiness