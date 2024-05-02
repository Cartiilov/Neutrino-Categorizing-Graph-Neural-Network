Wczytanie pliku:


import pandas as pd

df = pd.read_hdf("file.h5", "y")

print(df.head())



W przyrodzie występują trzy neutrina: elektronowe, mionowe i taonowe.
Mogą one oddziaływać na różne sposoby. Jednakże neutrina to cząstki, które
oddziałują bardzo niechętnie. Dlatego mamy bardzo mało danych. 

Osiem klas w zależności od typu neutrina i sposobu w jaki oddziałuje.
Dziewięć wielkości x1,...,x9 charakteryzujących dane neutrino.


Należy zbudować model, który "powie" do której klasy neutrinowej należy przypadek. 
