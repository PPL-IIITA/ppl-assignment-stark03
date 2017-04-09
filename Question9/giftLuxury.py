from Gifts import Gift

class giftLuxury(Gift):

    """Gift Class for gifttype = 'Luxury'"""

    def __init__(self, gift):
        "constructor"
        Gift.__init__(self,gift)
        self.luxuryRating = 0
        self.obtainDifficulty = 0

