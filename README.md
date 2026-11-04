# Construction Project Typology Ontology (CPO)

An OWL ontology of building projects, their phases, the products installed in their buildings, and the requirements on their spaces. It is the worked example of the course TADS23 Advanced Building Information Delivery at Jönköping University.

- Ontology: https://w3id.org/cpo
- Documentation: https://richzele.github.io/cpo/
- Namespace: `https://w3id.org/cpo#` (prefix `cpo:`)

| Ontology IRI | File | Content |
|---|---|---|
| `https://w3id.org/cpo` | `ontology.ttl` | The composed ontology: imports the modules and BOT, with the alignment and spanning axioms |
| `https://w3id.org/cpo/project` | `project/ontology.ttl` | Building projects, their types, phases and status |
| `https://w3id.org/cpo/product` | `product/ontology.ttl` | Installed products, their types and quantities |
| `https://w3id.org/cpo/requirement` | `requirement/ontology.ttl` | Lighting requirements for types of space |

To use it, open `https://w3id.org/cpo` in Protégé (File > Open from URL). The modules and BOT are imported from their own IRIs.

## For education

This repository is made for teaching. CPO is the worked example of the course TADS23 Advanced Building Information Delivery at Jönköping University. In the lectures, students build it step by step with ABID-Mo, the course's modular ontology modeling method:

| Lecture | What is built |
|---|---|
| 4a | The project module: building projects, their phases and status |
| 4b | The product module: installed products and their types from a manufacturer catalogue |
| 4c | The requirement module, and the composed ontology that imports the modules, aligns them with BOT and connects them with spanning axioms |

Students can compare their own ontology with the files here and reuse CPO in their projects. The ontology is kept small on purpose, so that each modeling decision can be explained in class; it is an example for learning, not a complete ontology for practice.

Maintainer: Rahel Kebede, rahel.kebede@ju.se

Licence: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See `LICENSE`.
