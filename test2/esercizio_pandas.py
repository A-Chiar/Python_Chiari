"""Scenario: Una catena di ristoranti vuole analizzare le vendite giornaliere in diverse filiali.
Obiettivo: Utilizzare pandas per calcolare le vendite medie giornaliere per ogni filiale.
Dati: Il dataset contiene colonne "Data", "Filiale" e "Vendite".

Compiti:
Genera i dati da un file CSV.
Utilizza groupby() per raggruppare i dati per "Data" e "Filiale".
Calcola la media delle vendite giornaliere per filiale
Calcola quale filiale ha venduto di più
Salva tutti i valori e i risultati su un nuovo file(ES: csv)."""
#importa la libreria
import pandas as pd

#carico il file csv
df = pd.read_csv('esercizio_pandas.csv')

#effettuo i groupby per definire le relazioni tra i dati
raggruppaDataFiliale = df.groupby('Data')['Filiale'].sum()
print("\n i dati raggruppati per data e filiale sono: ", raggruppaDataFiliale)
media_vendite = df.groupby('Filiale')['Vendite'].mean()
print("\n La media delle vendite giornaliere per filiale è stata: ", media_vendite)

nome_filiale = df.groupby('Filiale')['Vendite'].sum().idxmax()
massimo_vendite= df.groupby('Filiale')['Vendite'].sum().max()
print(f"\nLa città che ha venduto di più è stata {nome_filiale}, con un totale di {massimo_vendite} vendite")

#salvo il dataframe su un file csv
media_vendite.to_csv("MediaVendite.csv", index=False)
