rot = int(input("Input the key: "))
action = input("Do you want to [e]ncrypt or [d]ecrypt?: ")
data = input("Input text: ")

if action == "e" or action == "encrypt":
    text = ""
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord += rot # rotating to the right == encrypting
            char_ord %= 94
            char_ord += 32
            text += chr(char_ord)
        else:
            text += char
    print("cipher: {}".format(text))
elif action == "d" or action == "decrypt":
    text = ""
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord -= rot # rotating to the left == decrypting
            char_ord %= 94
            char_ord += 32
            text += chr(char_ord)
        else:
            text += char
    print("text: {}".format(text))
else:
    print("Error! Wrong operation!")