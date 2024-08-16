__author__ = 'suvasish'

from convert_units import UnitConversion
from bmi_category import BmiCategroy


class Bmi:
    def __init__(self):
        pass

    convert = UnitConversion()
    category = BmiCategroy()


    def body_fat_percent(self, _gender, _bmi, _age):
        # Adult Body Fat % = (1.20 x BMI) + (0.23 x Age) – (10.8 x gender) – 5.4
        # using gender male = 1, female = 0.
        if _gender[0] == 'M' or _gender[0] == 'm':
            return round(((1.20 * _bmi) + (0.23 * _age) - 10.8 - 5.4), 1)
        elif _gender[0] == 'F' or _gender[0] == 'f':
            return round(((1.20 * _bmi) + (0.23 * _age) - 5.4), 1)

    def recommend_weight(self, height, unit):
        weight_range = []
        height_in_meter = self.convert_to_meter(height, unit)
        weight_range.append(round((18.5 * (height_in_meter * height_in_meter)), 1))
        weight_range.append(round((25 * (height_in_meter * height_in_meter)), 1))
        return weight_range

    def convert_to_meter(self, height, unit):
        if unit == 'f':
            if '.' in str(height):
                inp = str(height).split('.')
            else:
                inp = str(height).split()
            height_in_inch = self.convert.feet_to_inch(float(inp[0]), float(inp[1]))
            height_in_cm = self.convert.inch_to_cm(height_in_inch)
            height_in_meter = self.convert.cm_to_meter(height_in_cm)
            return height_in_meter
        elif unit == 'm':
            return height
        elif unit == 'c':
            height_in_meter = self.convert.cm_to_meter(height)
            return height_in_meter

    def convert_to_kg(self, weight, unit):
        if unit == 'k':
            return weight
        if unit == 'l':
            weight_in_kg = self.convert.lb_to_kg(weight)
            return weight_in_kg

    def calculate_bmi(self, height, height_unit, weight, weight_unit):
        height_in_meter = self.convert_to_meter(height, height_unit)
        weight_in_kg = self.convert_to_kg(weight, weight_unit)
        bmi = round((weight_in_kg/(height_in_meter * height_in_meter)), 1)
        self.category.bmi_category(bmi)
        return bmi

    def body_fat_category(self, _bfp, _gender):
        return self.category.body_fat_percentage_categorie(bfp=_bfp, gender=_gender)

