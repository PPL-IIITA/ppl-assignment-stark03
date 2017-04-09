from reader import *
from couple import *
import operator
import logging

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG,filename='logGifting.txt',filemode='w')

Couples = []
brokenUpGirls = []

class coupleMaker:

    def makeCouples(self):
        """Makes Couples and prints the gifting details of each , 
        here the gifting is done by the new strategy of giving a gift of each type irrespective of the Budget.
        The log file 'logGifting.txt is updated during the program
        """
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
                        t.NewGifting(arrGirls[i].maintainanceCost, Gifts, giftBasket)
                        h = arrGirls[i].happinessCalculator(giftBasket,t.amountSpent)
                        if(t.bType == 'miser'):
                            t.happinessCalculator()
                        elif(t.bType == 'geeks'):
                            t.happinessCalculator(arrGirls[i].intelligence)
                        else:
                            t.happinessCalculator(h)
                        logging.info("%s has given %s gifts of following type,price and value:-" % (t.name, arrGirls[i].name))
                        print("%s has given %s gifts of following type,price and value:-" % (t.name, arrGirls[i].name))
                        for b in range(0,giftBasket.__len__()):
                            print(" %d . Type :- %s , Price :- %d , Value :- %d" % ((b+1),giftBasket[b][0], giftBasket[b][1], giftBasket[b][2]))
                            logging.info(" %d . Type :- %s , Price :- %d , Value :- %d" % ((b+1),giftBasket[b][0], giftBasket[b][1], giftBasket[b][2]))
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
                        k.NewGifting(arrGirls[i].maintainanceCost, Gifts, giftBasket)
                        h = arrGirls[i].happinessCalculator(giftBasket, k.amountSpent)
                        if (k.bType == 'miser'):
                            k.happinessCalculator()
                        elif (k.bType == 'geeks'):
                            k.happinessCalculator(arrGirls[i].intelligence)
                        else:
                            k.happinessCalculator(h)
                        logging.info("%s has given %s gifts of following type,price and value:-" % (k.name, arrGirls[i].name))
                        print("%s has given %s gifts of following type,price and value:-" % (k.name, arrGirls[i].name))
                        for b in range(0,giftBasket.__len__()):
                            print(" %d . Type :- %s , Price :- %d , Value :- %d" % ((b+1),giftBasket[b][0], giftBasket[b][1], giftBasket[b][2]))
                            logging.info(" %d . Type :- %s , Price :- %d , Value :- %d" % ((b+1),giftBasket[b][0], giftBasket[b][1], giftBasket[b][2]))
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
                        y.NewGifting(arrGirls[i].maintainanceCost, Gifts, giftBasket)
                        h = arrGirls[i].happinessCalculator(giftBasket, y.amountSpent)
                        if (y.bType == 'miser'):
                            y.happinessCalculator()
                        elif (y.bType == 'geeks'):
                            y.happinessCalculator(arrGirls[i].intelligence)
                        else:
                            y.happinessCalculator(h)
                        logging.info("%s has given %s gifts of following type,price and value:-" % (y.name , arrGirls[i].name))
                        print("%s has given %s gifts of following type,price and value:-" % (y.name , arrGirls[i].name))
                        for b in range(0,giftBasket.__len__()):
                            print(" %d . Type :- %s , Price :- %d , Value :- %d" % ((b+1),giftBasket[b][0], giftBasket[b][1], giftBasket[b][2]))

                            logging.info(" %d . Type :- %s , Price :- %d , Value :- %d" % ((b+1),giftBasket[b][0], giftBasket[b][1], giftBasket[b][2]))
                        temp = couple(y,arrGirls[i])
                        temp.happinessCalcuator(y, arrGirls[i])
                        temp.compatibilityCalculator(y, arrGirls[i])
                        Couples.append(temp)
                        break
                    else:
                        continue


