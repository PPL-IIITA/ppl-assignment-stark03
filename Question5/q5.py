
from oneByone import *

def main():

    obo = CoupleMaker()
    print("The Couples formed by the one by one mechanism are :-")
    print()
    obo.formCouples()
    print()
    k = input("Enter k :-")
    print("The" , k , "most happy couples are :- \n")
    obo.getMostHappy(int(k))

main()
