# GraphDB

The three files that make up the course's GraphDB repository. Import each one into its own named graph:

| # | File | Named graph | Triples |
|---|---|---|---|
| 1 | [`cpo-all.ttl`](cpo-all.ttl) | `https://w3id.org/cpo` | 374 |
| 2 | [`cpo-school-data.ttl`](cpo-school-data.ttl) | `https://w3id.org/cpo/data` | 219 |
| 3 | [`ifcmodel_LBD.ttl`](ifcmodel_LBD.ttl) | `https://w3id.org/cpo/duplex` | 14,988 |
| | | **Total** | **15,581** |

- `cpo-all.ttl` is the ontology as loaded in GraphDB. It is not the same file as `ontology/cpo-merged.ttl`; use this one, so that the counts in the SPARQL exercises match.
- `cpo-school-data.ttl` is the same data as `data/cpo-school-data.ttl`.
- `ifcmodel_LBD.ttl` is the duplex IFC model converted to RDF with IFCtoLBD in the Colab notebook (base IRI `https://w3id.org/cpo/duplex/`, properties at Level 1, no geometry).
