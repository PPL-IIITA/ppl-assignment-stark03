from reader import *
from couple import *
import operator
import logging

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG,filename='logCouples.txt',filemode='w')
class allocate:

    def alloc(self):
        """Allocates boys to girls"""

        r = read()
        r.readcsvfile('b')
        r.readcsvfile('g')
        r.readcsvfile('f')

        for i in range(0, int(len(arrGirls))):
            criteria = arrGirls[i].chosingCri
            if(criteria == 'mostAttractive'):
                arrBoys.sort(key=operator.attrgetter('attractiveness'), reverse=True)
                for t in arrBoys:
                    if(t.minimumAttrReq >=arrGirls[i].attractiveness and t.budget >= arrGirls[i].maintainanceCost and t.status == 'single'):
                        arrGirls[i].status = 'committed'
                        #print(arrGirls[i].name, "is committed to", t.name)
                        t.status = "Committed"
                        t.gfName = arrGirls[i].name
                        arrGirls[i].bfName = t.name
                        break
                    else:
                        continue

            elif(criteria == "mostRich"):
                arrBoys.sort(key=operator.attrgetter('budget'), reverse=True)
                for k in arrBoys:
                    if (k.minimumAttrReq >= arrGirls[i].attractiveness and k.budget > arrGirls[i].maintainanceCost and k.status == 'single'):
                        arrGirls[i].status = 'committed'
                        #print(arrGirls[i].name, "is committed to", k.name)
                        k.status = 'committed'
                        k.gfName = arrGirls[i].name
                        arrGirls[i].bfName = k.name
                        break
                    else:
                        continue
            else:
                arrBoys.sort(key=operator.attrgetter('intelligence'))
                for y in arrBoys:
                    if(y.minimumAttrReq >=arrGirls[i].attractiveness and y.budget > arrGirls[i].maintainanceCost and y.status == 'single'):
                        arrGirls[i].status = 'committed'
                        #print(arrGirls[i].name, "is committed to", y.name)
                        y.status = 'committed'
                        y.gfName = arrGirls[i].name
                        arrGirls[i].bfName = y.name
                        break
                    else:
                        continue



    def printCouples(self):
        """Prints Couples formed"""
        for boy in arrBoys:
            if(boy.status == "committed"):
                print(boy.name ,"is committed to", boy.gfName)

    def performLog(self):
        """Writes the couple formation event into log file"""
        logging.info("Event : Couples Formation\n")
        for boy in arrBoys:
            if(boy.status == "committed"):
                logging.info("%s is committed to %s" % (boy.name, boy.gfName))

