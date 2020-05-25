import unittest
from core.classes import Verb


class TestConjugation(unittest.TestCase):

    def test_conjugation_types(self):

        laudo = ['laudo', 'laudare', 'laudavi', 'laudatus']
        self.assertEqual(Verb(laudo).get_conjugation(), "1")

        moneo = ['moneo', 'monere', 'monui', 'monitus']
        self.assertEqual(Verb(moneo).get_conjugation(), "2")

        rego = ['rego', 'regere', 'rexi', 'rectus']
        self.assertEqual(Verb(rego).get_conjugation(), "3")

        capio = ['capio', 'capere', 'cepi', 'captus']
        self.assertEqual(Verb(capio).get_conjugation(), "3io")

        audio = ['audio', 'audire', 'audivi', 'auditus']
        self.assertEqual(Verb(audio).get_conjugation(), "4")

        timeo = ['timeo', 'timere', 'timui']
        self.assertEqual(Verb(timeo).get_conjugation(), "2")


if __name__ == "__main__":
    unittest.main()
