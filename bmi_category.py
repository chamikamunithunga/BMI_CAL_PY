__author__ = 'suvasish'

class BmiCategroy:
    def __init__(self):
        pass

    def bmi_category(self, bmi):
        if bmi < 15.0:
            print('Very severely underweight')
        elif bmi < 16.0:
            print('Severely underweight')
        elif bmi < 18.5:
            print('Underweight')
        elif bmi < 25:
            print('Great shape!')
        elif bmi < 30:
            print('Overweight')
        elif bmi < 35:
            print('Obese Class I Moderately obese')
        elif bmi <= 40:
            print('Obese Class II Severely obese')
        elif bmi > 40:
            print('Very severely obese')

    def body_fat_percentage_categorie(self, bfp, gender):

        category = ""

        if gender[0] == 'M' or gender[0] == 'm':
            if bfp > 25:
                category = "Obese"
            elif 18 <= bfp <= 25:
                category = "Acceptable"
            elif 14 <= bfp <= 17:
                category = "Fitness"
            elif 6 <= bfp <= 13:
                category = "Athletes"
            else:
                category = "Essential Fat"
        else:
            if bfp >= 32:
                category = "Obese"
            elif 25 <= bfp <= 31:
                category = "Acceptable"
            elif 21 <= bfp <= 24:
                category = "Fitness"
            elif 14 <= bfp <= 20:
                category = "Athletes"
            else:
                category = "Essential Fat"
        return category