from data import *

class RegularVerb():

    # initialize with principal parts
    def __init__(self, parts):
        self.parts = parts # should be list

    def get_conj(self):

        conj = ''

        # infinitive ends in -are = 1st conj
        if self.parts[1].endswith('are'):
            conj = '1'

        # 1st pp ends in -eo and 2nd ends in -ere = 2nd conj
        elif self.parts[0].endswith('eo') and self.parts[1].endswith('ere'):
            conj = '2'

        # 1st pp ends in neither -io nor -eo and 2nd ends in -ere = 3rd
        elif not self.parts[0].endswith('eo') and not self.parts[0].endswith('io') and self.parts[1].endswith('ere'):
            conj = '3'

        # 1st pp ends in -io and 2nd ends in -ere = 3rd io
        elif self.parts[0].endswith('io') and self.parts[1].endswith('ere'):
            conj = '3io'

        # no other conjugation markers met = 4th
        elif self.parts[1].endswith('ire'):
            conj = '4'

        return conj

    # conjugate in the present tense, active or passive voice
    def pres_conj(self, passive=False):

        conjugatedVerbs = []

        # ending groups
        pers_endings_act = ['o','s','t','mus','tis','nt']
        pers_endings_pass = ['r', 'ris', 'tur', 'mur', 'mini', 'ntur']
        pers_endings_act_m = ['m', 's', 't', 'mus', 'tis', 'nt']

        # 1st and 2nd conjugation
        if self.get_conj() in ['1', '2']:
            if not passive:
                conjugatedVerbs = [self.parts[0]] + [self.parts[1][:-2] + x for x in pers_endings_act[1:]]
            else:
                conjugatedVerbs = [self.parts[0] + pers_endings_pass[0]] + [self.parts[1][:-2] + x for x in pers_endings_pass[1:]]

        # 3rd conj
        elif self.get_conj() == '3':
            if not passive:
                conjugatedVerbs = [self.parts[0]] + [self.parts[1][:-3] + 'i' + x for x in pers_endings_act[1:5]] + [self.parts[1][:-3] + 'u' + pers_endings_act[5]]
            else:
                conjugatedVerbs = [self.parts[0] + pers_endings_pass[0]] + [self.parts[1][:-3] + 'e' + pers_endings_pass[1]] + [self.parts[1][:-3] + 'i' + x for x in pers_endings_pass[2:5]] + [self.parts[1][:-3] + 'u' + pers_endings_pass[5]]

        # 3rd io
        elif self.get_conj() == '3io':
            if not passive:
                conjugatedVerbs = [self.parts[0]] + [self.parts[1][:-3] + 'i' + x for x in pers_endings_act[1:5]] + [self.parts[1][:-3] + 'iu' + pers_endings_act[5]]
            else:
                conjugatedVerbs = [self.parts[0] + pers_endings_pass[0]] + [self.parts[1][:-3] + 'e' + pers_endings_pass[1]] + [self.parts[1][:-3] + 'i' + x for x in pers_endings_pass[2:5]] + [self.parts[1][:-3] + 'iu' + pers_endings_pass[5]]

        # 4th
        elif self.get_conj() == '4':
            if passive == False:
                conjugatedVerbs = [self.parts[0]] + [self.parts[1][:-2] + x for x in pers_endings_act[1:5]] + [self.parts[1][:-2] + 'u' + pers_endings_act[5]]
            elif passive == True:
                conjugatedVerbs = [self.parts[0] + pers_endings_pass[0]] + [self.parts[1][:-2] + x for x in pers_endings_pass[1:5]] + [self.parts[1][:-2] + 'u' + pers_endings_pass[5]]

        return conjugatedVerbs



'''
1st: 2nd principal part ends in -are
2nd: 1st principal part ends in -eo, 2nd principal part ends in -ere
3rd: 1st principal part ends in -o, 2nd principal part ends in -ere
3rd io: 1st principal part ends in -io, 2nd principal part ends in -ere
4th: 2nd principal part ends in -ire
'''

laudo = ['laudo', 'laudare', 'laudavi', 'laudatus']
moneo = ['moneo', 'monere', 'monui', 'monitus']
rego = ['rego', 'regere', 'rexi', 'rectus']
capio = ['capio', 'capere', 'cepi', 'captus']
audio = ['audio', 'audire', 'audivi', 'auditus']
timeo = ['timeo', 'timere', 'timui']

verbs = [laudo, moneo, rego, capio, audio, timeo]

for v in verbs:
    v = RegularVerb(v)
    print(v.get_conj())
    print(v.pres_conj())
    print(v.pres_conj(True))

dcc_verbs = [accedo, accido, accipio, addo, adduco, adhibeo, advenio, adverto, afficio, agito, ago, alo, amitto, amo, aperio, appareo, appello, ardeo, ascendo, aspicio, audeo, audio, augeo, cado, caedo, cano, capio, careo, caveo, cedo, celebro, censeo, cerno, certo, cingo, claudo, cogito, cognosco, cogo, colligo, colo, committo, comparo, compono, concedo, condo, conficio, consisto, constituo, consto, consulo, consumo, contemno, contineo, contingo, convenio, converto, corrumpo, credo, creo, cresco, cupio, curo, curro, damno, debeo, decerno, deduco, defendo, deficio, descendo, desero, desidero, desino, dico, diligo, dimitto, discedo, disco, divido, do, doceo, doleo, dono, dormio, dubito, duco, edico, edo, educo, efficio, effundo, eligo, eripio, erro, excipio, exerceo, exigo, existimo, exspecto, facio, fallo, fingo, fleo, fluo, frango, fugio, fugo, fundo, gaudeo, gero, gigno, habeo, iaceo, iacio, impero, impleo, impono, incido, incipio, indico, instituo, intellego, intendo, interficio, interrogo, intro, invenio, iubeo, iudico, iungo, iuro, iuvo, laboro, laedo, lateo, laudo, lego, maneo, mereo, metuo, misceo, mitto, moneo, moveo, muto, narro, nego, nescio, noceo, nosco, occido, occupo, occurro, opto, oro, ostendo, parco, pareo, pario, paro, pateo, pecco, pello, pendo, perdo, pergo, permitto, pertineo, pervenio, peto, placeo, pono, porto, posco, praebeo, praecipio, praesto, premo, probo, procedo, prodo, prohibeo, promitto, propero, propono, pugno, puto, quaero, quiesco, rapio, recedo, recipio, reddo, rego, relinquo, reperio, repeto, respicio, respondeo, retineo, reverto, revoco, rideo, rogo, rumpo, scio, scribo, sedeo, sentio, servio, servo, sino, soleo, solvo, sono, spargo, specto, spero, statuo, sto, studeo, sumo, supero, surgo, suscipio, sustineo, taceo, tango, tego, tempto, tendo, teneo, terreo, timeo, trado, traho, turbo, vaco, valeo, veho, venio, verto, veto, video, vinco, vito, vivo, voco]

for d in dcc_verbs:
    d = RegularVerb(d)
    print(d.pres_conj())
