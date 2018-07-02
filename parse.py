#!/usr/bin/python
# coding: utf-8

import numpy as np
import pandas as pd
import sqlite3

# Create the db if it doesn't exist
bdd = sqlite3.connect("examples.sqlite")

bdd.row_factory = sqlite3.Row
c = bdd.cursor()


df = pd.read_csv("var_drug_ann.tsv", sep="\t", error_bad_lines=False)
print(df)
df.to_sql("drugs", bdd)

c.close()
bdd.close()

if __name__ == "__main__":
    pass
