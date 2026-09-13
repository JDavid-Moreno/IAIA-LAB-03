import pandas as pd

pokemon = pd.read_csv("data/pokemon.csv", index_col=0)

#1.
print(pokemon["Attack"])

#2.
print(pokemon[["Attack","Defense"]])