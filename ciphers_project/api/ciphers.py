
def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        c_encoded = ord(c) + shift
        if(c_encoded > 122):
            back = c_encoded - 123
            c_encoded = 97+back
        else:
            if(97 > c_encoded >90):
                back = c_encoded - 91
                c_encoded = 65 + back
        c_encoded = chr(c_encoded)
        cipher_text += c_encoded
    return cipher_text