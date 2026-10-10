def caesar_encrypt(text, shift):
    new_text = ""
    for l in text:
        if l.isalpha():
            if l.islower():
                pos = ord(l) - ord("a")
                new_l = chr((pos + shift) % 26 + ord("a"))
            elif l.isupper():
                pos = ord(l) - ord("A")
                new_l = chr((pos + shift) % 26 + ord("A"))
        else:
            new_l = l
        new_text += new_l
    return new_text

def caesar_decrypt(text, shift):
    new_text = caesar_encrypt(text, -shift)
    return new_text 

en = caesar_encrypt("Hello, World!", 3)
print(en)
print(caesar_decrypt(en, 3))

