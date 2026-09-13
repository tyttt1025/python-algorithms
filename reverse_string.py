def reverse_string(text):
    result = ""
    for char in range(len(text) - 1, -1, -1):
        result = result + text[char]
    return result

def reverse_string_recursive(word):
    if len(word) == 0:
        return ""
    else:
        return word[-1] + reverse_string_recursive(word[:-1])

print(reverse_string("hello"))
print(reverse_string_recursive("hello"))