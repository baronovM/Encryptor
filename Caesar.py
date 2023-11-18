import random


class Caesar:
    """
    Класс, содержащий в виде статических методов функции, относящиеся к шифру Цезаря
    """
    @staticmethod
    def handle_key(key: str | None) -> int:
        """
        Если ключ задан, функция переводит его из строки в число.
        Иначе ключ выбирается случайным образом из диапазона [1, 255]
        """
        if key:
            k = int(key)
        else:
            k = random.randint(1, 255)
        return k

    @staticmethod
    def write_key(key: int):
        """
        Вывод ключа в консоль
        """
        print(f"Your key: {key}")

    @staticmethod
    def encrypt(binary_sequence: bytearray, key: int):
        """
        Применяет к последовательности шифр Цезаря
        :param binary_sequence: Шифруемая последовательность
        :param key: Ключ шифрования
        """
        for i in range(len(binary_sequence)):
            binary_sequence[i] = (binary_sequence[i] + key) % 256

    @staticmethod
    def decrypt(binary_sequence: bytearray, key: int):
        """
        Расшифровывает последовательность используя ключ
        :param binary_sequence: Расшифровываемая последовательность
        :param key: Ключ
        """
        Caesar.encrypt(binary_sequence, -key)

    @staticmethod
    def crack(binary_sequence: bytearray) -> int:
        """
        Методом частотного анализа находит подходящий ключ, возвращает его
        и расшифровывает последовательность
        :param binary_sequence: Взламываемая последовательность
        :return: Найденный ключ
        """
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
