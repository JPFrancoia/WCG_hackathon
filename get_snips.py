#!/usr/bin/python
# coding: utf-8

import sqlite3

# Create the db if it doesn't exist
bdd = sqlite3.connect("examples.sqlite")

bdd.row_factory = sqlite3.Row
c = bdd.cursor()

c.execute("SELECT * FROM drugs")

results = c.fetchall()

with open("snips.txt", "a") as f:
    for line in results:
        # Access each field by name
        variant = line["Variant"]
        print(variant)
        f.write(variant)
        f.write("\n")


c.close()
bdd.close()


if __name__ == "__main__":
    pass
