# CPO documentation, module by module

One PDF per CPO module, in the layout of MODL, the Modular Ontology Design Library (Shimizu, Hirt and Hitzler, 2019). Each PDF has a module card, the Graffoo schema diagram, a summary, the axioms in description logic, one explanation per axiom, and the competency questions the module answers.

The axioms in each PDF are checked against the published Turtle file of its module, so the PDFs describe exactly the ontology at `https://w3id.org/cpo`.

| PDF | Module | Ontology IRI | Turtle file | Online documentation | Pages | Axioms |
|---|---|---|---|---|---|---|
| [TADS23_CPO-Doc_1_Project.pdf](TADS23_CPO-Doc_1_Project.pdf) | Project | `https://w3id.org/cpo/project` | [ontology/cpo-project.ttl](../ontology/cpo-project.ttl) | [doc/project](https://richzele.github.io/cpo/doc/project/) | 4 | 37 |
| [TADS23_CPO-Doc_2_Product.pdf](TADS23_CPO-Doc_2_Product.pdf) | Product | `https://w3id.org/cpo/product` | [ontology/cpo-product.ttl](../ontology/cpo-product.ttl) | [doc/product](https://richzele.github.io/cpo/doc/product/) | 3 | 28 |
| [TADS23_CPO-Doc_3_Requirement.pdf](TADS23_CPO-Doc_3_Requirement.pdf) | Requirement | `https://w3id.org/cpo/requirement` | [ontology/cpo-requirement.ttl](../ontology/cpo-requirement.ttl) | [doc/requirement](https://richzele.github.io/cpo/doc/requirement/) | 2 | 16 |
| [TADS23_CPO-Doc_4_Spanning-axioms.pdf](TADS23_CPO-Doc_4_Spanning-axioms.pdf) | Composition and spanning axioms | `https://w3id.org/cpo` | [ontology/cpo.ttl](../ontology/cpo.ttl) | [doc/cpo](https://richzele.github.io/cpo/doc/cpo/) | 3 | 19 |

All modules share one namespace, `https://w3id.org/cpo#`, with the prefix `cpo:`. The composed ontology `https://w3id.org/cpo` imports the three modules and BOT (`https://w3id.org/bot`); to open the whole ontology in Protégé, use File > Open from URL with `https://w3id.org/cpo`.

## The Lecture 4c checkpoint

The files handed out in the lectures use the course IRIs `http://ju.se/ConstructionProjOnto/...`, with the namespace `http://ju.se/ConstructionProjOnto#`. The ontology is the same; only the IRIs differ. The published version uses the persistent w3id IRIs above, so cite and reuse those.

One axiom differs. In the checkpoint, `installedIn` is functional, which is allowed there because the checkpoint uses a reduced copy of BOT without BOT's property chain. The published CPO imports the real BOT, in which `installedIn` is a non-simple property and cannot be functional in OWL 2 DL; the rule that a product is installed in one space is checked on the data with SHACL instead. That is why the Spanning-axioms PDF here has 19 axioms. The [README of the repository](../README.md#two-modeling-notes) explains this in more detail.

## Notation

| Axiom | Description logic |
|---|---|
| subclass | `A ⊑ B` |
| domain of p | `∃p.⊤ ⊑ C` |
| range of p | `⊤ ⊑ ∀p.C` |
| functional | `⊤ ⊑ ≤1 p.⊤` |
| inverse | `q ≡ p⁻` |
| transitive | `p ∘ p ⊑ p` |
| disjoint | `A ⊓ B ⊑ ⊥` |
| exactly one, at least one | `=1 p.C`, `≥1 p.C` |

## Source

`source/` holds what builds the PDFs; see [source/README.md](source/README.md).

Reference: C. Shimizu, Q. Hirt and P. Hitzler (2019), MODL: A Modular Ontology Design Library, in Proceedings of the 10th Workshop on Ontology Design and Patterns (WOP 2019), CEUR Workshop Proceedings 2459.

Maintainer: Rahel Kebede, rahel.kebede@ju.se · Licence: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
