import unittest
import random
from Vigenere import Vigenere


class TestVigenere(unittest.TestCase):
    def test_key_handling(self):
        self.assertEqual(Vigenere.handle_key("hello"), bytearray(b"hello"))
        self.assertEqual(Vigenere.handle_key(None), bytearray(b"password"))

    def test_encrypt(self):
        bs = bytearray(b"aBcde")
        Vigenere.encrypt(bs, bytearray([0, 1, 2, 0, 1]))
        self.assertEqual(bs, bytearray(b"aCedf"))

        a = bytearray(b"ABOBA")
        Vigenere.encrypt(a, bytearray(b"Qwer3"))
        b = bytearray(b"Qwer3")
        Vigenere.encrypt(b, bytearray(b"ABOBA"))
        self.assertEqual(a, b)

    def test_decrypt(self):
        bs = bytearray(b"aCedf")
        Vigenere.decrypt(bs, bytearray([0, 1, 2, 0, 1]))
        self.assertEqual(bs, bytearray(b"aBcde"))

        a = bytearray(random.randbytes(50))
        key = bytearray(random.randbytes(7))
        key[3] = 13
        b = a.copy()
        Vigenere.encrypt(b, key)
        self.assertNotEqual(a, b)
        Vigenere.decrypt(b, key)
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
