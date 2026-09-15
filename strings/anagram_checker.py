def char_frequency(string):
    count = {}
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def is_anagram(str1, str2):
    return char_frequency(str1) == char_frequency(str2)

print(is_anagram("silent", "listen"))