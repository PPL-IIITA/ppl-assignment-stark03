
class Girl:

    """"Parent class for all types of girls """

    def __init__(self , girl):
        """constructor which initializes attributes such as :-
        name = name of the girl
        attractiveness = attractiveness of the girl
        intelligence = intelligence of the girl
        maintainanceCost = maintainance cost of the girl
        chosingCri =  chosing criterion for the boys
        gType = type of the girl
        status = relationship status
        """
        self.name = girl['name']
        self.attractiveness = int(girl['attractiveness'])
        self.maintainanceCost = int(girl['maintainanceCost'])
        self.intelligence = int(girl['intelligence'])
        self.gType = girl['gType']
        self.chosingCri = girl['chosingCri']
        self.status = "single"

    def happinessCalculator(self):
        pass