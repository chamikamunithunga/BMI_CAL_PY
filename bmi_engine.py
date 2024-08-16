__author__ = 'suvasish'

import sys
from bmi_calculation import Bmi
from user_input import UserInput
from bmi_category import BmiCategroy


class BmiEngine:
    def __init__(self):
        pass

    bmi = Bmi()
    input = UserInput()
    category = BmiCategroy()


    def start_bmi(self):

        gender = self.input.get_gender()

        age = self.input.get_age()
        if age < 20: sys.exit("EXIT: Please use 'BMI Calculator for Child and Teens'")

        height, height_unit = self.input.get_height()

        weight, weight_unit = self.input.get_weight()

        bmi_ = self.bmi.calculate_bmi(height, height_unit, weight, weight_unit)
        print("Your BMI: %s" % bmi_)

        recommended_weight = self.bmi.recommend_weight(height, height_unit)
        print("Weight Range: Min - %s Max - %s" % (recommended_weight[0], recommended_weight[1]))

        bfp = self.bmi.body_fat_percent(_gender=gender, _bmi= bmi_, _age=age)
        print("Boby Fat Percentage: %s" % bfp)

        bfp_category = self.bmi.body_fat_category(_bfp=bfp, _gender=gender)
        print("Boby Fat Percentage Category: %s" % bfp_category)


bmi_engine = BmiEngine()
bmi_engine.start_bmi()
