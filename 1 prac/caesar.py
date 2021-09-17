from typing import List

alphabet: List[str] = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
key_word: str = 'key'
shift: int = 3


def cipher(letter: str, alphabet: List[str], shift: int, key_word: str):
    assert len(letter) == 1
    assert len(alphabet) >= len(key_word)
    assert len(set(key_word)) == len(key_word)

    without_key = [letter for letter in alphabet if letter not in key_word]
    new_alphabet = list(reversed(without_key[-shift:])) + list(key_word) + without_key[:-shift]
    letter_index = alphabet.index(letter)
    return new_alphabet[letter_index]


def cipher_key_key(letter: str, alphabet: List[str], key_word: str, len_word: int, letter_index: int):
    assert len(letter) == 1
    assert len(alphabet) >= len(key_word)
    assert len(set(key_word)) == len(key_word)

    key_phrase = [key_word[i % len(key_word)] for i in range(len_word)]

    new_index = (ord(letter) + ord(key_phrase[letter_index])) % len(alphabet)
    return alphabet[new_index]


if __name__ == '__main__':
    alphabet: List[str] = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
    key_word: str = 'key'
    shift: int = 3

    word = 'cipherme'

    new_word = "".join([cipher(letter, alphabet, shift, key_word) for letter in word])
    new_word_2 = "".join([cipher_key_key(letter, alphabet, key_word, len(word), i) for i, letter in enumerate(word)])

    print(new_word)
    print(new_word_2)

print("Done")
