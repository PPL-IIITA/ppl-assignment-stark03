
class Gift:

    """Parent class for all types of Gifts"""

    def __init__(self, gift):
        """constructor with attributes :-
            giftType = type of the gift
            price = price of the gift
            value = value of the gift
        """
        self.giftType = gift['giftType']
        self.price = int(gift['price'])
        self.value = int(gift['value'])
