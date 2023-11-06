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