
class giftLuxury:

    luxuryRating = 0
    obtainDiff = 0

    def __init__(self, gift):
        self.giftType = gift['giftType']
        self.price = int(gift['price'])
        self.value = int(gift['value'])
