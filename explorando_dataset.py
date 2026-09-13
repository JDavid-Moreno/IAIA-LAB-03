import pandas as pd

#1.
pokemon = pd.read_csv("data/pokemon.csv", index_col=0)

#2.
print(pokemon.head())
print(pokemon.tail())

#3.
print(pokemon.info())

#4.
print(pokemon.describe())

#5.
print(pokemon.shape)

print(pokemon.dtypes)

