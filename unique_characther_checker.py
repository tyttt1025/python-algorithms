def char_frequency(string):
    count = {}
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def unique_char(text):
    for i in char_frequency(text).values():
        if i > 1:
            return False
    return True

print(unique_char("abcdef"))