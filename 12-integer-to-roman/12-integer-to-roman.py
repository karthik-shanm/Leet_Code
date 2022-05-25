class Solution:
    dict_roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    dict_int = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }
    dict_def = { 4: 'IV', 40: 'XL', 400:'CD', 9:'IX', 90:'XC', 900:'CM'}

    def get_romans(self, unit_val, roman_values):
        itr = 0
        sum = 0
        roman_equ = []
        while itr <= 3 and unit_val>0:
            itr += 1
            if unit_val in roman_values:
                sum += unit_val
                roman_equ.append(self.dict_int[unit_val])            
                unit_val -= unit_val
            else:
                high_val = [x for x in roman_values if x <= unit_val][0] 
                sum += high_val
                roman_equ.append(self.dict_int[high_val])
                unit_val -= high_val

        return ''.join(roman_equ), unit_val, itr

    def intToRoman(self, num: str) -> str:
        num_str = str(num)
        len_inp = len(num_str)
        roman_str = ""
        for i in range(len_inp):
            unit_val = int(num_str[-(i+1)]) * pow(10,i)
    
            if self.dict_def.get(unit_val):
                roman_equ = self.dict_def[unit_val]
            else:
                possible_romans = { key:val for key,val in self.dict_roman.items() if val <= unit_val}
                possible_romans_vals = sorted(list(possible_romans.values()), reverse=True)
                roman_equ, t_unit_val, itr = self.get_romans(unit_val, possible_romans_vals)
                
            roman_str = roman_equ + roman_str
        return roman_str
