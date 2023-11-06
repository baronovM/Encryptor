class Vigenere:
    @staticmethod
    def handle_key(key: str) -> bytearray:
        if key:
            k = bytearray(key.encode())
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
        newkey = bytearray(map(lambda x: (256 - x) % 256, key))
        Vigenere.encrypt(binary_sequence, newkey)

