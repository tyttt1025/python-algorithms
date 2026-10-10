def roman_to_int(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = []
    result = 0
    next_value = 0
    checked = False
    for w in s:
        if w.upper() not in values:
            return "not roman numerals"
    for i, c in enumerate(s):
        value = values.get(c.upper())
        try:
            next_value = values.get(s[i + 1].upper())
        except IndexError:
            next_value = 0
        if value < next_value and not checked:
            number.append(next_value - value)
            checked = True
        elif value > next_value and not checked:
            number.append(value)
        elif value == next_value:
            number.append(value)
        elif checked:
            checked = False
    for n in number:
        result += n
    return result

print(roman_to_int("MCMXCIV"))

