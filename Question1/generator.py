import csv
import random
import string
"""Generates random entries for boy.csv,girls.csv , gifts.csv"""
class randomGenerator:

    def __init__(self, totalBoys, totalGirls, totalGifts):
        self.boys_no = totalBoys
        self.girls_no = totalGirls
        self.totalGifts = totalGifts

    def generateBoys(self):
        with open('boys.csv', 'w') as csvfile:
            fieldnames = ['name', 'attractiveness', 'minimumAttrReq', 'intelligence', 'budget', 'status', 'bType']
            boyWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            boyWriter.writeheader()
            bTypeChoices = ['miser', 'generous', 'geeks']
            for i in range(self.boys_no):
                temp_obj = {
                    'name': random.choice(string.ascii_uppercase) + ''.join(random.choice(string.ascii_lowercase) for _ in range(6)),
                    'attractiveness': random.randint(1,100),
                    'minimumAttrReq': random.randint(1,50),
                    'intelligence': random.randint(1,100),
                    'budget': random.randint(1,100),
                    'bType': random.choice(bTypeChoices),
                    'status': 'single'
                }
                boyWriter.writerow(temp_obj)

    def generateGirls(self):
        with open('girls.csv', 'w') as csvfile:
            fieldnames = ['name', 'attractiveness', 'intelligence', 'maintainanceCost', 'status', 'gType', 'chosingCri']
            girlWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            girlWriter.writeheader()
            chosingCriChoices = ['mostAttractive', 'mostGenius', 'mostRich']
            gTypeChoices = ['choosy', 'normal', 'desperate']
            for i in range(self.girls_no):
                temp_obj = {
                    'name': random.choice(string.ascii_uppercase) + ''.join(random.choice(string.ascii_lowercase) for _ in range(6)),
                    'attractiveness': random.randint(1,100),
                    'intelligence': random.randint(1,100),
                    'maintainanceCost': random.randint(1,50),
                    'gType': random.choice(gTypeChoices),
                    'chosingCri':random.choice(chosingCriChoices),
                    'status': 'single'
                }
                girlWriter.writerow(temp_obj)


    def generateGifts(self):
        with open('gifts.csv', 'r+') as csvfile:
            fields = ['giftType', 'price', 'value']
            giftWriter = csv.DictWriter(csvfile, fieldnames=fields)
            giftWriter.writeheader()
            giftTypeChoices = ['Essential', 'Utility', 'Luxury']
            for i in range(self.totalGifts):
                obj = {
                    'giftType': random.choice(giftTypeChoices),
                    'price': random.randint(1, 50),
                    'value': random.randint(1, 50)
                }
                giftWriter.writerow(obj)
