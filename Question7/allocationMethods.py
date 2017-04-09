from reader import *
import operator
import logging
from couple import *

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG,filename='logCouples.txt',filemode='w')

Couples = []
C = {}

class allocAndFind():
    """allocates votfriends to all girlfriends and then uses different implementations such as list , sorted list and hashTable to find whethere the particular boy in the list is committed or not"""

    def makeCouples(self):
        """Makes Couples and prints the gifting details of each"""
        r = read()
        r.readcsvfile('b')
        r.readcsvfile('g')
        r.readcsvfile('f')

        logging.info("Event : Gifting Details\n")
        for i in range(0, int(len(arrGirls))):
            criteria = arrGirls[i].chosingCri
            giftBasket = []
            if (criteria == 'mostAttractive'):
                arrBoys.sort(key=operator.attrgetter('attractiveness'), reverse=True)
                for t in arrBoys:
                    if (t.minimumAttrReq >= arrGirls[i].attractiveness and t.budget >= arrGirls[
                        i].maintainanceCost and t.status == 'single'):
                        arrGirls[i].status = 'committed'
                        t.status = "Committed"
                        t.gifting(arrGirls[i].maintainanceCost, Gifts, giftBasket)
                        h = arrGirls[i].happinessCalculator(giftBasket, t.amountSpent)
                        if (t.bType == 'miser'):
                            t.happinessCalculator()
                        elif (t.bType == 'geeks'):
                            t.happinessCalculator(arrGirls[i].intelligence)
                        else:
                            t.happinessCalculator(h)
                        logging.info(
                            "%s has given %s gifts of following type,price and value:-" % (t.name, arrGirls[i].name))
                        for b in range(0, giftBasket.__len__()):
                            logging.info(" %d . Type :- %s , Price :- %d , Value :- %d" % (
                                (b + 1), giftBasket[b][0], giftBasket[b][1], giftBasket[b][2]))
                        temp = couple(t, arrGirls[i])
                        temp.happinessCalcuator(t, arrGirls[i])
                        temp.compatibilityCalculator(t, arrGirls[i])
                        Couples.append(temp)
                        C.update({t.name : arrGirls[i].name})
                        break
                    else:
                        continue

            elif criteria == "mostRich":
                arrBoys.sort(key=operator.attrgetter('budget'), reverse=True)
                for k in arrBoys:
                    if (k.minimumAttrReq >= arrGirls[i].attractiveness and k.budget > arrGirls[
                        i].maintainanceCost and k.status == 'single'):
                        arrGirls[i].status = 'committed'
                        k.status = 'committed'
                        k.gifting(arrGirls[i].maintainanceCost, Gifts, giftBasket)
                        h = arrGirls[i].happinessCalculator(giftBasket, k.amountSpent)
                        if (k.bType == 'miser'):
                            k.happinessCalculator()
                        elif (k.bType == 'geeks'):
                            k.happinessCalculator(arrGirls[i].intelligence)
                        else:
                            k.happinessCalculator(h)
                        logging.info(
                            "%s has given %s gifts of following type,price and value:-" % (k.name, arrGirls[i].name))

                        for b in range(0, giftBasket.__len__()):
                            logging.info(" %d . Type :- %s , Price :- %d , Value :- %d" % (
                                (b + 1), giftBasket[b][0], giftBasket[b][1], giftBasket[b][2]))
                        temp = couple(k, arrGirls[i])
                        temp.happinessCalcuator(k, arrGirls[i])
                        temp.compatibilityCalculator(k, arrGirls[i])
                        Couples.append(temp)
                        C.update({k.name : arrGirls[i].name})
                        break
                    else:
                        continue
            else:
                arrBoys.sort(key=operator.attrgetter('intelligence'))
                for y in arrBoys:
                    if (y.minimumAttrReq >= arrGirls[i].attractiveness and y.budget > arrGirls[
                        i].maintainanceCost and y.status == 'single'):
                        arrGirls[i].status = 'committed'
                        y.status = 'committed'
                        y.gifting(arrGirls[i].maintainanceCost, Gifts, giftBasket)
                        h = arrGirls[i].happinessCalculator(giftBasket, y.amountSpent)
                        if (y.bType == 'miser'):
                            y.happinessCalculator()
                        elif (y.bType == 'geeks'):
                            y.happinessCalculator(arrGirls[i].intelligence)
                        else:
                            y.happinessCalculator(h)
                        logging.info(
                            "%s has given %s gifts of following type,price and value:-" % (y.name, arrGirls[i].name))
                        for b in range(0, giftBasket.__len__()):
                            logging.info(" %d . Type :- %s , Price :- %d , Value :- %d" % (
                                (b + 1), giftBasket[b][0], giftBasket[b][1], giftBasket[b][2]))
                        temp = couple(y, arrGirls[i])
                        temp.happinessCalcuator(y, arrGirls[i])
                        temp.compatibilityCalculator(y, arrGirls[i])
                        Couples.append(temp)
                        C.update({y.name: arrGirls[i].name})
                        break
                    else:
                        continue

    def FindGf_List(self):

        """Checks whether a boy in the given list of boys has a girlfriend or not by using list"""

        for i  in arrBoys:
            flag = 0
            for c in Couples:
                if(c.bName == i.name):
                    print("Girlfriend found !! %s is committed to %s" % (c.bName , c.gName))
                    flag = 1
                    break
            if(flag == 0):
                print(" No Girlfriend found for %s" % i.name)

    def FindGf_SortedList(self):

        """Checks whether a boy in the given list of boys has a girlfriend or not by using sorted list"""

        Couples.sort(key=operator.attrgetter("bName"))
        for i in arrBoys:
            g = self.bSearch(Couples, i.name)
            if(g == None):
                print(" No Girlfriend found for %s" % i.name)
            else:
                print("Girlfriend found !! %s is committed to %s" % (i.name, g))

    def FindGf_Hash(self):

        """Checks whether a boy in the given list of boys has a girlfriend or not by using HashTable"""
        for i in arrBoys:
            if(i.status == 'single'):
                C.update({i.name: 'none'})


        for i in arrBoys:
            if(C[i.name] == "none"):
                print(" No Girlfriend found for %s" % i.name)
            else:
                print("Girlfriend found !! %s is committed to %s" % (i.name, C[i.name]))

    def bSearch(self , list , b):

        """Binary search to search whether  boy is present in the sorted Couples list or not"""

        if((list.__len__()) == 0):
            return None

        else:
            mid = int(len(list)/2)

            if(list[mid].bName == b):
                return list[mid].gName
            else:
                if(list[mid].bName > b ):
                    return self.bSearch(list[:mid] ,b)
                else:
                    return self.bSearch(list[mid+1:] , b)
