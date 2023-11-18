import unittest
from Caesar import Caesar
from io import StringIO
from unittest.mock import patch


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

    def test_write_key(self):
        key = 28
        expected_output = f"Your key: {key}\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            Caesar.write_key(key)
            self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
