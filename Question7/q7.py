from allocationMethods import *

def main():

    print("Choose the method of allocation :-\n1.List\n2.List(sorted)\n3.Hash Table")
    t = int(input())
    a = allocAndFind()
    a.makeCouples()

    if (t == 2):
        a.FindGf_SortedList()

    elif (t == 3):
        a.FindGf_Hash()

    else:
        a.FindGf_List()


main()