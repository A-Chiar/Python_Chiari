"""Scenario: Un laboratorio scientifico registra le temperature ogni ora.
Obiettivo: Utilizzare numpy per calcolare la temperatura media, minima e massima registrata.
Dati: Un array numpy di temperature registrate in una giornata.
Compiti:
Crea una dataset di dati da almeno 24 posizioni
Calcola la temperatura media 
Trova la temperatura massima e minima.
Determina la temperatura più probabile 
per le prossime 4 posizioni rispetto a un aumento costante di 0,2 gradi al giorno ogni settimana. """

#importo la libreria
import numpy as np

#creo l'array delle temperature
T = np.random.randint(15,30,size = (24))

media_T = np.mean(T)
print("\n La media delle temperature è: ", media_T)
minima_T = np.min(T)
print("\n La minima delle temperature è: ", minima_T)
massima_T = np.max(T)
print("\n La minima delle temperature è:",massima_T)

aumento_T = 0.2
ultima_T = T[-1]
previsioni4ore=[]
for i in range(4):
    pre = ultima_T + aumento_T * (i + 1)
    pre = float(pre)
    previsioni4ore.append(pre)

print("\n Le previsioni per le prossime 4 ore sono: ", previsioni4ore)

