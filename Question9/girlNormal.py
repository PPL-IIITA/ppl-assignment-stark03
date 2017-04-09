from Girls import Girl

class girlNormal(Girl):

    "Girl class for girlType = 'Choosy'"

    def __init__(self, girl):
        "constructor"
        Girl.__init__(self,girl)
        self.bfName = ""
        self.costOfGiftsRec = 0
        self.happiness = 0
        self.blackList = ""

    def happinessCalculator(self , giftBasket , amount):

        "Calculates happiness for girls of type Normal"

        self.costOfGiftsRec = amount

        for i in range(0,len(giftBasket)):
            amount += giftBasket[i][2]

        self.happiness = amount/self.maintainanceCost
        return self.happiness
