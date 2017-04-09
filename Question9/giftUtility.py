from Gifts import Gift

class giftUtility(Gift):

    """Gift Class for gifttype = 'Utility'"""

    def __init__(self, gift):
        "constructor"
        Gift.__init__(self,gift)
        self.utilityClass = None
        self.utilityValue = 0
