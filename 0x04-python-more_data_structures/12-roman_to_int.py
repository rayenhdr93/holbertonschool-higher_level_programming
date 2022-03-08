#!/usr/bin/python3
def roman_to_int(roman_string):
    if str(roman_string) == roman_string and not None:
        x = 0
        t = 1
        list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        i = len(roman_string)
        while i > 0:
            i += -1
            j = 0
            d = 0
            while list[j] != roman_string[i]:
                j += 1
            if i != 0:
                if ((roman_string[i] == 'X' or 'C' or 'M') and (roman_string[
                        i - 1] == list[j - 2])):
                    t = 0.9
                    d = 1
                elif ((roman_string[i] == 'V' or 'L' or 'D') and (roman_string[
                        i - 1] == list[j - 1])):
                    t = 0.8
                    d = 1
                else:
                    t = 1
            else:
                t = 1
            if roman_string[i] == 'D':
                x += 500 * t
            elif roman_string[i] == 'C':
                x += 100 * t
            elif roman_string[i] == 'L':
                x += 50 * t
            elif roman_string[i] == 'X':
                x += 10 * t
            elif roman_string[i] == 'V':
                x += 5 * t
            elif roman_string[i] == 'I':
                x += 1 * t
            elif roman_string[i] == 'M':
                x += 1000 * t
            if d:
                i += -1
        return int(x)
    else:
        return 0
