class RegularVerb:

    def __init__(self, parts: list):
        """
        Initializing the Verb class

                Parameters:
                        `parts` (list of str): list of principal parts
        """
        self.parts = parts

    def __conj_1(self) -> bool:
        """
        Check if 2nd principal part end in 'are'

                Returns: Boolean
        """
        return self.parts[1].endswith('are')

    def __conj_2(self) -> bool:
        """
        Check if 1st principal part ends with 'eo' and
        2nd principal part ends in 'ere'

                Returns: Boolean
        """
        return self.parts[0].endswith('eo') and self.parts[1].endswith('ere')

    def __conj_3(self) -> bool:
        """
        Check that 1st principal part doesn't end in 'eo' or 'io'
        and that 2nd principal part ends in 'ere'

                Returns: Boolean
        """
        return not self.parts[0].endswith('eo') and not self.parts[0].endswith('io') and self.parts[1].endswith('ere')

    def __conj_3io(self) -> bool:
        """
        Check if 1st principal part ends in 'io' and
        2nd principal part ends in 'ere'

                Returns: Boolean
        """
        return self.parts[0].endswith('io') and self.parts[1].endswith('ere')

    def __conj_4(self) -> bool:
        """
        Check if 2nd principal part ends in 'ire'

                Returns: Boolean
        """
        return self.parts[1].endswith('ire')

    def get_conjugation(self) -> str:
        """
        Conditionally loop through all the conjugation checks

                Returns:
                        `conjugation_type` (str)
        """
        return '1' if self.__conj_1() else ('2' if self.__conj_2() else ('3' if self.__conj_3() else ('3io' if self.__conj_3io() else '4')))

    def get_infinitives(self) -> list:
        """
        Return a max of 6 infinitives.

                Returns:
                        `infinitives` (list): infinitives in the order pres act, pres pass,
                            perf act, perf pass, fut act, fut pass
        """

        infinitives = []

        # pres act inf
        infinitives.append(self.parts[1])

        # pres pass inf
        if self.get_conjugation() in ['1', '2', '4']:
            infinitives.append(f'{self.parts[1][:-1]}i')
        else:
            infinitives.append(f'{self.parts[1][:-3]}i')

        # perf act inf

        # semi-deponent
        if ' ' in self.parts[2]:
            infinitives.append(None)
        # regular 3rd pp
        else:
            infinitives.append(f'{self.parts[2]}sse')

        # perf pass inf

        # semi-deponent
        if ' ' in self.parts[2] and self.parts[3] == None:
            infinitives.append(f'{self.parts[2][:-3]}esse')
        # no 4th pp
        elif not self.parts[3]:
            infinitives.append(None)
        # regular 4th pp
        else:
            infinitives.append(f'{self.parts[3]} esse')

        # fut act inf

        # semi-deponent
        if ' ' in self.parts[2] and not self.parts[3]:
            infinitives.append(f'{self.parts[2][:-5]}rus esse')
        # regular 3rd pp but no 4th pp
        elif not ' ' in self.parts[2] and not self.parts[3]:
            infinitives.append(None)
        # regular 4th pp
        else:
            infinitives.append(f'{self.parts[3][:-1]}rus esse')

        # fut pass inf

        # semi-deponent
        if ' ' in self.parts[2] and not self.parts[3]:
            infinitives.append(f'{self.parts[2][:-5]}m iri')
        # regular 3rd pp but no 4th pp
        elif not ' ' in self.parts[2] and not self.parts[3]:
            infinitives.append(None)
        # regular 4th pp
        else:
            infinitives.append(f'{self.parts[3][:-1]}m iri')

        return infinitives


    def get_participles(self):
        pass

    def present_tense(self, mood: str, is_active: bool) -> list:
        """
        Return present tense of a regular verb, based on:

                Parameters:
                        `mood` (str): 'ind'(idcative), 'subj'(unctive), or 'imp'(erative) mood
                        `is_active` (bool): active (or passive) voice

                Returns:
                        `conjugated_verbs` (list): conjugated verb list in the order 1st sg., 2nd sg.,
                            3rd sg., 1st pl., 2nd pl., 3rd pl.
        """

        # ending groups
        personal_endings_act = ['o','s','t','mus','tis','nt']
        personal_endings_pass = ['r', 'ris', 'tur', 'mur', 'mini', 'ntur']
        personal_endings_act_m = ['m', 's', 't', 'mus', 'tis', 'nt']

        conjugated_verbs = []

        # indicative mood
        if mood == 'ind':

            # 1st and 2nd conjugation
            if self.get_conjugation() in ['1', '2']:
                if is_active:
                    conjugated_verbs = [self.parts[0]] + [self.parts[1][:-2] + x for x in personal_endings_act[1:]]
                else:
                    conjugated_verbs = [self.parts[0] + personal_endings_pass[0]] + [self.parts[1][:-2] + x for x in personal_endings_pass[1:]]

            # 3rd conj
            elif self.get_conjugation() == '3':
                if is_active:
                    conjugated_verbs = [self.parts[0]] + [self.parts[1][:-3] + 'i' + x for x in personal_endings_act[1:5]] + [self.parts[1][:-3] + 'u' + personal_endings_act[5]]
                else:
                    conjugated_verbs = [self.parts[0] + personal_endings_pass[0]] + [self.parts[1][:-3] + 'e' + personal_endings_pass[1]] + [self.parts[1][:-3] + 'i' + x for x in personal_endings_pass[2:5]] + [self.parts[1][:-3] + 'u' + personal_endings_pass[5]]

            # 3rd io
            elif self.get_conjugation() == '3io':
                if is_active:
                    conjugated_verbs = [self.parts[0]] + [self.parts[1][:-3] + 'i' + x for x in personal_endings_act[1:5]] + [self.parts[1][:-3] + 'iu' + personal_endings_act[5]]
                else:
                    conjugated_verbs = [self.parts[0] + personal_endings_pass[0]] + [self.parts[1][:-3] + 'e' + personal_endings_pass[1]] + [self.parts[1][:-3] + 'i' + x for x in personal_endings_pass[2:5]] + [self.parts[1][:-3] + 'iu' + personal_endings_pass[5]]

            # 4th
            elif self.get_conjugation() == '4':
                if is_active:
                    conjugated_verbs = [self.parts[0]] + [self.parts[1][:-2] + x for x in personal_endings_act[1:5]] + [self.parts[1][:-2] + 'u' + personal_endings_act[5]]
                else:
                    conjugated_verbs = [self.parts[0] + personal_endings_pass[0]] + [self.parts[1][:-2] + x for x in personal_endings_pass[1:5]] + [self.parts[1][:-2] + 'u' + personal_endings_pass[5]]

        # subjunctive mood
        elif mood == 'subj':

            subjunctive = {
                "1": "e", # conjugation: present subjunctive vowel change
                "2": "ea",
                "3": "a",
                "3io": "ia",
                "4": "ia"
            }

            conjugated_verbs = [f'{self.parts[1][:-3]}{subjunctive[self.get_conjugation()]}' + x for x in (personal_endings_act_m if is_active else personal_endings_pass)]

        else: # imperative mood

            irregular_imperatives = [
                ['dico', 'dicere', 'dixi', 'dictus'],
                ['duco', 'ducere', 'duxi', 'ductus'],
                ['facio', 'facere', 'feci', 'factus']
                # ['fero', 'ferre', 'tuli', 'latus'] ---> include in irregular verbs
            ]

            # 1st, 2nd, 4th conj
            if self.get_conjugation() in ['1', '2', '4']:
                if is_active:
                    conjugated_verbs = [f'{self.parts[1][:-2]}', f'{self.parts[1][:-2]}te']
                else:
                    return 'The passive imperative exists mostly in deponent verbs.'

            # 3rd, 3rd io conj
            elif self.get_conjugation() in ['3', '3io']:
                if self.parts in irregular_imperatives:
                    if is_active:
                        conjugated_verbs = [f'{self.parts[1][:-3]}', f'{self.parts[1][:-3]}ite']
                    else:
                        return 'The passive imperative exists mostly in deponent verbs.'
                else:
                    if is_active:
                        conjugated_verbs = [f'{self.parts[1][:-2]}', f'{self.parts[1][:-3]}ite']
                    else:
                        return 'The passive imperative exists mostly in deponent verbs.'

        return conjugated_verbs

    def imperfect_tense(self, is_indicative: bool, is_active: bool) -> list:
        """
        Return the imperfect tense of a regular verb, based on:

                Parameters:
                        `is_indicative` (bool): indicative (or subjunctive) mood
                        `is_active` (bool): active (or passive) voice

                Returns:
                        `conjugated_verbs` (list): conjugated verb list in the order 1st sg., 2nd sg.,
                            3rd sg., 1st pl., 2nd pl., 3rd pl.
        """
        conjugated_verbs = []

        # ending groups
        personal_endings_act = ['m', 's', 't', 'mus', 'tis', 'nt']
        personal_endings_pass = ['r', 'ris', 'tur', 'mur', 'mini', 'ntur']

        # indicative mood
        if is_indicative:
            stem = f'{self.parts[1][:-2]}ba' if self.get_conjugation() in ['1', '2', '3'] else f'{self.parts[1][:-3]}ieba'
        # subjunctive mood
        else:
            stem = self.parts[1]

        conjugated_verbs = [stem + x for x in (personal_endings_act if is_active else personal_endings_pass)]

        return conjugated_verbs

    def future_tense(self, is_active: bool) -> list:
        """
        Return future tense of a regular verb, based on:

                Parameters:
                        `is_active` (bool): active (or passive) voice

                Returns:
                        `conjugated_verbs` (list): conjugated verb list in the order 1st sg., 2nd sg.,
                            3rd sg., 1st pl., 2nd pl., 3rd pl.
        """

        # ending groups
        personal_endings_act_1_2 = ['bo','bis','bit','bimus','bitis','bunt']
        personal_endings_pass_1_2 = ['bor', 'beris', 'bitur', 'bimur', 'bimini', 'buntur']

        personal_endings_act_3_4 = ['am', 'es', 'et', 'emus', 'etis', 'ent']
        personal_endings_pass_3_4 = ['ar', 'eris', 'etur', 'emur', 'emini', 'entur']

        conjugated_verbs = []

        # 1st and 2nd conjugation
        if self.get_conjugation() in ['1', '2']:
            if is_active:
                conjugated_verbs = [self.parts[1][:-2] + x for x in personal_endings_act_1_2]
            else:
                conjugated_verbs = [self.parts[1][:-2] + x for x in personal_endings_pass_1_2]

        # 3rd conj
        elif self.get_conjugation() == '3':
            if is_active:
                conjugated_verbs = [self.parts[1][:-3] + x for x in personal_endings_act_3_4]
            else:
                conjugated_verbs = [self.parts[1][:-3] + x for x in personal_endings_pass_3_4]

        # 3rd io and 4th
        else:
            if is_active:
                conjugated_verbs = [f'{self.parts[1][:-3]}i' + x for x in personal_endings_act_3_4]
            else:
                conjugated_verbs = [f'{self.parts[1][:-3]}i' + x for x in personal_endings_pass_3_4]

        return conjugated_verbs

    def perfect_tense(self, is_indicative: bool, is_active: bool) -> list:
        """
        Return perfect tense of a regular verb, based on:

                Parameters:
                        `is_indicative` (bool): indicative (or subjunctive) mood
                        `is_active` (bool): active (or passive) voice

                Returns:
                        `conjugated_verbs` (list): conjugated verb list in the order 1st sg., 2nd sg.,
                            3rd sg., 1st pl., 2nd pl., 3rd pl.
        """

        perf_act_ind_endings = ['i', 'isti', 'it', 'imus', 'istis', 'erunt/-ere']
        perf_act_subj_endings = ['erim', 'eris', 'erit', 'erimus', 'eritis', 'erint']
        sum_present_ind = ['sum', 'es', 'est', 'sumus', 'estis', 'sunt']
        sum_present_subj = ['sim', 'sis', 'sit', 'simus', 'sitis', 'sint']

        if is_indicative:
            if is_active:
                conjugated_verbs = [f'{self.parts[2][:-1]}' + x for x in perf_act_ind_endings]
            else: # perf ind pass
                if self.parts[3] == None:
                    return f'{self.parts[0]} has no fourth principal part.'
                else:
                    conjugated_verbs = [f'{self.parts[3]}, -a, -um ' + x for x in sum_present_ind[:3]] + [f'{self.parts[3][:-2]}i, -ae, -a ' + x for x in sum_present_ind[3:]]

        else: # subjunctive
            if is_active:
                conjugated_verbs = [f'{self.parts[2][:-1]}' + x for x in perf_act_subj_endings]
            else: # perf subj pass
                if self.parts[3] == None:
                    return f'{self.parts[0]} has no fourth principal part.'
                else:
                    conjugated_verbs = [f'{self.parts[3]}, -a, -um ' + x for x in sum_present_subj[:3]] + [f'{self.parts[3][:-2]}i, -ae, -a ' + x for x in sum_present_subj[3:]]

        return conjugated_verbs

    def pluperfect_tense(self, is_indicative: bool, is_active: bool) -> list:
        """
        Return pluperfect tense of a regular verb, based on:

                Parameters:
                        `is_indicative` (bool): indicative (or subjunctive) mood
                        `is_active` (bool): active (or passive) voice

                Returns:
                        `conjugated_verbs` (list): conjugated verb list in the order 1st sg., 2nd sg.,
                            3rd sg., 1st pl., 2nd pl., 3rd pl.
        """

        pluperf_act_ind_endings = ['eram', 'eras', 'erat', 'eramus', 'eratis', 'erant']
        pluperf_act_subj_endings = ['issem', 'isses', 'isset', 'issemus', 'issetis', 'issent']
        sum_impf_subj = ['essem', 'esses', 'esset', 'essemus', 'essetis', 'essent']

        if is_indicative:
            if is_active:
                conjugated_verbs = [f'{self.parts[2][:-1]}' + x for x in pluperf_act_ind_endings]
            else: # perf ind pass
                if not self.parts[3]:
                    return f'{self.parts[0]} has no fourth principal part.'
                else:
                    conjugated_verbs = [f'{self.parts[3]}, -a, -um ' + x for x in pluperf_act_ind_endings[:3]] + [f'{self.parts[3][:-2]}i, -ae, -a ' + x for x in pluperf_act_ind_endings[3:]]

        else: # subjunctive
            if is_active:
                conjugated_verbs = [f'{self.parts[2][:-1]}' + x for x in pluperf_act_subj_endings]
            else: # perf subj pass
                if self.parts[3] == None:
                    return f'{self.parts[0]} has no fourth principal part.'
                else:
                    conjugated_verbs = [f'{self.parts[3]}, -a, -um ' + x for x in sum_impf_subj[:3]] + [f'{self.parts[3][:-2]}i, -ae, -a ' + x for x in sum_impf_subj[3:]]

        return conjugated_verbs

    def future_perfect_tense(self, is_active: bool) -> list:
        """
        Return pluperfect tense of a regular verb, based on:

                Parameters:
                        `is_active` (bool): active (or passive) voice

                Returns:
                        `conjugated_verbs` (list): conjugated verb list in the order 1st sg., 2nd sg.,
                            3rd sg., 1st pl., 2nd pl., 3rd pl.
        """

        futperf_act_ind_endings = ['ero', 'eris', 'erit', 'erimus', 'eritis', 'erint']
        sum_fut = ['ero', 'eris', 'erit', 'erimus', 'eritis', 'erunt']

        if is_active:
            conjugated_verbs = [f'{self.parts[2][:-1]}' + x for x in futperf_act_ind_endings]
        else: # fut perf ind pass
            if self.parts[3] == None:
                return f'{self.parts[0]} has no fourth principal part.'
            else:
                conjugated_verbs = [f'{self.parts[3]}, -a, -um ' + x for x in sum_fut[:3]] + [f'{self.parts[3][:-2]}i, -ae, -a ' + x for x in sum_fut[3:]]

        return conjugated_verbs
