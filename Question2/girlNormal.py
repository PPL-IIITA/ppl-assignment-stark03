class girlNormal:
    happiness = 0
    costOfGiftsRec = 0
    bfName = ""

    def __init__(self, girl):
        self.name = girl['name']
        self.attractiveness = int(girl['attractiveness'])
        self.maintainanceCost = int(girl['maintainanceCost'])
        self.intelligence = int(girl['intelligence'])
        self.gType = girl['gType']
        self.chosingCri = girl['chosingCri']
        self.status = bool(girl['status'])

    def happinessCalculator(self , giftBasket , amount):
        self.costOfGiftsRec = amount

        for i in range(0,len(giftBasket)):
            amount += giftBasket[i][2]

        self.happiness = amount/self.maintainanceCost
        return self.happiness
