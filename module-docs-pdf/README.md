# Design documentation (PDF), module by module

This folder holds the design of each module as a PDF. For the reference documentation of every class and property as a website, made with WIDOCO, see [doc/](../doc/) or https://richzele.github.io/cpo/doc/cpo/.

One PDF per CPO module, in the layout of MODL, the Modular Ontology Design Library (Shimizu, Hirt and Hitzler, 2019). Each PDF has a module card, the Graffoo schema diagram, a summary, the axioms in description logic, one explanation per axiom, and the competency questions the module answers.

The axioms in each PDF are checked against the published Turtle file of its module, so the PDFs describe exactly the ontology at `https://w3id.org/cpo`.

| PDF | Module | Ontology IRI | Turtle file | Online documentation | Pages | Axioms |
|---|---|---|---|---|---|---|
| [TADS23_CPO-Doc_1_Project.pdf](TADS23_CPO-Doc_1_Project.pdf) | Project | `https://w3id.org/cpo/project` | [ontology/cpo-project.ttl](../ontology/cpo-project.ttl) | [doc/project](https://richzele.github.io/cpo/doc/project/) | 4 | 37 |
| [TADS23_CPO-Doc_2_Product.pdf](TADS23_CPO-Doc_2_Product.pdf) | Product | `https://w3id.org/cpo/product` | [ontology/cpo-product.ttl](../ontology/cpo-product.ttl) | [doc/product](https://richzele.github.io/cpo/doc/product/) | 3 | 28 |
| [TADS23_CPO-Doc_3_Requirement.pdf](TADS23_CPO-Doc_3_Requirement.pdf) | Requirement | `https://w3id.org/cpo/requirement` | [ontology/cpo-requirement.ttl](../ontology/cpo-requirement.ttl) | [doc/requirement](https://richzele.github.io/cpo/doc/requirement/) | 2 | 16 |
| [TADS23_CPO-Doc_4_Spanning-axioms.pdf](TADS23_CPO-Doc_4_Spanning-axioms.pdf) | Composition and spanning axioms | `https://w3id.org/cpo` | [ontology/cpo.ttl](../ontology/cpo.ttl) | [doc/cpo](https://richzele.github.io/cpo/doc/cpo/) | 3 | 20 |

All modules share one namespace, `https://w3id.org/cpo#`, with the prefix `cpo:`. The composed ontology `https://w3id.org/cpo` imports the three modules and BOT, as the reduced copy used in the course (`ontology/bot.ttl`). To open the whole ontology in Protégé, download the `ontology/` folder and open `cpo.ttl`: `catalog-v001.xml` resolves each import to its local file.

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


Reference: C. Shimizu, Q. Hirt and P. Hitzler (2019), MODL: A Modular Ontology Design Library, in Proceedings of the 10th Workshop on Ontology Design and Patterns (WOP 2019), CEUR Workshop Proceedings 2459.

Maintainer: Rahel Kebede, rahel.kebede@ju.se · Licence: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
