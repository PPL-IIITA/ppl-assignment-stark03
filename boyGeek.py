import operator

class boyGeek:

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

    def happinessCalculator(self , gIntelligence):
        self.happiness = gIntelligence

    def gifting(self, gMaintainanceCost , Gifts , giftBasket):
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

