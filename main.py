import argparse
from Caesar import Caesar
from Vigenere import Vigenere
from Vernam import Vernam

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
