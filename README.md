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

Maintainer: Rahel Kebede, rahel.kebede@ju.se

Licence: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See `LICENSE`.
