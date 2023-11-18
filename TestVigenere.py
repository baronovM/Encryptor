import unittest
from Vigenere import Vigenere
import random
from io import StringIO
from unittest.mock import patch


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

    def test_write_key(self):
        key = bytearray(b"QwabE")
        expected_output = f"Your key: {key.decode()}\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            Vigenere.write_key(key)
            self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
