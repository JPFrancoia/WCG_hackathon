#!/usr/bin/python
# coding: utf-8

import requests
import sqlite3
from bs4 import BeautifulSoup, SoupStrainer


BASE = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id="

# Create the db if it doesn't exist
bdd = sqlite3.connect("clean.sqlite")

bdd.row_factory = sqlite3.Row
c = bdd.cursor()


c.execute(
    "CREATE TABLE IF NOT EXISTS abstracts (id INTEGER PRIMARY KEY AUTOINCREMENT, lit_id INTEGER, abstract TEXT)"
)


# c.execute("SELECT * FROM drugs")

# results = c.fetchall()

# # variants = dict()
# list_lit_id = list()

# for line in results:
    # lit_id = line["lit_id"]
    # list_lit_id.append(lit_id)
    # # notes = line["notes"]
    # # sentence = line["sentence"]
    # # variants[variant] = (notes, sentence)

# list_lit_id = list(set(list_lit_id))

# STEP = 20

# for i in range(0, 103):
    # BASE = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id="

    # for each_id in list_lit_id[i * STEP: i * STEP + STEP]:

        # if each_id is not list_lit_id[-1]:
            # BASE = BASE + str(each_id) + ","
        # else:
            # BASE = BASE + str(each_id)

    # print(BASE)
    # print("\n")

    # req = requests.get(BASE)

    # with open("all_abstracts_{}.xml".format(i), "w") as f:
        # f.write(req.text)

for i in range(0, 103):
    with open("abstracts_xml/all_abstracts_{}.xml".format(i), "r") as f:
        lines = f.read()

    soup = BeautifulSoup(lines, "html.parser")
    # print(soup)

    articles = soup.findAll("pubmedarticle")

    for article in articles:

        try:
            abstract = article.abstract.text
        except AttributeError:
            continue

        print(article.pmid.text)
        print(article.abstract.text)
        c.execute("INSERT INTO abstracts (lit_id, abstract) VALUES (?, ?)", (article.pmid.text, article.abstract.text))


bdd.commit()
c.close()
bdd.close()


if __name__ == '__main__':
    pass
