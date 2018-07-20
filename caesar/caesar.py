from cs50 import get_string
from cs50 import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: ./caesar k\n")
        exit(1)

    key = int(sys.argv[1])
    get_text(key)

def get_text(key):
    prompt = "plaintext: "
    plain_text = get_string(prompt)

    ciphered = []

    for char in plain_text:
        if char.isalpha():
            ciphered.append(cipher(char, key))
        else:
            ciphered.append(char)

    print("ciphertext:","".join(ciphered))

def cipher(char, key):
    if char.isupper():
        return chr(((ord(char) - 65 + key) % 26) + 65)
    else:
        return chr(((ord(char) - 97 + key) % 26) + 97)

if __name__ == "__main__":
    main()
