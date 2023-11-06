import random


class Caesar:
    @staticmethod
    def handle_key(key: str) -> int:
        if key:
            k = int(key)
        else:
            k = random.randint(1, 255)
        return k

    @staticmethod
    def write_key(key: int):
        print(f"Your key: {key}")

    @staticmethod
    def encrypt(binary_sequence: bytearray, key: int):
        for i in range(len(binary_sequence)):
            binary_sequence[i] = (binary_sequence[i] + key) % 256

    @staticmethod
    def decrypt(binary_sequence: bytearray, key: int):
        Caesar.encrypt(binary_sequence, -key)

    @staticmethod
    def crack(binary_sequence: bytearray) -> int:
        ans = 0
        best_result = 0
        with open("alphabet.txt") as alph:
            freq = list(map(float, alph.read().split()))
            for key in range(256):
                cnt = [0] * 26
                temp = binary_sequence.copy()
                Caesar.decrypt(temp, key)
                for ch in temp:
                    ch = chr(ch)
                    if 'a' <= ch.lower() <= 'z':
                        cnt[ord(ch.lower()) - ord('a')] += 1
                hi = sum([freq[i] * cnt[i] for i in range(26)])
                if hi > best_result:
                    best_result = hi
                    ans = key
        Caesar.decrypt(binary_sequence, ans)
        return ans
