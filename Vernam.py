import random


class Vernam:
    """
    Класс, содержащий в виде статических методов функции, относящиеся к шифру Вернама
    """
    @staticmethod
    def handle_key(key_filename: str | None) -> str:
        """
        Если имя файла для хранения ключа задано, возвращает его же.
        Иначе возвращает "key", так как по умолчанию ключ хранится в файле "key"
        :param key_filename: Файл для хранения ключа (может быть None)
        :return: Файл для хранения ключа (если был передан None, то вернётся "key")
        """
        if key_filename:
            return key_filename
        return "key"

    @staticmethod
    def write_key(key_filename: str):
        """
        Записывает ключ шифрования в файл
        :param key_filename: Имя файла для записи
        """
        with open(key_filename, "wb") as fkey:
            fkey.write(Vernam.key)

    @staticmethod
    def encrypt(binary_sequence: bytearray, key_filename: str):
        """
        Применяет к последовательности шифр Вернама
        :param binary_sequence: Шифруемая последовательность
        :param key_filename: Файл для записи ключа (в фуекции этот аргумент не используется,
        принимается чтобы ф-ия имела ту же сигнатуру, что и функции шифрования у других шифров)
        """
        Vernam.key = bytearray(random.randbytes(len(binary_sequence)))
        binary_sequence[:] = [binary_sequence[i] ^ Vernam.key[i] for i in range(len(binary_sequence))]

    @staticmethod
    def decrypt(binary_sequence: bytearray, key_filename: str):
        """
        Расшифровывает зашифрованную шифром Вернама последовательность используя ключ из файла с переданным названием
        :param binary_sequence: Расшифровываемая последовательность
        :param key_filename: Имя файла с ключом шифрования
        """
        with open(key_filename, "rb") as fkey:
            key = bytearray(fkey.read())
        binary_sequence[:] = [binary_sequence[i] ^ key[i] for i in range(len(binary_sequence))]
