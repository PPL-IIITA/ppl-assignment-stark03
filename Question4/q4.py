
from coupleBreaker import *

def main():


    cm = Break()
    cm.makeCouples()

    k = input("Enter k :- ")
    cm.breakLeastHappy(int(k))
    print()
    cm.makeEveryoneCommitted()


main()