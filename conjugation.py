def pres_conj(verb, conj, passive=False):

    # ending groups
    pres_act = ['o','s','t','mus','tis','nt']
    pres_pass = ['r', 'ris', 'tur', 'mur', 'mini', 'ntur']

    # 1st and 2nd conjugation
    if conj in ['1', '2']: # if conj == '1' or conj == '2':
        if not passive: # if passive == False:
            conjugated_verbs = [verb[0]] + [verb[1][:-2] + x for x in pres_act[1:]]
        else: # elif passive == True:
            conjugated_verbs = [verb[0] + pres_pass[0]] + [verb[1][:-2] + x for x in pres_pass[1:]]

    # 3rd conj
    elif conj == '3':
        if not passive: # if passive == False:
            conjugated_verbs = [verb[0]] + [verb[1][:-3] + 'i' + x for x in pres_act[1:5]] + [verb[1][:-3] + 'u' + pres_act[5]]
        else: # elif passive == True:
            conjugated_verbs = [verb[0] + pres_pass[0]] + [verb[1][:-3] + 'e' + pres_pass[1]] + [verb[1][:-3] + 'i' + x for x in pres_pass[2:5]] + [verb[1][:-3] + 'u' + pres_pass[5]]

    # 3rd io
    elif conj == '3io':
        if not passive: # if passive == False:
            conjugated_verbs = [verb[0]] + [verb[1][:-3] + 'i' + x for x in pres_act[1:5]] + [verb[1][:-3] + 'iu' + pres_act[5]]
        else: # elif passive == True:
            conjugated_verbs = [verb[0] + pres_pass[0]] + [verb[1][:-3] + 'e' + pres_pass[1]] + [verb[1][:-3] + 'i' + x for x in pres_pass[2:5]] + [verb[1][:-3] + 'iu' + pres_pass[5]]

    # 4th
    elif conj == '4':
        if not passive: # if passive == False:
            conjugated_verbs = [verb[0]] + [verb[1][:-2] + x for x in pres_act[1:5]] + [verb[1][:-2] + 'u' + pres_act[5]]
        else: # elif passive == True:
            conjugated_verbs = [verb[0] + pres_pass[0]] + [verb[1][:-2] + x for x in pres_pass[1:5]] + [verb[1][:-2] + 'u' + pres_pass[5]]

    return conjugated_verbs

def impf_conj(verb, conj, passive=False):

    # ending groups
    impf_act = ['bam','bas','bat','bamus','batis','bant']
    impf_pass = ['bar', 'baris', 'batur', 'bamur', 'bamini', 'bantur']

    # 1st 2nd or 3rd conj
    if conj in ['1', '2', '3']: # if conj == '1' or conj=='2' or conj=='3':
        # if not passive: # if passive == False:
        #     conjugated_verbs = [verb[1][:-2] + x for x in impf_act]
        # else: # elif passive == True:
        #     conjugated_verbs = [verb[1][:-2] + x for x in impf_pass]
        return [
            (verb[1][:-2] + x) for x in (impf_pass if passive else impf_act)
        ]

    # 3rd io or 4th
    if conj in ['3io', '4']: # elif conj == '3io' or conj=='4':
        # if not passive: # if passive == False:
        #     conjugated_verbs = [verb[1][:-3] + 'ie' + x for x in impf_act]
        # else: # elif passive == True:
        #     conjugated_verbs = [verb[1][:-3] + 'ie' + x for x in impf_pass]
        return [
            (verb[1][:-3] + 'ie' + x) for x in (impf_pass if passive else impf_act)
        ]

    # return conjugated_verbs
