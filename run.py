from core.classes import RegularVerb
from core.data import *

print(RegularVerb(VERB_LIST[0]).present_tense('ind', True))
print(RegularVerb(VERB_LIST[15]).present_tense('subj', False))
print(RegularVerb(VERB_LIST[33]).imperfect_tense(True, False))
print(RegularVerb(VERB_LIST[81]).imperfect_tense(False, True))
print(RegularVerb(VERB_LIST[100]).future_tense(False))
