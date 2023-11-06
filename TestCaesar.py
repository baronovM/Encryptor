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
        text = bytearray("""
        At a few minutes before midnight Hamlet and Horatio went out into the cold night and climbed up to the watch platform and joined Marcellus.
‘It’s biting cold,’ said Hamlet.
‘A nipping and stinging air,’ said Horatio.
‘What’s the time?’
‘Not yet twelve, I think,’ said Horatio.
‘No, it’s struck.’
‘Really? I didn’t hear it. Then it’s the time that the ghost usually walks.’ There was a flourish of trumpets and a huge banging of drums. ‘What’s that, my lord?’
‘The king is staying up tonight, carousing. Singing, dancing. And as he drinks his draughts of Rhineland wine, the kettle-drum and trumpet bray out his glorious achievement as a boozer .’
‘Is it a local custom?’
‘Yes, it is. But to my mind, although I’m a native here, and to the manner born, it’s a custom more honoured in the breach than the observance. This heavy-handed revelry makes our neighbours east and west censure us. 
They refer to Danes as drunkards and foul our reputation with swinish adjectives. And, to tell you the truth, it detracts from our achievements, though, at their best, they’re significant.
It’s like it is with some men, who because of a vicious flaw in their nature, such as their class – which they’re not guilty of – since people can’t choose their origins, are unjustly condemned.
Things like a too well-developed temper that sometimes overwhelms their reason, or a habit that makes them bad-mannered, no matter how great their strong points are, no matter that they may be as good as a man can be, can cause the finger to be pointed at that one fault.
That drop of evil may bring doubt on the whole man.’
                       """.encode())
        bs = text.copy()
        Caesar.encrypt(bs, 17)
        key = Caesar.crack(bs)
        self.assertEqual(text, bs)
        self.assertEqual(key, 17)


if __name__ == '__main__':
    unittest.main()
