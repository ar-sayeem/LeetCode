class Solution(object):
 def romanToInt(self, s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    s = s.replace('IV', 'IIII')
    s = s.replace('IX', 'VIIII')
    S = s.replace('XL', 'XXXX')
    s = s.replace('XC', 'LXXXX')
    s = s.replace('CD', 'CCCC')
    s = s.replace('CM', 'DCCCC')
    for numeral in s:
        total += roman[numeral]
    return total      