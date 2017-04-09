
from droughtPeriod import *

def main():

    """main function for question6 , performs breakups of couples with happiness less than k and patchups of newly broke couples for t days in a year"""
    d = CoupleBreaker()
    d.makeCouples()

    """here k is taken as 2 , any value can be taken"""
    t= int(input("Enter the no. of days :-"))

    for i in range(0, t):
        d.breakLeastHappy(2)
        d.PatchThemUp()

main()