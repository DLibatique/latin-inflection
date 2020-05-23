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
        else:
            conj = '4'

        return conj

    def pres_conj(self, passive=False):

        conjugatedVerbs = []

        # ending groups
        pres_act = ['o','s','t','mus','tis','nt']
        pres_pass = ['r', 'ris', 'tur', 'mur', 'mini', 'ntur']

        # 1st and 2nd conjugation
        if self.get_conj() in ['1', '2']:
            if not passive:
                conjugatedVerbs = [self.parts[0]] + [self.parts[1][:-2] + x for x in pres_act[1:]]
            else:
                conjugatedVerbs = [self.parts[0] + pres_pass[0]] + [self.parts[1][:-2] + x for x in pres_pass[1:]]

        # 3rd conj
        elif self.get_conj() == '3':
            if passive == False:
                conjugatedVerbs = [self.parts[0]] + [self.parts[1][:-3] + 'i' + x for x in pres_act[1:5]] + [self.parts[1][:-3] + 'u' + pres_act[5]]
            elif passive == True:
                conjugatedVerbs = [self.parts[0] + pres_pass[0]] + [self.parts[1][:-3] + 'e' + pres_pass[1]] + [self.parts[1][:-3] + 'i' + x for x in pres_pass[2:5]] + [self.parts[1][:-3] + 'u' + pres_pass[5]]

        # 3rd io
        elif self.get_conj() == '3io':
                if passive == False:
                    conjugatedVerbs = [self.parts[0]] + [self.parts[1][:-3] + 'i' + x for x in pres_act[1:5]] + [self.parts[1][:-3] + 'iu' + pres_act[5]]
                elif passive == True:
                    conjugatedVerbs = [self.parts[0] + pres_pass[0]] + [self.parts[1][:-3] + 'e' + pres_pass[1]] + [self.parts[1][:-3] + 'i' + x for x in pres_pass[2:5]] + [self.parts[1][:-3] + 'iu' + pres_pass[5]]

        # 4th
        elif self.get_conj() == '4':
            if passive == False:
                conjugatedVerbs = [self.parts[0]] + [self.parts[1][:-2] + x for x in pres_act[1:5]] + [self.parts[1][:-2] + 'u' + pres_act[5]]
            elif passive == True:
                conjugatedVerbs = [self.parts[0] + pres_pass[0]] + [self.parts[1][:-2] + x for x in pres_pass[1:5]] + [self.parts[1][:-2] + 'u' + pres_pass[5]]

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
