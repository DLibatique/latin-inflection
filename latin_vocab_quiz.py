do = ['do', 'dare', 'dedi', 'datus']
capio = ['capio', 'capere', 'cepi', 'captus']
audio = ['audio', 'audire', 'audivi', 'auditus']
rego = ['rego', 'regere', 'rexi', 'rectus']


def pres_conj(verb, conj, passive=False):

    # ending groups
    pres_act = ['o','s','t','mus','tis','nt']
    pres_pass = ['r', 'ris', 'tur', 'mur', 'mini', 'ntur']

    # 1st and 2nd conjugation
    if conj == '1' or conj == '2':
        if passive == False:
            conjugatedVerbs = [verb[0]] + [verb[1][:-2] + x for x in pres_act[1:]]
        elif passive == True:
            conjugatedVerbs = [verb[0] + pres_pass[0]] + [verb[1][:-2] + x for x in pres_pass[1:]]

    # 3rd conj
    elif conj == '3':
        if passive == False:
            conjugatedVerbs = [verb[0]] + [verb[1][:-3] + 'i' + x for x in pres_act[1:5]] + [verb[1][:-3] + 'u' + pres_act[5]]
        elif passive == True:
            conjugatedVerbs = [verb[0] + pres_pass[0]] + [verb[1][:-3] + 'e' + pres_pass[1]] + [verb[1][:-3] + 'i' + x for x in pres_pass[2:5]] + [verb[1][:-3] + 'u' + pres_pass[5]]

    # 3rd io
    elif conj == '3io':
            if passive == False:
                conjugatedVerbs = [verb[0]] + [verb[1][:-3] + 'i' + x for x in pres_act[1:5]] + [verb[1][:-3] + 'iu' + pres_act[5]]
            elif passive == True:
                conjugatedVerbs = [verb[0] + pres_pass[0]] + [verb[1][:-3] + 'e' + pres_pass[1]] + [verb[1][:-3] + 'i' + x for x in pres_pass[2:5]] + [verb[1][:-3] + 'iu' + pres_pass[5]]

    # 4th
    elif conj == '4':
        if passive == False:
            conjugatedVerbs = [verb[0]] + [verb[1][:-2] + x for x in pres_act[1:5]] + [verb[1][:-2] + 'u' + pres_act[5]]
        elif passive == True:
            conjugatedVerbs = [verb[0] + pres_pass[0]] + [verb[1][:-2] + x for x in pres_pass[1:5]] + [verb[1][:-2] + 'u' + pres_pass[5]]

    return conjugatedVerbs

def impf_conj(verb, conj, passive=False):

    # ending groups
    impf_act = ['bam','bas','bat','bamus','batis','bant']
    impf_pass = ['bar', 'baris', 'batur', 'bamur', 'bamini', 'bantur']

    # 1st 2nd or 3rd conj
    if conj == '1' or conj=='2' or conj=='3':
        if passive == False:
            conjugatedVerbs = [verb[1][:-2] + x for x in impf_act]
        elif passive == True:
            conjugatedVerbs = [verb[1][:-2] + x for x in impf_pass]

    # 3rd io or 4th
    elif conj == '3io' or conj=='4':
        if passive == False:
            conjugatedVerbs = [verb[1][:-3] + 'ie' + x for x in impf_act]
        elif passive == True:
            conjugatedVerbs = [verb[1][:-3] + 'ie' + x for x in impf_pass]

    return conjugatedVerbs

# print(pres_act_conj(do,pres_act))
# print(pres_pass_conj(do,pres_pass))
# print(impf_fut_conj(do,impf_act))
# print(impf_fut_conj(do,fut_act_1_2))

    # fut_act = ['bo','bis','bit','bimus','bitis','bunt']
    # fut_pass = ['bor', 'beris', 'bitur', 'bimur', 'bimini', 'buntur']
    #         else:
    #             conjugatedVerbs = [verb[1][:-2] + x for x in fut_pass]
    #                     elif passive==False and impf==False:
    #                         conjugatedVerbs = [verb[1][:-2] + x for x in fut_act]

print(impf_conj(do,'2'))
print(impf_conj(capio,'3io',True))
print(impf_conj(capio,'3io'))
print(pres_conj(audio,'4'))
print(pres_conj(capio,'3io',True))
print(pres_conj(rego,'3',True))
print(pres_conj(rego,'3'))
print(impf_conj(audio,'4',True))
