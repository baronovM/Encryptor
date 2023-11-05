import random
import argparse


class Caesar:
    @staticmethod
    def handle_key(key: str) -> int:
        if key:
            k = int(key)
        else:
            k = random.randint(1, 255)
        return k

    @staticmethod
    def write_key(key: bytearray):
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


class Vigenere:
    @staticmethod
    def handle_key(key: str) -> bytearray:
        if key:
            k = bytearray(args.key.encode())
        else:
            k = bytearray("password".encode())
        return k

    @staticmethod
    def write_key(key: bytearray):
        print(f"Your key: {key.decode()}")

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
    def handle_key(key_filename: str) -> str:
        if key_filename:
            return key_filename
        return "key"

    @staticmethod
    def write_key(key_filename: str):
        with open(key_filename, "wb") as fkey:
            fkey.write(Vernam.key)

    @staticmethod
    def encrypt(binary_sequence: bytearray, key_filename: str):
        Vernam.key = bytearray(random.randbytes(len(binary_sequence)))
        binary_sequence[:] = [binary_sequence[i] ^ Vernam.key[i] for i in range(len(binary_sequence))]

    @staticmethod
    def decrypt(binary_sequence: bytearray, key_filename: str):
        with open(key_filename, "rb") as fkey:
            key = bytearray(fkey.read())
        binary_sequence[:] = [binary_sequence[i] ^ key[i] for i in range(len(binary_sequence))]


cipher_dict = {
    "Caesar": Caesar,
    "Vigenere": Vigenere,
    "Vernam": Vernam
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Encrypt files with different types of ciphers")
    parser.add_argument("command", type=str, help="e/d/c (Encrypt/Decrypt/Crack_cipher)")
    parser.add_argument("cipher", type=str, help=f"Cipher type name ({'/'.join(cipher_dict.keys())})")
    parser.add_argument("input_file", type=str, help="Input file name")
    parser.add_argument("output_file", type=str, help="Output file name (default: output)", default="output")
    parser.add_argument("-k", "--key")

    args = parser.parse_args()

    args.key = cipher_dict[args.cipher].handle_key(args.key)

    with open(args.input_file, "rb") as fin:
        r = bytearray(fin.read())

        if args.command[0].lower() == "e":
            cipher_dict[args.cipher].encrypt(r, args.key)
            cipher_dict[args.cipher].write_key(args.key)
        elif args.command[0].lower() == "d":
            cipher_dict[args.cipher].decrypt(r, args.key)
        elif args.command[0].lower() == "c":
            args.key = cipher_dict[args.cipher].crack(r)
            cipher_dict[args.cipher].write_key(args.key)

        with open(args.output_file, "wb") as fout:
            fout.write(r)
