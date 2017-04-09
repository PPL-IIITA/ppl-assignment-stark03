import operator

class boyGenerous:
    happiness = 0
    amountSpent = 0
    gfName = ""

    def __init__(self, boy):
        self.name = boy['name']
        self.attractiveness = int(boy['attractiveness'])
        self.intelligence = int(boy['intelligence'])
        self.budget = int(boy['budget'])
        self.minimumAttrReq = int(boy['minimumAttrReq'])
        self.bType = boy['bType']
        # self.amountSpent = boy['amountSpent']
        self.status = boy['status']

    def happinessCalculator(self, gHappiness):
        self.happiness = gHappiness

    def gifting(self, gMaintainanceCost, Gifts, giftBasket):
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
