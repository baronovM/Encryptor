import random
import argparse


class Caesar:
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


class Vigenere:
    @staticmethod
    def encrypt(binary_sequence: bytearray, key: bytearray):
        for i in range(len(binary_sequence)):
            binary_sequence[i] = (binary_sequence[i] + key[i % len(key)]) % 256

    @staticmethod
    def decrypt(binary_sequence: bytearray, key: bytearray):
        newkey = bytearray(map(lambda x: 256 - x, key))
        Vigenere.encrypt(binary_sequence, newkey)


class Vernam:
    @staticmethod
    def encrypt_vernam(binary_sequence: bytearray, key: bytearray):
        key[:] = bytearray(random.randbytes(len(binary_sequence)))
        binary_sequence[:] = [binary_sequence[i] ^ key[i] for i in range(len(binary_sequence))]

    @staticmethod
    def decrypt_vernam(binary_sequence: bytearray, key: bytearray):
        binary_sequence[:] = [binary_sequence[i] ^ key[i] for i in range(len(binary_sequence))]


cipher_dict = {
    "Caesar": Caesar,
    "Vigenere": Vigenere,
    "Vernam": Vernam
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Encrypt files with different types of ciphers")
    parser.add_argument("command", type=str, help="Encrypt/Decrypt/Crack_cipher")
    parser.add_argument("cipher", type=str, help=f"Cipher type name ({'/'.join(cipher_dict.keys())})")
    parser.add_argument("input_file", type=str, help="Input file name")
    parser.add_argument("output_file", type=str, help="Output file name (default: output)", default="output")
    parser.add_argument("-k", "--key")

    args = parser.parse_args()

    if args.key:
        args.key = int(args.key)

    with open(args.input_file, "rb") as fin:
        fout = open(args.output_file, "wb")
        r = bytearray(fin.read())

        if args.command == "Encrypt":
            cipher_dict[args.cipher].encrypt(r, args.key)
        elif args.command == "Decrypt":
            cipher_dict[args.cipher].decrypt(r, args.key)
        elif args.command == "Crack_cipher":
            args.key = cipher_dict[args.cipher].crack(r)

        fout.write(r)
        fout.close()
        print(f"Your key: {args.key}")
