# Notebooks

The notebooks of the course, to run in Google Colab in the browser. You need only a Google account.

| Notebook | Lecture | What it does |
|---|---|---|
| [`cpo-lecture8-shacl.ipynb`](cpo-lecture8-shacl.ipynb) · [open in Colab](https://colab.research.google.com/github/RichZele/cpo/blob/main/notebooks/cpo-lecture8-shacl.ipynb) | 8 | Validates the worked example against the level of information need, written as SHACL shapes, with pySHACL. It reports the violations, fixes them at the source and validates again. Run 7 validates your own project: upload your data and your shapes. |
| [`cpo-lecture8-rules.ipynb`](cpo-lecture8-rules.ipynb) · [open in Colab](https://colab.research.google.com/github/RichZele/cpo/blob/main/notebooks/cpo-lecture8-rules.ipynb) | 8 | One question, *is a luminaire type below or above 110 lm/W?*, four ways on `../rules/cpo-rules.ttl`: a SPARQL query (Run 3), a SHACL-SPARQL constraint (Run 4), a SHACL rule (Run 5), and the SWRL rules with the reasoner Pellet in owlready2 (Runs 6 and 7). |

Open a notebook with the Colab link, then use **File › Save a copy in Drive** and work in your copy. The notebook here stays unchanged.

`cpo-lecture8-shacl.ipynb` reads the school data from this repository (`data/cpo-school-data.ttl`). The classification and the shapes are written in its cells, and they are the same as in `../classification/` and `../shapes/`.

`cpo-lecture8-rules.ipynb` downloads its files from this repository: `rules/cpo-rules.ttl`, the two files `shapes/cpo-efficacy-sparql-shape.ttl` and `shapes/cpo-derive-type-rule.ttl`, and `queries/cpo-below-minimum-efficacy.rq`. Run 1 installs Java for Pellet and owlready2 0.47, because newer versions bring a Pellet that needs Java 25.
