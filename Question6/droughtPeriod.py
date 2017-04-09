
"""Module containing the class which has fuctions which are responsible for everyday breakup of couples"""

from reader import *
from couple import *
import operator
import logging

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG,filename='CouplesNew.txt', filemode='w')

Couples = []
brokenUpGirls = []


class CoupleBreaker():

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
                        h = arrGirls[i].happinessCalculator(giftBasket, t.amountSpent)
                        if (t.bType == 'miser'):
                            t.happinessCalculator()
                        elif (t.bType == 'geeks'):
                            t.happinessCalculator(arrGirls[i].intelligence)
                        else:
                            t.happinessCalculator(h)
                        temp = couple(t, arrGirls[i])
                        temp.happinessCalcuator(t, arrGirls[i])
                        temp.compatibilityCalculator(t, arrGirls[i])
                        Couples.append(temp)
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

                        temp = couple(k, arrGirls[i])
                        temp.happinessCalcuator(k, arrGirls[i])
                        temp.compatibilityCalculator(k, arrGirls[i])
                        Couples.append(temp)
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

                        temp = couple(y, arrGirls[i])
                        temp.happinessCalcuator(y, arrGirls[i])
                        temp.compatibilityCalculator(y, arrGirls[i])
                        Couples.append(temp)
                        break
                    else:
                        continue

    def breakLeastHappy(self, k):

        """Performs break up of Couples with happiness less than k"""
        Couples.sort(key=operator.attrgetter('happiness'), reverse=False)
        logging.info("Break Up Details :-\n")
        i = 0
        j = 0
        while( k > Couples[i].happiness and i < Couples.__len__()):
            i += 1

        for j in range(0, i):
            print("%s broke up with %s" % (Couples[j].gName , Couples[j].bName ))
            logging.info("%s broke up with %s" % (Couples[j].gName , Couples[j].bName ))

            for m in range(0, int(len(arrBoys))):
                if (arrBoys[m].name == Couples[j].bName):
                    arrBoys[m].status = "single"
                    break
            for l in range(0, int(len(arrGirls))):
                if (arrGirls[l].name == Couples[j].gName):
                    arrGirls[l].status = "single"
                    arrGirls[l].blackList = Couples[j].bName
                    brokenUpGirls.append(arrGirls[l])
                    break

        for i in range(0, i):
            del Couples[0]

    def PatchThemUp(self):


        """
         Allocates boyfriends to newly broke up girls and form new couples
        """

        logging.info("Patch-Up Details :-\n")

        for f in range(0, int(len(brokenUpGirls))):

            flag = 0
            for i in range(0, int(len(arrGirls))):

                if (flag == 1):
                    break

                if (arrGirls[i].name == brokenUpGirls[f].name):
                    criteria = arrGirls[i].chosingCri

                    giftB = []

                    if (criteria == 'mostAttractive'):
                        arrBoys.sort(key=operator.attrgetter('attractiveness'), reverse=True)
                        count = 0
                        for t in arrBoys:
                            count +=1
                            if (t.minimumAttrReq >= arrGirls[i].attractiveness and t.budget >= arrGirls[
                                i].maintainanceCost and t.status == 'single' and arrGirls[i].blackList != t.name):
                                arrGirls[i].status = 'committed'
                                t.status = "committed"
                                t.gifting(arrGirls[i].maintainanceCost, Gifts, giftB)
                                h = arrGirls[i].happinessCalculator(giftB, t.amountSpent)
                                if (t.bType == 'miser'):
                                    t.happinessCalculator()
                                elif (t.bType == 'geeks'):
                                    t.happinessCalculator(arrGirls[i].intelligence)
                                else:
                                    t.happinessCalculator(h)
                                print("%s recently patched up with %s , her old boyfriend was %s" % (
                                    arrGirls[i].name, t.name, arrGirls[i].blackList))
                                logging.info("%s recently patched up with %s , her old boyfriend was %s , their gifting details are as follows :- \n" % (
                                    arrGirls[i].name, t.name, arrGirls[i].blackList))
                                for b in range(0, giftB.__len__()):
                                    logging.info(" %d . Type :- %s , Price :- %d , Value :- %d" % (
                                    (b + 1), giftB[b][0], giftB[b][1], giftB[b][2]))
                                temp = couple(t, arrGirls[i])
                                temp.happinessCalcuator(t, arrGirls[i])
                                temp.compatibilityCalculator(t, arrGirls[i])
                                Couples.append(temp)
                                flag = 1
                                break
                            else:
                                if(count  == arrBoys.__len__()):
                                    break
                                else :
                                    continue

                    elif criteria == "mostRich":
                        arrBoys.sort(key=operator.attrgetter('budget'), reverse=True)
                        count  = 0
                        for k in arrBoys:
                            count +=1
                            if (k.minimumAttrReq >= arrGirls[i].attractiveness and k.budget > arrGirls[
                                i].maintainanceCost and k.status == 'single' and arrGirls[i].blackList != k.name):
                                arrGirls[i].status = 'committed'
                                k.status = 'committed'
                                k.gifting(arrGirls[i].maintainanceCost, Gifts, giftB)
                                h = arrGirls[i].happinessCalculator(giftB, k.amountSpent)
                                if (k.bType == 'miser'):
                                    k.happinessCalculator()
                                elif (k.bType == 'geeks'):
                                    k.happinessCalculator(arrGirls[i].intelligence)
                                else:
                                    k.happinessCalculator(h)
                                print("%s recently patched up with %s , her old boyfriend was %s" % (
                                    arrGirls[i].name, k.name, arrGirls[i].blackList))
                                logging.info("%s recently patched up with %s , her old boyfriend was %s , thier gifting details are as follows :- \n" % (
                                    arrGirls[i].name, k.name, arrGirls[i].blackList))
                                for b in range(0, giftB.__len__()):
                                    logging.info(" %d . Type :- %s , Price :- %d , Value :- %d" % (
                                    (b + 1), giftB[b][0], giftB[b][1], giftB[b][2]))
                                temp = couple(k, arrGirls[i])
                                temp.happinessCalcuator(k, arrGirls[i])
                                temp.compatibilityCalculator(k, arrGirls[i])
                                Couples.append(temp)
                                flag = 1
                                break
                            else:
                                if(count == arrBoys.__len__()):
                                    break
                                else:
                                    continue
                    else:
                        arrBoys.sort(key=operator.attrgetter('intelligence'))
                        count = 0
                        for y in arrBoys:
                            count += 1
                            if (y.minimumAttrReq >= arrGirls[i].attractiveness and arrGirls[
                                i].blackList != y.name and y.budget > arrGirls[
                                i].maintainanceCost and y.status == 'single'):

                                arrGirls[i].status = 'committed'
                                y.status = 'committed'
                                y.gifting(arrGirls[i].maintainanceCost, Gifts, giftB)
                                h = arrGirls[i].happinessCalculator(giftB, y.amountSpent)
                                if (y.bType == 'miser'):
                                    y.happinessCalculator()
                                elif (y.bType == 'geeks'):
                                    y.happinessCalculator(arrGirls[i].intelligence)
                                else:
                                    y.happinessCalculator(h)
                                print("%s recently patched up with %s , her old boyfriend was %s" % (
                                    arrGirls[i].name, y.name, arrGirls[i].blackList))
                                logging.info("%s recently patched up with %s , her old boyfriend was %s , their gifting details are as follows :- \n" % (
                                    arrGirls[i].name, y.name, arrGirls[i].blackList))
                                for b in range(0, giftB.__len__()):
                                    logging.info(" %d . Type :- %s , Price :- %d , Value :- %d" % (
                                    (b + 1), giftB[b][0], giftB[b][1], giftB[b][2]))
                                temp = couple(y, arrGirls[i])
                                temp.happinessCalcuator(y, arrGirls[i])
                                temp.compatibilityCalculator(y, arrGirls[i])
                                Couples.append(temp)
                                flag = 1
                                break
                            else:
                                if(count == arrBoys.__len__()):
                                    break
                                else:
                                    continue

                else:
                    continue
