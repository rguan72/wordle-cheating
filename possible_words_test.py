import unittest
import possible_words

class TestGetPossibleWords(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(possible_words.PossibleWordGenerator(wordStructure="halts").getPossibleWords(), ["halts"])

    def test_run_through_letters_remaining(self):
        self.assertEqual(
            possible_words.PossibleWordGenerator(wordStructure="*ream", excludeLetters="abefghijklmnopqrstuvwxyz").getPossibleWords(),
            ["cream", "dream"]
        )

    def test_run_through_two_letters_remaining_with_spell_check(self):
        self.assertEqual(
            possible_words.PossibleWordGenerator(wordStructure="**eam", excludeLetters="l").getPossibleWords(),
            ["abeam", "bream", "cream", "dream", "steam"]
        )

    def test_use_five_letters(self):
        self.assertEqual(
            possible_words.PossibleWordGenerator(requireLetters="iltun").getPossibleWords(),
            ["unlit", "until"]
        )

class TestGetUntouchedLetterFrequencies(unittest.TestCase):

    def test_untouched_letters_frequency(self):
        g = possible_words.PossibleWordGenerator(wordStructure="*ream", excludeLetters="b")
        self.assertEqual(
            g.getUntouchedLetterFrequencies(),
            [("c", 0.5), ("d", 0.5)]
        )

    def test_untouched_letters_frequency_wordStructure_exclude_require(self):
        g = possible_words.PossibleWordGenerator(wordStructure="s*ar*", excludeLetters="unlito", requireLetters="h")
        self.assertEqual(
            g.getUntouchedLetterFrequencies(),
            [("d", 0.25), ("e", 0.25), ("k", 0.25), ("p", 0.25)]
        )

if __name__ == "__main__":
    unittest.main()