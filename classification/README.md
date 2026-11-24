# Classification

Step 2 of the information delivery cycle (Lecture 7): the things in the graph get a class from a shared classification system, written as SKOS.

| File | What is in it | Triples |
|---|---|---|
| [`cpo-classification.ttl`](cpo-classification.ttl) | The classes the worked example needs, as SKOS concept schemes: three Uniclass 2015 classes with their parents, and six IEC 81346-2 classes | 84 |
| [`cpo-lecture7-data.ttl`](cpo-lecture7-data.ttl) | The links from the things to their classes, with `dcterms:subject`, and two Duplex rooms from the IFC model, A102 and B102, used as classrooms | 17 |

## The classes

| Thing in the graph | Uniclass 2015 (ISO 12006-2) | IEC 81346-2:2019 |
|---|---|---|
| Classrooms 2.14 and 2.15 (school); A102 and B102 (Duplex) | `SL_25_10_14` Classrooms, under `SL_25_10` Educational spaces | |
| Pleiad G4 165 (Fagerhult 73029-520) | `Pr_70_70_48_70` Recessed downlights, under `Pr_70_70_48` Luminaires, lighting track and lighting accessories | `UAC` light fixture: a positioning object for a light source |
| Multilume Flat Delta 600x600 and 300x1200 (23784-402, 23916-529) | `Pr_70_70_48_45` LED light panels, under `Pr_70_70_48` | `UAC` light fixture |

Uniclass tables: Spaces/locations v1.37 and Products v1.44, October 2026, checked on uniclass.thenbs.com on 21 November 2026. The luminaire holds the light source, so in IEC 81346-2 it is `UAC`; the lamp that emits the light would be `EAA`, electric lamp.

## How it is written

- A table is a `skos:ConceptScheme`; each class is a `skos:Concept` with `skos:inScheme`, its code in `skos:notation`, its name in `skos:prefLabel`, and its parent with `skos:broader`.
- A Uniclass class uses the address of its page as its IRI: `https://uniclass.thenbs.com/taxon/` and the code in lower case, for example `uc:pr_70_70_48_70`.
- IEC 81346-2 publishes no pages for its classes, so they get IRIs in the CPO namespace for classes, `https://w3id.org/cpo/class/iec81346-2/`, with the definition from the standard in `skos:definition`.
- A thing points to its class with `dcterms:subject`. The luminaire types are classified, not each luminaire, because every installed copy shares the class of its type.

Why SKOS and not OWL classes? A classification table is a list of agreed codes and names, with broader and narrower classes, kept by someone else. It is not a set of logical definitions for a reasoner, so SKOS describes it better than OWL classes do.

## Ask by class

With `skos:broader*`, a query finds the luminaire types in Uniclass's Luminaires class, at any depth below it:

```sparql
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos:    <http://www.w3.org/2004/02/skos/core#>
PREFIX uc:      <https://uniclass.thenbs.com/taxon/>

SELECT ?type ?class
WHERE {
  ?t dcterms:subject ?c ;
     rdfs:label ?type .
  ?c skos:broader* uc:pr_70_70_48 ;
     skos:prefLabel ?class .
}
```

The result is the three Fagerhult types: two LED light panels and one recessed downlight.

Uniclass is published by NBS under [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/): use and share the codes with credit to NBS, and do not change the tables or add codes.
