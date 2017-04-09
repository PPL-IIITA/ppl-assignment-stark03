
from chooseFromBest import *

def main():

    """main function for question 9 , creates an object of class 'chooseFromBest' prints the formed couples , the changes are made in the log file 'logGifting.txt' durin the program"""
    c = formCouples()
    """here k is taken as 10 , any value can be taken."""

    c.makeCouples(10)

main()