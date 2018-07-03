#!/usr/bin/python
# coding: utf-8

import sqlite3

separator = "-----------------------------------------------"

# DRUGS = "efavirenz"
# DRUGS = "clozapine"
DRUGS = "simvastatin"

# Create the db if it doesn't exist
bdd = sqlite3.connect("clean.sqlite")

bdd.row_factory = sqlite3.Row
c = bdd.cursor()

c.execute("SELECT * FROM drugs WHERE chemical like \"%{}%\"".format(DRUGS))

results = c.fetchall()

variants = dict()

for line in results:
    variant = line["variant"]
    lit_id = line["lit_id"]
    notes = line["notes"]
    sentence = line["sentence"]
    variants[variant] = (lit_id, notes, sentence)


# print(variants)

for key, value in variants.items():
    c.execute("SELECT * FROM abstracts WHERE lit_id=?", (value[0],))
    results = c.fetchone()[2]
    print(results)

    variants[key] = (value[0], value[1], value[2], results)
    print(variants[key])

l_variants = list(variants.keys())
req = "SELECT * FROM patient0 WHERE "

# Building the query
for each_variant in l_variants:

    if each_variant is l_variants[0]:
        req = req + "variant=\"{}\"".format(each_variant)
    elif each_variant is not l_variants[-1]:
        req = req + " OR variant=\"{}\"".format(each_variant)
    else:
        req = req + " OR variant=\"{}\"".format(each_variant)

c.execute(req)

results = c.fetchall()

# variants = dict()
for line in results:
    variant = line["variant"]
    genotype = line["genotype"]
    # print(genotype)
    if variant in variants:
        print("{}: patient genotype is {}\nNotes: {}\nSentence: {}\n\nMore info: {}\n{}".
              format(variant, genotype, variants[variant][1], variants[variant][2], variants[variant][3], separator))


# bdd.commit()
c.close()
bdd.close()


if __name__ == "__main__":
    pass
