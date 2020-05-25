class RegularVerb:

    def __init__(self, parts: list):
        """
        Initializing the Verb class

                Parameters:
                        `parts` (list): list of principal parts
        """
        self.parts = parts

    def __conj_1(self) -> bool:
        """
        Check if any word in the list end in 'are'

                Returns: Boolean
        """
        return any(x.endswith('are') for x in self.parts)

    def __conj_2(self) -> bool:
        """
        Check if any word in the list has an ending 'eo' and
        any word in the list has an ending 'ere'

                Returns: Boolean
        """
        return any(x.endswith('eo') for x in self.parts) and any(x.endswith('ere') for x in self.parts)

    def __conj_3(self) -> bool:
        """
        Check if any word in the list has an ending 'ere' and
        no word in the list has an ending 'eo' and
        no word in the list has an ending 'io'

                Returns: Boolean
        """
        return not any(x.endswith('eo') for x in self.parts) and not any(x.endswith('io') for x in self.parts) and any(x.endswith('ere') for x in self.parts)

    def __conj_3io(self) -> bool:
        """
        Check if any word in the list has an ending 'io' and
        any word in the list has an ending 'ere'

                Returns: Boolean
        """
        return not any(x.endswith('eo') for x in self.parts) and any(x.endswith('ere') for x in self.parts)

    def __conj_4(self) -> bool:
        """
        Check if any word in the list has an ending 'ire'

                Returns: Boolean
        """
        return any(x.endswith('ire') for x in self.parts)

    def get_conjugation(self) -> str:
        """
        Conditionally loop through all the conjugation checks

                Returns:
                        `conjugation_type` (str)
        """
        return '1' if self.__conj_1() else ('2' if self.__conj_2() else ('3' if self.__conj_3() else ('3io' if self.__conj_3io() else '4')))

    def present_tense(self, mood: str, is_active: bool) -> list:
        """
        Return present tense of a regular verb, based on:

                Parameters:
                        `mood` (str): 'ind'(idcative), 'subj'(unctive), or 'imp'(erative) mood
                        `is_active` (bool): active (or passive) voice

                Returns:
                        `conjugated_verbs` (list): conjugated verb list
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
                        `conjugated_verbs` (list): conjugated verb list
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
                        `conjugated_verbs` (list): conjugated verb list
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
