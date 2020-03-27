from conjugation import pres_conj, impf_conj
from data import do, capio, audio, rego


print(pres_conj(audio,'4'))
print(pres_conj(capio,'3io',True))
print(pres_conj(rego,'3',True))
print(pres_conj(rego,'3'))
print(impf_conj(do,'2'))
print(impf_conj(capio,'3io',True))
print(impf_conj(capio,'3io'))
print(impf_conj(audio,'4',True))
