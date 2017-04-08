
class couple:

    """Couple class with attributes:-
        bName = Name of the boy
        gName = Name of the girl
        happiness  = happiness of the couple
        compatibility = compatibility of the couple
    """
    def __init__(self, boy, girl):
        "constructor"
        self.bName = boy.name
        self.gName = girl.name

    def happinessCalcuator(self, boy, girl):
        "calculates happiness of the couple"
        self.happiness = boy.happiness + girl.happiness
        return self.happiness

    def compatibilityCalculator(self, boy, girl):
        "calculates compatibility of the couple"
        self.compatibility = (boy.budget - girl.maintainanceCost) + abs(boy.intelligence - girl.intelligence) + abs(boy.attractiveness - girl.attractiveness)
        return self.compatibility
