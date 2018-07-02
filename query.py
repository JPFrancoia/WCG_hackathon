#!/usr/bin/python
# coding: utf-8

import sqlite3

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
    notes = line["notes"]
    sentence = line["sentence"]
    variants[variant] = (notes, sentence)

# print(variants)

req = "SELECT * FROM patient0 WHERE "

l_variants = list(variants.keys())

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
# 
for line in results:
    variant = line["variant"]
    genotype = line["genotype"]
    # print(genotype)
    if variant in variants:
        print("{}: patient genotype is {}\nNotes: {}\nSentence: {}\n".format(variant, genotype, variants[variant][0], variants[variant][1]))


# bdd.commit()
c.close()
bdd.close()


if __name__ == "__main__":
    pass
