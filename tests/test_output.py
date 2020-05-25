import unittest
from core.classes import RegularVerb


class TestConjugation(unittest.TestCase):

    def test_conjugation_types(self):

        laudo = ['laudo', 'laudare', 'laudavi', 'laudatus']
        self.assertEqual(RegularVerb(laudo).get_conjugation(), "1")

        moneo = ['moneo', 'monere', 'monui', 'monitus']
        self.assertEqual(RegularVerb(moneo).get_conjugation(), "2")

        rego = ['rego', 'regere', 'rexi', 'rectus']
        self.assertEqual(RegularVerb(rego).get_conjugation(), "3")

        capio = ['capio', 'capere', 'cepi', 'captus']
        self.assertEqual(RegularVerb(capio).get_conjugation(), "3io")

        audio = ['audio', 'audire', 'audivi', 'auditus']
        self.assertEqual(RegularVerb(audio).get_conjugation(), "4")

        timeo = ['timeo', 'timere', 'timui']
        self.assertEqual(RegularVerb(timeo).get_conjugation(), "2")

    def test_conjugation_length(self):

        laudo = ['laudo', 'laudare', 'laudavi', 'laudatus']
        self.assertEqual(len(RegularVerb(laudo).present_tense(True, True)), 6)


if __name__ == "__main__":
    unittest.main()
