import unittest
import latin_vocab_quiz

class TestSum(unittest.TestCase):

    def test_conj(self):
        self.assertEqual(len(latin_vocab_quiz.impf_conj(latin_vocab_quiz.do,'2')), 6, "should be six")

if __name__ == '__main__':
    unittest.main()
