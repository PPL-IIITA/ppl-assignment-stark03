from reader import *
from couple import *
import operator
import logging

Couples = []
brokenUpGirls = []

class Break:

    def makeCouples(self):
        """Makes Couples"""
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
                    if (t.minimumAttrReq >= arrGirls[i].attractiveness and t.budget >= arrGirls[i].maintainanceCost and t.status == 'single'):
                        arrGirls[i].status = 'committed'
                        t.status = "Committed"
                        t.gifting(arrGirls[i].maintainanceCost, Gifts, giftBasket)
                        h = arrGirls[i].happinessCalculator(giftBasket,t.amountSpent)
                        if(t.bType == 'miser'):
                            t.happinessCalculator()
                        elif(t.bType == 'geeks'):
                            t.happinessCalculator(arrGirls[i].intelligence)
                        else:
                            t.happinessCalculator(h)
                        temp = couple(t,arrGirls[i])
                        temp.happinessCalcuator(t,arrGirls[i])
                        temp.compatibilityCalculator(t,arrGirls[i])
                        Couples.append(temp)
                        break
                    else:
                        continue

            elif criteria == "mostRich":
                arrBoys.sort(key=operator.attrgetter('budget'), reverse=True)
                for k in arrBoys:
                    if (k.minimumAttrReq >= arrGirls[i].attractiveness and k.budget > arrGirls[i].maintainanceCost and k.status == 'single'):
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

                        temp = couple(k,arrGirls[i])
                        temp.happinessCalcuator(k, arrGirls[i])
                        temp.compatibilityCalculator(k, arrGirls[i])
                        Couples.append(temp)
                        break
                    else:
                        continue
            else:
                arrBoys.sort(key=operator.attrgetter('intelligence'))
                for y in arrBoys:
                    if (y.minimumAttrReq >= arrGirls[i].attractiveness and y.budget > arrGirls[i].maintainanceCost and y.status == 'single'):
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

                        temp = couple(y,arrGirls[i])
                        temp.happinessCalcuator(y, arrGirls[i])
                        temp.compatibilityCalculator(y, arrGirls[i])
                        Couples.append(temp)
                        break
                    else:
                        continue


    def breakLeastHappy(self,k):

        """Gives the k least happy couples and perform their break up"""
        Couples.sort(key=operator.attrgetter('happiness'),reverse=False)
        if((k <= Couples.__len__())):
            for i in range (0,k):
                print("%s broke up with %s" % (Couples[i].gName , Couples[i].bName ))
                for j in range(0 , int(len(arrBoys))):
                    if(arrBoys[j].name == Couples[i].bName):
                        arrBoys[j].status = "single"
                        break
                for l in range(0,int(len(arrGirls))):
                    if(arrGirls[l].name == Couples[i].gName):
                        arrGirls[l].status = "single"
                        arrGirls[l].blackList = Couples[i].bName
                        brokenUpGirls.append(arrGirls[l])
                        break

            for i in range(0,k):
                del Couples[0]


        else :
            print("%d is greater than the no.of couples formed"%(k))


    def makeEveryoneCommitted(self):
        """
        Allocates boyfriends to newly broke up girls and form new couples
        """

        for f in range(0, int(len(brokenUpGirls))):

            flag = 0
            for i in range(0, int(len(arrGirls))):
                if(arrGirls[i].name == brokenUpGirls[f].name):
                    criteria = arrGirls[i].chosingCri

                    giftB = []

                    if (criteria == 'mostAttractive'):
                        arrBoys.sort(key=operator.attrgetter('attractiveness'), reverse=True)
                        for t in arrBoys:
                            if (t.minimumAttrReq >= arrGirls[i].attractiveness and t.budget >= arrGirls[
                                i].maintainanceCost and t.status == 'single' and arrGirls[i].blackList != t.name):
                                arrGirls[i].status = 'committed'
                                t.status = "committed"

                                h = arrGirls[i].happinessCalculator(giftB, t.amountSpent)
                                if (t.bType == 'miser'):
                                    t.happinessCalculator()
                                elif (t.bType == 'geeks'):
                                    t.happinessCalculator(arrGirls[i].intelligence)
                                else:
                                    t.happinessCalculator(h)
                                print("%s recently patched up with %s , her old boyfriend was %s" % (arrGirls[i].name , t.name , arrGirls[i].blackList))
                                temp = couple(t, arrGirls[i])
                                temp.happinessCalcuator(t, arrGirls[i])
                                temp.compatibilityCalculator(t, arrGirls[i])
                                Couples.append(temp)
                                flag = 1
                                break
                            else:
                                continue

                    elif criteria == "mostRich":
                        arrBoys.sort(key=operator.attrgetter('budget'), reverse=True)
                        for k in arrBoys:
                            if (k.minimumAttrReq >= arrGirls[i].attractiveness and k.budget > arrGirls[
                                i].maintainanceCost and k.status == 'single' and arrGirls[i].blackList != k.name):
                                arrGirls[i].status = 'committed'
                                k.status = 'committed'
                                h = arrGirls[i].happinessCalculator(giftB, k.amountSpent)
                                if (k.bType == 'miser'):
                                    k.happinessCalculator()
                                elif (k.bType == 'geeks'):
                                    k.happinessCalculator(arrGirls[i].intelligence)
                                else:
                                    k.happinessCalculator(h)
                                print("%s recently patched up with %s , her old boyfriend was %s" % (arrGirls[i].name , k.name , arrGirls[i].blackList))

                                temp = couple(k, arrGirls[i])
                                temp.happinessCalcuator(k, arrGirls[i])
                                temp.compatibilityCalculator(k, arrGirls[i])
                                Couples.append(temp)
                                flag = 1
                                break
                            else:
                                continue
                    else:
                        arrBoys.sort(key=operator.attrgetter('intelligence'))
                        for y in arrBoys:
                            if (y.minimumAttrReq >= arrGirls[i].attractiveness and arrGirls[
                                i].blackList != y.name and y.budget > arrGirls[
                                i].maintainanceCost and y.status == 'single'):

                                arrGirls[i].status = 'committed'
                                y.status = 'committed'

                                h = arrGirls[i].happinessCalculator(giftB, y.amountSpent)
                                if (y.bType == 'miser'):
                                    y.happinessCalculator()
                                elif (y.bType == 'geeks'):
                                    y.happinessCalculator(arrGirls[i].intelligence)
                                else:
                                    y.happinessCalculator(h)
                                print("%s recently patched up with %s , her old boyfriend was %s" % (arrGirls[i].name , y.name , arrGirls[i].blackList))

                                temp = couple(y, arrGirls[i])
                                temp.happinessCalcuator(y, arrGirls[i])
                                temp.compatibilityCalculator(y, arrGirls[i])
                                Couples.append(temp)
                                flag = 1
                                break
                            else:
                                continue


                if(flag == 1):
                    break

