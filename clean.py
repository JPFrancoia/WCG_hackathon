#!/usr/bin/python
# coding: utf-8

import sqlite3

# Create the db if it doesn't exist
bdd = sqlite3.connect("examples.sqlite")
bdd_out = sqlite3.connect("clean.sqlite")

bdd.row_factory = sqlite3.Row
c = bdd.cursor()

bdd_out.row_factory = sqlite3.Row
c2 = bdd_out.cursor()

# Create a table in the db
c2.execute(
    "CREATE TABLE IF NOT EXISTS drugs \
    (id INTEGER PRIMARY KEY AUTOINCREMENT, annotation INTEGER, variant TEXT,\
    gene TEXT, chemical TEXT, lit_id TEXT, pheno_cat TEXT, significance TEXT,\
    notes TEXT, sentence TEXT, study_para TEXT, alleles TEXT, chromosome TEXT)"
)

c.execute("SELECT * FROM drugs")

# Fetch all rows returned
results = c.fetchall()

# Access the rows returned
for line in results:
# Access each field by name
    annotation = line['Annotation ID']
    variant = line['Variant']
    gene = line['Gene']
    chemical = line['Chemical']
    lit_id = line['Literature Id']
    pheno_cat = line['Phenotype Category']
    significance = line['Significance']
    notes = line['Notes']
    sentence = line['Sentence']
    study_para = line['StudyParameters']
    alleles = line['Alleles']
    chromosome = line['Chromosome']

    if not variant.startswith('rs'):
        continue

    if gene is not None:
        gene = gene.split(" (PA")[0]
    chemical = chemical.split(" (PA")[0]

# print(variant, chemical)

# Delete stuff, use tuple for parameters. If one element, don't forget the comma
    c2.execute("INSERT INTO drugs (annotation, variant, gene, chemical, lit_id, pheno_cat, significance, notes, sentence, study_para, alleles, chromosome) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (annotation, variant, gene, chemical, lit_id, pheno_cat, significance, notes, sentence, study_para, alleles, chromosome))


# bdd.commit()
c.close()
bdd.close()

bdd_out.commit()
c2.close()
bdd_out.close()


if __name__ == "__main__":
    pass
