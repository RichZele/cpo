# Rules

Step 4 of the information delivery cycle (Lecture 8): SWRL rules that derive new knowledge from the graph.

| File | What is in it |
|---|---|
| [`cpo-rules.ttl`](cpo-rules.ttl) | One ontology to open in Protégé, `https://w3id.org/cpo/lecture7`: CPO, the school data, the classification and the Duplex classrooms, the classes `HighEfficacyLuminaireType` and `HighEfficacyLuminaire`, and two SWRL rules. Saved from Protégé, with no imports. Open it in Protégé with File > Open. |

## The rules

Luminous efficacy is the luminous flux divided by the rated input power, in lm/W (CEN/TS 17623:2021, 04-0007).

**R1, high-efficacy luminaire type.** A luminaire type whose efficacy is at least 110 lm/W is a high-efficacy luminaire type.

```
cpo:LuminaireType(?t) ^
cpo:hasLuminousFlux(?t, ?f) ^ qudt:numericValue(?f, ?fv) ^
cpo:hasRatedPower(?t, ?p) ^ qudt:numericValue(?p, ?pv) ^
swrlb:divide(?e, ?fv, ?pv) ^ swrlb:greaterThanOrEqual(?e, 110)
-> cpo:HighEfficacyLuminaireType(?t)
```

**R2, high-efficacy luminaire.** An installed luminaire of a high-efficacy type is a high-efficacy luminaire.

```
cpo:Luminaire(?l) ^ cpo:hasProductType(?l, ?t) ^ cpo:HighEfficacyLuminaireType(?t)
-> cpo:HighEfficacyLuminaire(?l)
```

The threshold of 110 lm/W is an assumption made for teaching. In a project, take the threshold from a source.

## Running them

The rules use built-ins (`swrlb:divide`, `swrlb:greaterThanOrEqual`), which HermiT ignores. Run them in Protégé 5.6 with the SWRLTab (Window > Tabs > SWRLTab) and its Drools engine:

1. **OWL+SWRL->Drools** sends the ontology and the rules: 2 rules, 75 individuals, 432 axioms.
2. **Run Drools** runs them: 707 axioms inferred, because Drools also applies the OWL 2 RL rules.
3. **Drools->OWL** writes all inferred axioms into the ontology, as asserted axioms. Do it on a copy, or do not save afterwards.

| Luminaire type | lm ÷ W | R1 |
|---|---|---|
| Multilume Flat Delta 600x600 | 4231 ÷ 37 = 114.4 | high efficacy |
| Multilume Flat Delta 300x1200 | 3853 ÷ 30.5 = 126.3 | high efficacy |
| Pleiad G4 165 | 938 ÷ 9.5 = 98.7 | no inference |

The same rules also run without Protégé, with the reasoner Pellet in owlready2: Runs 6 and 7 of the notebook [`../notebooks/cpo-lecture8-rules.ipynb`](../notebooks/cpo-lecture8-rules.ipynb), with the same result.

R2 then marks the 23 luminaires of the two panel types as high-efficacy luminaires: 8 in classroom 2.14 and 15 in classroom 2.15. The four Pleiad downlights in the corridor are not marked. That does not make them non-compliant: under the open world, a fact that is not inferred is unknown, not false.

## SHACL or SWRL?

SHACL checks whether the required information is there, in the right form, under the closed world, and its output is a report (`../shapes/`). SWRL derives what follows from the data, under the open world, and its output is new triples. Whether a flux is present is a question for SHACL; whether a luminaire is high efficacy is one for SWRL. A rule that must count or sum, such as the total flux in a room, needs a SPARQL-based rule, because SWRL does not aggregate.

The two meet in SHACL Advanced Features: a SHACL rule (`sh:rule`) derives triples, as SWRL does. `../shapes/cpo-derive-type-rule.ttl` derives the conclusion of R1 with SPARQL, and `../shapes/cpo-efficacy-sparql-shape.ttl` reports the type that R1 leaves out.
