from core.classes import RegularVerb
from core.data import *
from random import randrange as rr

print(RegularVerb(VERB_LIST[rr(0,249)]).present_tense('ind', True)) # pres ind act
print(RegularVerb(VERB_LIST[rr(0,249)]).present_tense('subj', True)) # pres subj act
print(RegularVerb(VERB_LIST[rr(0,249)]).present_tense('ind', False)) # pres ind pass
print(RegularVerb(VERB_LIST[rr(0,249)]).present_tense('subj', False)) # pres subj pass
print(RegularVerb(VERB_LIST[rr(0,249)]).present_tense('imp', True)) # pres imp act
print(RegularVerb(VERB_LIST[rr(0,249)]).present_tense('imp', False)) # pres imp act

# imperfect
print(RegularVerb(VERB_LIST[rr(0,249)]).imperfect_tense(True, True)) # impf ind act
print(RegularVerb(VERB_LIST[rr(0,249)]).imperfect_tense(False, True)) # impf subj act
print(RegularVerb(VERB_LIST[rr(0,249)]).imperfect_tense(True, False)) # impf ind pass
print(RegularVerb(VERB_LIST[rr(0,249)]).imperfect_tense(False, False)) # impf subj pass

# future
print(RegularVerb(VERB_LIST[rr(0,249)]).future_tense(True)) # fut ind act
print(RegularVerb(VERB_LIST[rr(0,249)]).future_tense(False)) # fut ind pass

# perfect
print(RegularVerb(VERB_LIST[rr(0,249)]).perfect_tense(True, True)) # perf ind act
print(RegularVerb(VERB_LIST[rr(0,249)]).perfect_tense(False, True)) # perf subj act
print(RegularVerb(VERB_LIST[rr(0,249)]).perfect_tense(True, False)) # perf ind pass
print(RegularVerb(VERB_LIST[rr(0,249)]).perfect_tense(False, False)) # perf subj pass

# pluperfect
print(RegularVerb(VERB_LIST[rr(0,249)]).pluperfect_tense(True, True)) # pluperf ind act
print(RegularVerb(VERB_LIST[rr(0,249)]).pluperfect_tense(False, True)) # pluperf subj act
print(RegularVerb(VERB_LIST[rr(0,249)]).pluperfect_tense(True, False)) # pluperf ind pass
print(RegularVerb(VERB_LIST[rr(0,249)]).pluperfect_tense(False, False)) # pluperf subj pass

# future perfect
print(RegularVerb(VERB_LIST[rr(0,249)]).future_perfect_tense(True)) # fut perf ind act
print(RegularVerb(VERB_LIST[rr(0,249)]).future_perfect_tense(False)) # fut perf pass act
