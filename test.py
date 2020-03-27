import unittest
from conjugation import impf_conj, pres_conj
from data import do, capio, audio, rego


class TestConj(unittest.TestCase):

    def test_pres_conj_lengths(self):

        self.assertEqual(len(pres_conj(audio, '4')), 6)
        self.assertEqual(len(pres_conj(capio, '3io',True)), 6)
        self.assertEqual(len(pres_conj(rego, '3',True)), 6)
        self.assertEqual(len(pres_conj(rego, '3')), 6)

    def test_impf_conj_lengths(self):

        self.assertEqual(len(impf_conj(do, '2')), 6)
        self.assertEqual(len(impf_conj(capio, '3io', True)), 6)
        self.assertEqual(len(impf_conj(capio, '3io')), 6)
        self.assertEqual(len(impf_conj(audio, '4', True)), 6)

    def test_pres_conj_values(self):

        self.assertEqual(
            pres_conj(audio, '4'),
            ['audio', 'audis', 'audit', 'audimus', 'auditis', 'audiunt']
        )
        self.assertEqual(
            pres_conj(capio, '3io', True),
            ['capior', 'caperis', 'capitur', 'capimur', 'capimini', 'capiuntur']
        )
        self.assertEqual(
            pres_conj(rego, '3', True),
            ['regor', 'regeris', 'regitur', 'regimur', 'regimini', 'reguntur']
        )
        self.assertEqual(
            pres_conj(rego, '3'),
            ['rego', 'regis', 'regit', 'regimus', 'regitis', 'regunt']
        )

    def test_impf_conj_values(self):

        self.assertEqual(
            impf_conj(do, '2'),
            ['dabam', 'dabas', 'dabat', 'dabamus', 'dabatis', 'dabant']
        )
        self.assertEqual(
            impf_conj(capio, '3io', True),
            ['capiebar', 'capiebaris', 'capiebatur', 'capiebamur', 'capiebamini', 'capiebantur']
        )
        self.assertEqual(
            impf_conj(capio, '3io'),
            ['capiebam', 'capiebas', 'capiebat', 'capiebamus', 'capiebatis', 'capiebant']
        )
        self.assertEqual(
            impf_conj(audio, '4', True),
            ['audiebar', 'audiebaris', 'audiebatur', 'audiebamur', 'audiebamini', 'audiebantur']
        )


if __name__ == "__main__":
    unittest.main()
