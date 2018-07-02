#!/usr/bin/python
# coding: utf-8

import sqlite3

# Create the db if it doesn't exist
bdd = sqlite3.connect("clean.sqlite")

bdd.row_factory = sqlite3.Row
c = bdd.cursor()

c.execute(
    "CREATE TABLE IF NOT EXISTS patient0 (id INTEGER PRIMARY KEY AUTOINCREMENT, variant TEXT, genotype TEXT)"
)

# c.execute("SELECT * FROM drugs")

# results = c.fetchall()

with open("build.tped", "r") as f:
    lines = f.readlines()


for l in lines:
    l = l.strip()
    variant = l.split()[1]
    genotype = l.split()[-2:]
    genotype = "".join(genotype)

    c.execute(
        "INSERT INTO patient0 (variant, genotype) VALUES (?, ?)", (variant, genotype)
    )


bdd.commit()
c.close()
bdd.close()


if __name__ == "__main__":
    pass
