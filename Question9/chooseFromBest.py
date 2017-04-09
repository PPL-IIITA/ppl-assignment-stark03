from reader import *
from couple import *
import operator
import logging

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG,filename='logGifting.txt',filemode='w')

Couples = []

class formCouples():

    def kBestItems(self, k, list, criteria):
        """the function creates a list of the best k items based on a particular criteria"""
        l = []
        list.sort(key=operator.attrgetter(criteria))
        for i in range(0, k):
            l.append(list[i])

        return l

    def makeCouples(self, k):

        r = read()
        r.readcsvfile('b')
        r.readcsvfile('g')
        r.readcsvfile('f')
        co = 0
        for i in range(0, int(arrGirls.__len__())):
            criteria = arrGirls[i].chosingCri
            if(criteria == "mostAttractive"):
                cri = "attractiveness"
            elif(criteria == "mostRich"):
                cri = "budget"
            else:
                cri = "intelligence"
            giftBasket = []
            newBoys = self.kBestItems(k, arrBoys, cri)
            count = 0
            for t in newBoys:
                if(t.status == 'single' and t.budget >= arrGirls[i].maintainanceCost):
                    arrGirls[i].status = 'committed'
                    t.status = "Committed"
                    t.gifting(arrGirls[i].maintainanceCost, Gifts, giftBasket , k)
                    h = arrGirls[i].happinessCalculator(giftBasket, t.amountSpent)
                    if (t.bType == 'miser'):
                        t.happinessCalculator()
                    elif (t.bType == 'geeks'):
                        t.happinessCalculator(arrGirls[i].intelligence)
                    else:
                        t.happinessCalculator(h)
                    logging.info(
                        "%s has given %s gifts of following type,price and value:-" % (t.name, arrGirls[i].name))
                    print("%s is now in relationship with %s" % (t.name, arrGirls[i].name))
                    for b in range(0, giftBasket.__len__()):
                        logging.info(" %d . Type :- %s , Price :- %d , Value :- %d" % (
                        (b + 1), giftBasket[b][0], giftBasket[b][1], giftBasket[b][2]))
                    temp = couple(t, arrGirls[i])
                    temp.happinessCalcuator(t, arrGirls[i])
                    temp.compatibilityCalculator(t, arrGirls[i])
                    Couples.append(temp)
                    break

                else:
                    continue
