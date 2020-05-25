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

    def test_conjugation_output(self):

        # 1st conj

        # present
        self.assertEqual(RegularVerb(['amo', 'amare']).present_tense(True, True), ['amo', 'amas', 'amat', 'amamus', 'amatis', 'amant']) # pres ind act
        self.assertEqual(RegularVerb(['amo', 'amare']).present_tense(False, True), ['amem', 'ames', 'amet', 'amemus', 'ametis', 'ament']) # pres subj act
        self.assertEqual(RegularVerb(['amo', 'amare']).present_tense(True, False), ['amor', 'amaris', 'amatur', 'amamur', 'amamini', 'amantur']) # pres ind pass
        self.assertEqual(RegularVerb(['amo', 'amare']).present_tense(False, False), ['amer', 'ameris', 'ametur', 'amemur', 'amemini', 'amentur']) # pres subj pass

        # imperfect
        self.assertEqual(RegularVerb(['amo', 'amare']).imperfect_tense(True, True), ['amabam', 'amabas', 'amabat', 'amabamus', 'amabatis', 'amabant']) # impf ind act
        self.assertEqual(RegularVerb(['amo', 'amare']).imperfect_tense(False, True), ['amarem', 'amares', 'amaret', 'amaremus', 'amaretis', 'amarent']) # impf subj act
        self.assertEqual(RegularVerb(['amo', 'amare']).imperfect_tense(True, False), ['amabar', 'amabaris', 'amabatur', 'amabamur', 'amabamini', 'amabantur']) # impf ind pass
        self.assertEqual(RegularVerb(['amo', 'amare']).imperfect_tense(False, False), ['amarer', 'amareris', 'amaretur', 'amaremur', 'amaremini', 'amarentur']) # impf subj pass

        # 2nd conj

        # present
        self.assertEqual(RegularVerb(['moneo', 'monere']).present_tense(True, True), ['moneo', 'mones', 'monet', 'monemus', 'monetis', 'monent']) # pres ind act
        self.assertEqual(RegularVerb(['moneo', 'monere']).present_tense(False, True), ['moneam', 'moneas', 'moneat', 'moneamus', 'moneatis', 'moneant']) # pres subj act
        self.assertEqual(RegularVerb(['moneo', 'monere']).present_tense(True, False), ['moneor', 'moneris', 'monetur', 'monemur', 'monemini', 'monentur']) # pres ind pass
        self.assertEqual(RegularVerb(['moneo', 'monere']).present_tense(False, False), ['monear', 'monearis', 'moneatur', 'moneamur', 'moneamini', 'moneantur']) # pres subj pass

        # imperfect
        self.assertEqual(RegularVerb(['moneo', 'monere']).imperfect_tense(True, True), ['monebam', 'monebas', 'monebat', 'monebamus', 'monebatis', 'monebant']) # impf ind act
        self.assertEqual(RegularVerb(['moneo', 'monere']).imperfect_tense(False, True), ['monerem', 'moneres', 'moneret', 'moneremus', 'moneretis', 'monerent']) # impf subj act
        self.assertEqual(RegularVerb(['moneo', 'monere']).imperfect_tense(True, False), ['monebar', 'monebaris', 'monebatur', 'monebamur', 'monebamini', 'monebantur']) # impf ind pass
        self.assertEqual(RegularVerb(['moneo', 'monere']).imperfect_tense(False, False), ['monerer', 'monereris', 'moneretur', 'moneremur', 'moneremini', 'monerentur']) # impf subj pass

        # 3rd conj

        # present
        self.assertEqual(RegularVerb(['rego', 'regere']).present_tense(True, True), ['rego', 'regis', 'regit', 'regimus', 'regitis', 'regunt']) # pres ind act
        self.assertEqual(RegularVerb(['rego', 'regere']).present_tense(False, True), ['regam', 'regas', 'regat', 'regamus', 'regatis', 'regant']) # pres subj act
        self.assertEqual(RegularVerb(['rego', 'regere']).present_tense(True, False), ['regor', 'regeris', 'regitur', 'regimur', 'regimini', 'reguntur']) # pres ind pass
        self.assertEqual(RegularVerb(['rego', 'regere']).present_tense(False, False), ['regar', 'regaris', 'regatur', 'regamur', 'regamini', 'regantur']) # pres subj pass

        # imperfect
        self.assertEqual(RegularVerb(['rego', 'regere']).imperfect_tense(True, True), ['regebam', 'regebas', 'regebat', 'regebamus', 'regebatis', 'regebant']) # impf ind act
        self.assertEqual(RegularVerb(['rego', 'regere']).imperfect_tense(False, True), ['regerem', 'regeres', 'regeret', 'regeremus', 'regeretis', 'regerent']) # impf subj act
        self.assertEqual(RegularVerb(['rego', 'regere']).imperfect_tense(True, False), ['regebar', 'regebaris', 'regebatur', 'regebamur', 'regebamini', 'regebantur']) # impf ind pass
        self.assertEqual(RegularVerb(['rego', 'regere']).imperfect_tense(False, False), ['regerer', 'regereris', 'regeretur', 'regeremur', 'regeremini', 'regerentur']) # impf subj pass

        # 3rd io conj

        # present
        self.assertEqual(RegularVerb(['capio', 'capere']).present_tense(True, True), ['capio', 'capis', 'capit', 'capimus', 'capitis', 'capiunt']) # pres ind act
        self.assertEqual(RegularVerb(['capio', 'capere']).present_tense(False, True), ['capiam', 'capias', 'capiat', 'capiamus', 'capiatis', 'capiant']) # pres subj act
        self.assertEqual(RegularVerb(['capio', 'capere']).present_tense(True, False), ['capior', 'caperis', 'capitur', 'capimur', 'capimini', 'capiuntur']) # pres ind pass
        self.assertEqual(RegularVerb(['capio', 'capere']).present_tense(False, False), ['capiar', 'capiaris', 'capiatur', 'capiamur', 'capiamini', 'capiantur']) # pres subj pass

        # imperfect
        self.assertEqual(RegularVerb(['capio', 'capere']).imperfect_tense(True, True), ['capiebam', 'capiebas', 'capiebat', 'capiebamus', 'capiebatis', 'capiebant']) # impf ind act
        self.assertEqual(RegularVerb(['capio', 'capere']).imperfect_tense(False, True), ['caperem', 'caperes', 'caperet', 'caperemus', 'caperetis', 'caperent']) # impf subj act
        self.assertEqual(RegularVerb(['capio', 'capere']).imperfect_tense(True, False), ['capiebar', 'capiebaris', 'capiebatur', 'capiebamur', 'capiebamini', 'capiebantur']) # impf ind pass
        self.assertEqual(RegularVerb(['capio', 'capere']).imperfect_tense(False, False), ['caperer', 'capereris', 'caperetur', 'caperemur', 'caperemini', 'caperentur']) # impf subj pass

        # 4th conj

if __name__ == "__main__":
    unittest.main()
