import unittest
from core.classes import RegularVerb


data = [
    (['amo', 'amare', 'amavi', 'amatus'], "1"), # 1st conj
    (['moneo', 'monere', 'monui', 'monitus'], "2"), # 2nd conj
    (['rego', 'regere', 'rexi', 'rectus'], "3"), # 3rd conj
    (['capio', 'capere', 'cepi', 'captus'], "3io"), # 3rd io conj
    (['audio', 'audire', 'audivi', 'auditus'], "4"), # 4th conj
    (['timeo', 'timere', 'timui'], "2"), # missing 4th principal part
    (['impero', 'imperare'], "1") # only 1st two principal parts
]


class TestConjugation(unittest.TestCase):

    def test_conjugation_types(self):

        check_assertion = lambda x, i: self.assertEqual(RegularVerb(x).get_conjugation(), i)

        self.assertTrue(all(check_assertion for x, i in data))

    def test_conjugation_lengths(self):

        check_length = lambda x, i: self.assertEqual(len(RegularVerb(x).get_conjugation()), 6)

        self.assertTrue(all(check_length for x, i in data))

    def test_conjugation_outputs(self):

        # 1st conj

        # present
        self.assertEqual(RegularVerb(data[0][0]).present_tense('ind', True), ['amo', 'amas', 'amat', 'amamus', 'amatis', 'amant']) # pres ind act
        self.assertEqual(RegularVerb(data[0][0]).present_tense('subj', True), ['amem', 'ames', 'amet', 'amemus', 'ametis', 'ament']) # pres subj act
        self.assertEqual(RegularVerb(data[0][0]).present_tense('ind', False), ['amor', 'amaris', 'amatur', 'amamur', 'amamini', 'amantur']) # pres ind pass
        self.assertEqual(RegularVerb(data[0][0]).present_tense('subj', False), ['amer', 'ameris', 'ametur', 'amemur', 'amemini', 'amentur']) # pres subj pass
        self.assertEqual(RegularVerb(data[0][0]).present_tense('imp', True), ['ama', 'amate']) # pres imp act
        self.assertEqual(RegularVerb(data[0][0]).present_tense('imp', False), 'The passive imperative exists mostly in deponent verbs.') # pres imp act

        # imperfect
        self.assertEqual(RegularVerb(data[0][0]).imperfect_tense(True, True), ['amabam', 'amabas', 'amabat', 'amabamus', 'amabatis', 'amabant']) # impf ind act
        self.assertEqual(RegularVerb(data[0][0]).imperfect_tense(False, True), ['amarem', 'amares', 'amaret', 'amaremus', 'amaretis', 'amarent']) # impf subj act
        self.assertEqual(RegularVerb(data[0][0]).imperfect_tense(True, False), ['amabar', 'amabaris', 'amabatur', 'amabamur', 'amabamini', 'amabantur']) # impf ind pass
        self.assertEqual(RegularVerb(data[0][0]).imperfect_tense(False, False), ['amarer', 'amareris', 'amaretur', 'amaremur', 'amaremini', 'amarentur']) # impf subj pass

        # future
        self.assertEqual(RegularVerb(data[0][0]).future_tense(True), ['amabo', 'amabis', 'amabit', 'amabimus', 'amabitis', 'amabunt']) # fut ind act
        self.assertEqual(RegularVerb(data[0][0]).future_tense(False), ['amabor', 'amaberis', 'amabitur', 'amabimur', 'amabimini', 'amabuntur']) # fut ind pass

        # 2nd conj

        # present
        self.assertEqual(RegularVerb(data[1][0]).present_tense('ind', True), ['moneo', 'mones', 'monet', 'monemus', 'monetis', 'monent']) # pres ind act
        self.assertEqual(RegularVerb(data[1][0]).present_tense('subj', True), ['moneam', 'moneas', 'moneat', 'moneamus', 'moneatis', 'moneant']) # pres subj act
        self.assertEqual(RegularVerb(data[1][0]).present_tense('ind', False), ['moneor', 'moneris', 'monetur', 'monemur', 'monemini', 'monentur']) # pres ind pass
        self.assertEqual(RegularVerb(data[1][0]).present_tense('subj', False), ['monear', 'monearis', 'moneatur', 'moneamur', 'moneamini', 'moneantur']) # pres subj pass
        self.assertEqual(RegularVerb(data[1][0]).present_tense('imp', True), ['mone', 'monete']) # pres imp act
        self.assertEqual(RegularVerb(data[1][0]).present_tense('imp', False), 'The passive imperative exists mostly in deponent verbs.') # pres imp act

        # imperfect
        self.assertEqual(RegularVerb(data[1][0]).imperfect_tense(True, True), ['monebam', 'monebas', 'monebat', 'monebamus', 'monebatis', 'monebant']) # impf ind act
        self.assertEqual(RegularVerb(data[1][0]).imperfect_tense(False, True), ['monerem', 'moneres', 'moneret', 'moneremus', 'moneretis', 'monerent']) # impf subj act
        self.assertEqual(RegularVerb(data[1][0]).imperfect_tense(True, False), ['monebar', 'monebaris', 'monebatur', 'monebamur', 'monebamini', 'monebantur']) # impf ind pass
        self.assertEqual(RegularVerb(data[1][0]).imperfect_tense(False, False), ['monerer', 'monereris', 'moneretur', 'moneremur', 'moneremini', 'monerentur']) # impf subj pass

        # future
        self.assertEqual(RegularVerb(data[1][0]).future_tense(True), ['monebo', 'monebis', 'monebit', 'monebimus', 'monebitis', 'monebunt']) # fut ind act
        self.assertEqual(RegularVerb(data[1][0]).future_tense(False), ['monebor', 'moneberis', 'monebitur', 'monebimur', 'monebimini', 'monebuntur']) # fut ind pass

        # 3rd conj

        # present
        self.assertEqual(RegularVerb(data[2][0]).present_tense('ind', True), ['rego', 'regis', 'regit', 'regimus', 'regitis', 'regunt']) # pres ind act
        self.assertEqual(RegularVerb(data[2][0]).present_tense('subj', True), ['regam', 'regas', 'regat', 'regamus', 'regatis', 'regant']) # pres subj act
        self.assertEqual(RegularVerb(data[2][0]).present_tense('ind', False), ['regor', 'regeris', 'regitur', 'regimur', 'regimini', 'reguntur']) # pres ind pass
        self.assertEqual(RegularVerb(data[2][0]).present_tense('subj', False), ['regar', 'regaris', 'regatur', 'regamur', 'regamini', 'regantur']) # pres subj pass
        self.assertEqual(RegularVerb(data[2][0]).present_tense('imp', True), ['rege', 'regite']) # pres imp act
        self.assertEqual(RegularVerb(data[2][0]).present_tense('imp', False), 'The passive imperative exists mostly in deponent verbs.') # pres imp act
        self.assertEqual(RegularVerb(['dico', 'dicere', 'dixi', 'dictus']).present_tense('imp', True), ['dic', 'dicite']) # pres imp act, irregular
        self.assertEqual(RegularVerb(['duco', 'ducere', 'duxi', 'ductus']).present_tense('imp', True), ['duc', 'ducite']) # pres imp act, irregular

        # imperfect
        self.assertEqual(RegularVerb(data[2][0]).imperfect_tense(True, True), ['regebam', 'regebas', 'regebat', 'regebamus', 'regebatis', 'regebant']) # impf ind act
        self.assertEqual(RegularVerb(data[2][0]).imperfect_tense(False, True), ['regerem', 'regeres', 'regeret', 'regeremus', 'regeretis', 'regerent']) # impf subj act
        self.assertEqual(RegularVerb(data[2][0]).imperfect_tense(True, False), ['regebar', 'regebaris', 'regebatur', 'regebamur', 'regebamini', 'regebantur']) # impf ind pass
        self.assertEqual(RegularVerb(data[2][0]).imperfect_tense(False, False), ['regerer', 'regereris', 'regeretur', 'regeremur', 'regeremini', 'regerentur']) # impf subj pass

        # future
        self.assertEqual(RegularVerb(data[2][0]).future_tense(True), ['regam', 'reges', 'reget', 'regemus', 'regetis', 'regent']) # fut ind act
        self.assertEqual(RegularVerb(data[2][0]).future_tense(False), ['regar', 'regeris', 'regetur', 'regemur', 'regemini', 'regentur']) # fut ind pass

        # 3rd io conj

        # present
        self.assertEqual(RegularVerb(data[3][0]).present_tense('ind', True), ['capio', 'capis', 'capit', 'capimus', 'capitis', 'capiunt']) # pres ind act
        self.assertEqual(RegularVerb(data[3][0]).present_tense('subj', True), ['capiam', 'capias', 'capiat', 'capiamus', 'capiatis', 'capiant']) # pres subj act
        self.assertEqual(RegularVerb(data[3][0]).present_tense('ind', False), ['capior', 'caperis', 'capitur', 'capimur', 'capimini', 'capiuntur']) # pres ind pass
        self.assertEqual(RegularVerb(data[3][0]).present_tense('subj', False), ['capiar', 'capiaris', 'capiatur', 'capiamur', 'capiamini', 'capiantur']) # pres subj pass
        self.assertEqual(RegularVerb(data[3][0]).present_tense('imp', True), ['cape', 'capite']) # pres imp act
        self.assertEqual(RegularVerb(data[3][0]).present_tense('imp', False), 'The passive imperative exists mostly in deponent verbs.') # pres imp act
        self.assertEqual(RegularVerb(['facio', 'facere', 'feci', 'factus']).present_tense('imp', True), ['fac', 'facite']) # pres imp act, irregular

        # imperfect
        self.assertEqual(RegularVerb(data[3][0]).imperfect_tense(True, True), ['capiebam', 'capiebas', 'capiebat', 'capiebamus', 'capiebatis', 'capiebant']) # impf ind act
        self.assertEqual(RegularVerb(data[3][0]).imperfect_tense(False, True), ['caperem', 'caperes', 'caperet', 'caperemus', 'caperetis', 'caperent']) # impf subj act
        self.assertEqual(RegularVerb(data[3][0]).imperfect_tense(True, False), ['capiebar', 'capiebaris', 'capiebatur', 'capiebamur', 'capiebamini', 'capiebantur']) # impf ind pass
        self.assertEqual(RegularVerb(data[3][0]).imperfect_tense(False, False), ['caperer', 'capereris', 'caperetur', 'caperemur', 'caperemini', 'caperentur']) # impf subj pass

        # future
        self.assertEqual(RegularVerb(data[3][0]).future_tense(True), ['capiam', 'capies', 'capiet', 'capiemus', 'capietis', 'capient']) # fut ind act
        self.assertEqual(RegularVerb(data[3][0]).future_tense(False), ['capiar', 'capieris', 'capietur', 'capiemur', 'capiemini', 'capientur']) # fut ind pass

        # 4th conj

        # present
        self.assertEqual(RegularVerb(data[4][0]).present_tense('ind', True), ['audio', 'audis', 'audit', 'audimus', 'auditis', 'audiunt']) # pres ind act
        self.assertEqual(RegularVerb(data[4][0]).present_tense('subj', True), ['audiam', 'audias', 'audiat', 'audiamus', 'audiatis', 'audiant']) # pres subj act
        self.assertEqual(RegularVerb(data[4][0]).present_tense('ind', False), ['audior', 'audiris', 'auditur', 'audimur', 'audimini', 'audiuntur']) # pres ind pass
        self.assertEqual(RegularVerb(data[4][0]).present_tense('subj', False), ['audiar', 'audiaris', 'audiatur', 'audiamur', 'audiamini', 'audiantur']) # pres subj pass
        self.assertEqual(RegularVerb(data[4][0]).present_tense('imp', True), ['audi', 'audite']) # pres imp act
        self.assertEqual(RegularVerb(data[4][0]).present_tense('imp', False), 'The passive imperative exists mostly in deponent verbs.') # pres imp act

        # imperfect
        self.assertEqual(RegularVerb(data[4][0]).imperfect_tense(True, True), ['audiebam', 'audiebas', 'audiebat', 'audiebamus', 'audiebatis', 'audiebant']) # impf ind act
        self.assertEqual(RegularVerb(data[4][0]).imperfect_tense(False, True), ['audirem', 'audires', 'audiret', 'audiremus', 'audiretis', 'audirent']) # impf subj act
        self.assertEqual(RegularVerb(data[4][0]).imperfect_tense(True, False), ['audiebar', 'audiebaris', 'audiebatur', 'audiebamur', 'audiebamini', 'audiebantur']) # impf ind pass
        self.assertEqual(RegularVerb(data[4][0]).imperfect_tense(False, False), ['audirer', 'audireris', 'audiretur', 'audiremur', 'audiremini', 'audirentur']) # impf subj pass

        # future
        self.assertEqual(RegularVerb(data[4][0]).future_tense(True), ['audiam', 'audies', 'audiet', 'audiemus', 'audietis', 'audient']) # fut ind act
        self.assertEqual(RegularVerb(data[4][0]).future_tense(False), ['audiar', 'audieris', 'audietur', 'audiemur', 'audiemini', 'audientur']) # fut ind pass

if __name__ == "__main__":
    unittest.main()
