__author__ = 'SA23091184'

from convert_units import UnitConversion


class UserInput:
    def __init__(self):
        pass
    convert = UnitConversion()

    def _get_user_input(self):
        return input()

    def get_gender(self):
        print("Gender: Press F(Female) or M(Male)", flush=True)
        return self._get_user_input()

    def get_age(self):
        print("AGE: ", flush=True)
        return float(self._get_user_input())

    def get_height(self):
        print("HEIGHT: Press F(Feet-inch) or M(Meter): ", flush=True)
        choice = self._get_user_input().lower()
        if choice == 'f':
            print('Height in Feet-inch: ', flush=True)
            return str(self._get_user_input()), choice
       
        elif choice == 'm':
            print('Height in Meter: ', flush=True)
            return float(self._get_user_input()), choice
        else:
            raise ValueError("height must be 'Feet inch(f)'or 'Meter(m)'")

    def get_weight(self):
        print("WEIGHT: Press L(Pound) or K(Kilogram): ", flush=True)
        choice = self._get_user_input().lower()
        if choice == 'k':
            print("WEIGHT in Kilogram: ", flush=True)
            weight_in_kg = float(self._get_user_input())
            return weight_in_kg, choice
        elif choice == 'l':
            print("WEIGHT in Pound: ", flush=True)
            weight_in_lb = float(self._get_user_input())
            return weight_in_lb, choice
        else:
            raise ValueError("Input must be 'Kilogram(k) or 'Pound(l)'")
