#carico le librerie
import numpy as np
import pandas as pd

#uso le funzioni di numpy per generarmi i vari array che poi caricherò nel dataframe, passando per un dizionario
date = np.arange('2024-06', '2024-07', dtype='datetime64[D]')
print(date)

vendite = np.random.randint(0,1000,size= (30))
print(vendite)
ore_lavorative = np.random.randint(1,8,size= (30))
print(ore_lavorative)

#creo un dizionario
data = {
    'Data': date,
    'Vendite': vendite,
    'Ore Lavorative': ore_lavorative
}
#trasformo il dizionario in dataframe
df = pd.DataFrame(data)
print(df)

media_vendite =  df.groupby(['Data','Ore Lavorative'])['Vendite'].mean()
print(media_vendite)

#raggruppo i valori per definirne le relazioni 
datamax = df.groupby('Data')['Vendite'].sum().idxmax()
massima_vendite = df.groupby('Data')['Vendite'].sum().max()
datamin = df.groupby('Data')['Vendite'].sum().idxmin()
minima_vendite =df.groupby('Data')['Vendite'].sum().min()
#effettuo le stampe
print(f"Il giorno con la massima delle vendite è stato {datamax}, con un valore pari a {massima_vendite}")
print(f"Il giorno con la massima delle vendite è stato {datamin}, con un valore pari a {minima_vendite}")

#salvo il dataframe su un file csv
media_vendite.to_csv("Esercizio_integrato.csv")
