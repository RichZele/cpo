# Shapes

Step 3 of the information delivery cycle (Lectures 7 and 8): the level of information need for classroom lighting, written as SHACL shapes.

| File | What is in it | Triples |
|---|---|---|
| [`cpo-lighting-shapes.ttl`](cpo-lighting-shapes.ttl) | Two node shapes, one for classrooms and one for luminaire types, with one property shape per row of the LOIN table | 43 |

## The level of information need (ISO 7817-1)

- **Purpose:** verify the classroom lighting against EN 12464-1:2021
- **Milestone:** detail design, when the luminaires are chosen
- **Actors:** the lighting designer receives the information; the manufacturer and the architect provide it

| Object | Information | Unit, type | Source of the definition | SHACL constraint |
|---|---|---|---|---|
| Luminaire type | rated luminous flux | lm, decimal | CEN/TS 17623:2021, 04-0005 | `sh:path ( cpo:hasLuminousFlux qudt:numericValue )`, `sh:minCount 1`, `sh:datatype xsd:decimal`, `sh:minExclusive 0` |
| Luminaire type | rated input power | W, decimal | CEN/TS 17623:2021, 02-0002 | `sh:path ( cpo:hasRatedPower qudt:numericValue )`, `sh:minCount 1`, `sh:datatype xsd:decimal`, `sh:minExclusive 0` |
| Luminaire type | classification | a class | Uniclass, IEC 81346-2 | `sh:path dcterms:subject`, `sh:minCount 1` |
| Classroom | floor area | m², one value | the model (IFC) | `sh:path cpo:hasArea`, `sh:minCount 1`, `sh:maxCount 1`, `sh:class qudt:QuantityValue` |
| Classroom | lighting requirement | a requirement | EN 12464-1:2021 | `sh:path cpo:hasLightingRequirement`, `sh:minCount 1` |
| Classroom | classification | a class | Uniclass SL | `sh:path dcterms:subject`, `sh:minCount 1`, `sh:class skos:Concept` |

The flux and the power are quantity values, so their paths take two hops: from the type to the quantity node, and from the quantity node to its number.

## The validation

The data graph is the school data (`../data/cpo-school-data.ttl`), the classification and the Duplex classrooms (`../classification/`): 320 triples. Validated with pySHACL, without inference:

| Focus node | Path | Message |
|---|---|---|
| A102 | `cpo:hasArea` | LOIN: a classroom has one floor area, in m2. |
| B102 | `cpo:hasArea` | LOIN: a classroom has one floor area, in m2. |
| B102 | `cpo:hasLightingRequirement` | LOIN: a classroom has a lighting requirement. |

The graph does not conform: three violations. Classrooms 2.14 and 2.15 and the three luminaire types conform. The two Duplex rooms have their area from IFC as `props:area`, a plain number without a unit, while the LOIN asks for `cpo:hasArea`, a quantity value in m². B102 has no lighting requirement.

Fixed at the source with one SPARQL update: for each classroom with `props:area` and no `cpo:hasArea`, a `qudt:QuantityValue` with the number, rounded to two decimals, and `unit:M2`; and the classroom requirement for B102. That adds 9 triples, and validated again, the graph conforms.

Never weaken a shape just to make the data pass: the shape is the LOIN. A violation that cannot be fixed stays in the report as a finding.

The notebook of Lecture 8 runs this validation in Google Colab; it reads the school data from this repository.
