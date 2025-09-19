# ...existing code...
s = "ciao ciao ciao"
sub = "ciao"

first = s.find(sub)
# seconda occorrenza consentendo sovrapposizioni
second_overlap = s.find(sub, first + 1) if first != -1 and sub != "" else -1
# seconda occorrenza NON sovrapposta (salta la lunghezza della sottostringa)
second_nonoverlap = s.find(sub, first + len(sub)) if first != -1 and sub != "" else -1

print(first)               # indice prima occorrenza
print(second_overlap)      # indice seconda occorrenza (consentendo sovrapposizioni)
print(second_nonoverlap)   # indice seconda occorrenza (non sovrapposta)
# ...existing code...