from reader import *
from couple import *
import operator
import logging

Couples = []

class CoupleMaker():

    def formCouples(self):

        """Makes couples by mechanism that first a girl chooses a boy and later a boy chooses a girl"""

        r = read()
        r.readcsvfile('b')
        r.readcsvfile('g')
        r.readcsvfile('f')

        i = 0
        j = 0
        ch = 0

        while (i < arrGirls.__len__() and j < arrBoys.__len__()):

            if(ch == 0):
                arrGirls.sort(key=operator.attrgetter('maintainanceCost'))
                while(arrGirls[i].status != "single" and i < arrGirls.__len__()):
                    i+=1

                if(i == arrGirls.__len__()):
                    break
                criteria = arrGirls[i].chosingCri
                giftBasket = []
                flag = 0
                if (criteria == 'mostAttractive'):
                    arrBoys.sort(key=operator.attrgetter('attractiveness'), reverse=True)
                    count = 0
                    for t in arrBoys:
                        count +=1
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

                            print("%s is now in relationship with %s" % (arrGirls[i].name , t.name))

                            temp = couple(t, arrGirls[i])
                            temp.happinessCalcuator(t, arrGirls[i])
                            temp.compatibilityCalculator(t, arrGirls[i])
                            Couples.append(temp)
                            break
                        else:
                            if(count == arrBoys.__len__()):
                                flag = 1
                                break
                            else:
                                continue

                elif criteria == "mostRich":
                    arrBoys.sort(key=operator.attrgetter('budget'), reverse=True)
                    count = 0
                    for k in arrBoys:
                        count +=1
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

                            print("%s is now in relationship with %s" % (arrGirls[i].name , k.name))

                            temp = couple(k, arrGirls[i])
                            temp.happinessCalcuator(k, arrGirls[i])
                            temp.compatibilityCalculator(k, arrGirls[i])
                            Couples.append(temp)
                            break
                        else:
                            if(count == arrBoys.__len__()):
                                flag = 1
                                break
                            else:
                                continue


                else:
                    arrBoys.sort(key=operator.attrgetter('intelligence'))
                    count = 0
                    for y in arrBoys:
                        count += 1
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
                            logging.info("%s has given %s gifts of following type,price and value:-" % (
                            y.name, arrGirls[i].name))
                            print("%s is now in relationship with %s" % (arrGirls[i].name , y.name))

                            temp = couple(y, arrGirls[i])
                            temp.happinessCalcuator(y, arrGirls[i])
                            temp.compatibilityCalculator(y, arrGirls[i])
                            Couples.append(temp)
                            break
                        else:
                            if(count == arrBoys.__len__()):
                                flag = 1
                                break
                            continue
                if(flag == 1):
                    i+=1
                    ch = 1
                else:
                    ch = 0

            else:
                arrBoys.sort(key=operator.attrgetter("attractiveness"))
                while(arrBoys[j].status != "single" and j<arrBoys.__len__()):
                    j+=1

                if(j==arrBoys.__len__()):
                    break
                giftBasket = []
                flag = 0
                arrGirls.sort(key=operator.attrgetter("attractiveness"))
                count = 0
                for g in arrGirls:
                    count +=1
                    if(arrBoys[j].minimumAttrReq >= g.attractiveness and arrBoys[j].budget > g.maintainanceCost and g.status == 'single'):
                        arrBoys[j].status = 'committed'
                        g.status = 'committed'
                        arrBoys[j].gifting(g.maintainanceCost, Gifts, giftBasket)
                        h = g.happinessCalculator(giftBasket, arrBoys[j].amountSpent)

                        if (arrBoys[j].bType == 'miser'):
                            arrBoys[j].happinessCalculator()
                        elif (arrBoys[j].bType == 'geeks'):
                            arrBoys[j].happinessCalculator(arrGirls[i].intelligence)
                        else:
                            arrBoys[j].happinessCalculator(h)

                        print("%s is now in relationship with %s" % (g.name, arrBoys[j].name))
                        temp = couple(arrBoys[j],g)
                        temp.happinessCalcuator(arrBoys[j], g)
                        temp.compatibilityCalculator(arrBoys[j], g)
                        Couples.append(temp)
                        break
                    else:
                        if(count == arrGirls.__len__()):
                            flag = 1
                            break
                        else:
                            continue
                if(flag == 0):
                    ch = 0
                else:
                    j+=1
                    ch = 1

    def getMostHappy(self, k):
        """ Prints the k most happy Couples"""
        Couples.sort(key=operator.attrgetter('happiness'),reverse=True)
        if(k <= Couples.__len__()):
            for i in range(0, k):
                print("Boy :- %s , Girl :- %s , Happiness :- %f" % (Couples[i].bName,Couples[i].gName, Couples[i].happiness))
        else:
            print("K is greater than the no. of couples formed")


