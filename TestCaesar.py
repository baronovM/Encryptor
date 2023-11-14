import unittest
from Caesar import Caesar


class TestCaesar(unittest.TestCase):
    def test_key_handling(self):
        self.assertEqual(Caesar.handle_key("34"), 34)
        self.assertEqual(Caesar.handle_key("0"), 0)
        self.assertEqual(Caesar.handle_key("255"), 255)
        self.assertTrue(Caesar.handle_key(None) in range(1, 256))

    def test_encrypt(self):
        bs = bytearray(b"abcde")
        Caesar.encrypt(bs, 2)
        self.assertEqual(bs, bytearray(b"cdefg"))

        bs = bytearray(b"ABOBA")
        Caesar.encrypt(bs, 4)
        self.assertEqual(bs, bytearray(b"EFSFE"))

    def test_decrypt(self):
        bs = bytearray(b"cdefg")
        Caesar.decrypt(bs, 2)
        self.assertEqual(bs, bytearray(b"abcde"))

        bs = bytearray(b"EFSFE")
        Caesar.decrypt(bs, 4)
        self.assertEqual(bs, bytearray(b"ABOBA"))

    def test_crack(self):
        with open("TestCaesarText.txt", "rb") as ftext:
            text = bytearray(ftext.read())
        bs = text.copy()
        Caesar.encrypt(bs, 17)
        key = Caesar.crack(bs)
        self.assertEqual(text, bs)
        self.assertEqual(key, 17)


if __name__ == '__main__':
    unittest.main()
