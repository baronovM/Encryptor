class Vigenere:
    """
    Класс, содержащий в виде статических методов функции, относящиеся к шифру Виженера
    """
    @staticmethod
    def handle_key(key: str) -> bytearray:
        """
        Если ключ задан, переводит его в массив байт.
        Иначе же возвращает ключ по умолчанию "password"
        :param key: Ключ в виде строки
        :return: Ключ в виде массива байт
        """
        if key:
            k = bytearray(key.encode())
        else:
            k = bytearray("password".encode())
        return k

    @staticmethod
    def write_key(key: bytearray):
        """
        Выводит ключ в консоль
        :param key: Ключ в виде массиива байт
        :return:
        """
        print(f"Your key: {key.decode()}")

    @staticmethod
    def encrypt(binary_sequence: bytearray, key: bytearray):
        """
        Применяет к последовательности шифр Вижнера
        :param binary_sequence: Шифруемая последовательность
        :param key: Ключ шифрования в виде массива байт
        :return:
        """
        for i in range(len(binary_sequence)):
            binary_sequence[i] = (binary_sequence[i] + key[i % len(key)]) % 256

    @staticmethod
    def decrypt(binary_sequence: bytearray, key: bytearray):
        """
        Расшифровывает зашифрованную шифром Виженера последовательность
        :param binary_sequence: Расшифровываемая последовательность
        :param key: Ключ в виде массива байт
        """
        newkey = bytearray(map(lambda x: (256 - x) % 256, key))
        Vigenere.encrypt(binary_sequence, newkey)

