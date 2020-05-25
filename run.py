from core.classes import RegularVerb

print(RegularVerb(['do', 'dare', 'dedi', 'datus']).present_tense(False, True))
print(RegularVerb(['do', 'dare', 'dedi', 'datus']).imperfect_tense(True, True))
