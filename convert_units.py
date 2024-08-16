__author__ = 'suvasish'


class UnitConversion:
    def __init__(self):
        pass

    def feet_to_inch(self, feet, inch):
        return feet * 12 + inch

    def cm_to_inch(self, height_in_cm):
        return height_in_cm / 2.54

    def inch_to_cm(self, height_in_inch):
        return height_in_inch * 2.54

    def cm_to_meter(self, height_in_cm):
        return height_in_cm * 0.01

    def kg_to_lb(self, kg):
        return kg * 2.20462

    def lb_to_kg(self, lb):
        return lb / 2.20462
