import unittest
from Vernam import Vernam
import os


class TestVernam(unittest.TestCase):
    def test_key_handling(self):
        self.assertEqual("QwertY", Vernam.handle_key("QwertY"))
        self.assertEqual("key", Vernam.handle_key(None))

    def test_encrypt_decrypt(self):
        st = "String.Test?Message!ABCDEF;1234567891011"
        bs = bytearray(st.encode())
        Vernam.encrypt(bs, "key")
        Vernam.write_key("test_key_file")
        self.assertNotEqual(st.encode(), bs)

        Vernam.decrypt(bs, "test_key_file")
        self.assertEqual(st, bs.decode())

        os.remove("test_key_file")


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
