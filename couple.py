
class couple:

    def __init__(self, boy, girl):
        self.bName = boy.name
        self.gName = girl.name

    def happinessCalcuator(self, boy, girl):
        self.happiness = boy.happiness + girl.happiness
        return self.happiness

    def compatibilityCalculator(self, boy, girl):
        self.compatibility = (boy.budget - girl.maintainanceCost) + abs(boy.intelligence - girl.intelligence) + abs(boy.attractiveness - girl.attractiveness)
        return self.compatibility
