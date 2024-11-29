class VigenereCipher(object):
    def __init__(self, key: str, abc: str):
        self.abc = abc
        self.key = key

    def encode(self, text: str, key: str = None) -> str:
        key = key or self.key
        encoded_text = ''

        for i, ch in enumerate(text):

            if ch not in self.abc:
                encoded_text += ch
            else:
                encoded_text += self.abc[(self.abc.index(ch) + self.abc.index(key[i % len(key)])) % len(self.abc)]

        return encoded_text

    def decode(self, text: str) -> str:
        decoding_key = ''.join([self.abc[-(self.abc.index(ch))] for ch in self.key])
        return self.encode(text, decoding_key)


abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

# print(c.abc)

print(c.encode('codewars'))
print(c.decode('rovwsoiv'))
