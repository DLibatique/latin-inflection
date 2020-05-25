from core.classes import RegularVerb
from core.data import *

print(RegularVerb(['do', 'dare', 'dedi', 'datus']).present_tense(True, True))
print(RegularVerb(['do', 'dare', 'dedi', 'datus']).present_tense(True, False))
print(RegularVerb(['do', 'dare', 'dedi', 'datus']).present_tense(False, True))
print(RegularVerb(['do', 'dare', 'dedi', 'datus']).present_tense(False, False))

print(RegularVerb(['do', 'dare', 'dedi', 'datus']).imperfect_tense(True, True))
print(RegularVerb(['do', 'dare', 'dedi', 'datus']).imperfect_tense(True, False))
print(RegularVerb(['do', 'dare', 'dedi', 'datus']).imperfect_tense(False, True))
print(RegularVerb(['do', 'dare', 'dedi', 'datus']).imperfect_tense(False, False))

for x in VERB_LIST:
    print(str(x) + ': ' + RegularVerb(x).get_conjugation())
