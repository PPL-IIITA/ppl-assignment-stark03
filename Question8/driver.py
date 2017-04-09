
from generator import *

def generateRandomInput():
    """Can be used to generate random Inputs"""
    ra = randomGenerator(100, 100, 100)
    ra.generateBoys()
    ra.generateGirls()
    ra.generateGifts()

generateRandomInput()

