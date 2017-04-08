
class Boy:

    """The parent class for all types of boys"""

    def __init__(self, boy ):
        """constructor which initializes attributes such as :-
        name = name of the boy
        attractiveness = attractiveness of the boy
        intelligence = intelligence of the boy
        budget = budget of the boy
        minimumAttrReq = minimum attractiveness required in the girl
        bType = type of the boy
        status = relationship status
        """
        self.name = boy['name']
        self.attractiveness = int(boy['attractiveness'])
        self.intelligence = int(boy['intelligence'])
        self.budget = int(boy['budget'])
        self.minimumAttrReq = int(boy['minimumAttrReq'])
        self.bType = boy['bType']
        self.status = boy['status']

    def gifting(self):
        pass

    def happinessCalculator(self):
        pass

