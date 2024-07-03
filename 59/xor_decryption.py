from itertools import combinations, permutations
import string
from collections import Counter
import numpy as np

def create_decryptor(chars : list[str]):
    """
    Creates a decryptor for a given XOR cipher.
    """
    def decryptor(cipher : list[int]):
        """
        Deciphers a code that was created with a XOR cipher based on the given characters.
        """
        chars_index = 0
        chars_len = len(chars)
        chars_ord = [ord(char) for char in chars]
        cipher_index = 0
        cipher_len = len(cipher)
        res = ""
        while(cipher_index < cipher_len):
            res += chr(cipher[cipher_index] ^ chars_ord[chars_index])
            cipher_index += 1
            chars_index = (chars_index + 1) % chars_len
        return res

    return decryptor

def not_substrings(strings : str, text : str):
    for string in strings:
        if string in text:
            return False
    return True

def are_substrings(strings : str, text : str):
    for string in strings:
        if string not in text:
            return False
    return True

if __name__ == "__main__":
    lowercase_alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    alphabet = set(string.ascii_letters + string.digits + " .,:;+?!/[]()'\"")
    with open("chiper.txt") as file:
        input = file.read()
    ciphered_text = [int(num) for num in input.split(",")]

    original_text = ""

    for comb in combinations(lowercase_alphabet, 3):
        for perm in permutations(comb):
            cipher = ''.join(list(perm))

            decryptor = create_decryptor(cipher)
            deciphered_text = decryptor(ciphered_text)
            symbol_counts = Counter(deciphered_text)
            most_common_symbol = max(symbol_counts, key = symbol_counts.get)
            if(most_common_symbol == " " and set(deciphered_text) <= alphabet):
                original_text = deciphered_text
                break
        else:
            continue
        break
    print(np.sum([ord(char) for char in original_text]))
