import unittest
import word_gen

# how does unittest work?
class TestGetNovelLetters(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(word_gen.getNovelLetters("soare", ["hello"]), {"hl": ["hello"]})

    def test_alphabetical(self):
        self.assertEqual(word_gen.getNovelLetters("soare", ["snarl"]), {"ln": ["snarl"]})

    def test_multiple_words(self):
        self.assertEqual(word_gen.getNovelLetters("soare", ["hello", "snarl"]), {"hl": ["hello"], "ln": ["snarl"]})

    def test_multiple_anagrams(self):
        self.assertEqual(word_gen.getNovelLetters("soare", ["alert", "alter"]), {"lt": ["alert", "alter"]})

    def test_anagram_of_original_word(self):
        self.assertEqual(word_gen.getNovelLetters("alter", ["alert"]), {"": ["alert"]})


if __name__ == "__main__":
    unittest.main()
