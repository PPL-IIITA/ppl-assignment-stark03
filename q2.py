
from coupleMaker import *

def main():

    cm = coupleMaker()
    cm.makeCouples()

    k = input("Enter k :- ")
    print("%d most happy couples:-" % int(k))
    cm.getMostHappy(int(k))
    print("\n")
    print("%d most compatible couples:-" % int(k))
    cm.getMostCompatible(int(k))


main()
