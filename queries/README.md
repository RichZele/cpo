# Queries

The SPARQL queries of Lecture 6: ABID-Mo step 11, the test of the competency questions, and step 5 of the information delivery cycle. One query of Lecture 8, and the queries of Lecture 9.

| File | What is in it |
|---|---|
| [`cpo-sparql-queries.rq`](cpo-sparql-queries.rq) | 30 queries, numbered as on the slides: D1 to D9 on DBpedia (`https://dbpedia.org/sparql`), to learn the language; Q1 to Q21 on the CPO graph in GraphDB, with the three files of `../graphdb/`, each in its own named graph |
| [`cpo-deliver-queries.rq`](cpo-deliver-queries.rq) | Lecture 9: L9-1 to L9-7. The lumen method E = n × Φ × UF × MF / A (UF 0.6, MF 0.8, teaching assumptions) as a SPARQL INSERT rule (L9-2) that writes the calculated illuminance and a status, PASS or FAIL, into the graph `https://w3id.org/cpo/results`; CQ1, classrooms below target (L9-3); CQ3, catalogue types that fix them, with the lighting power density (L9-4), and the number of luminaires needed (L9-5); the query Dynamo sends (L9-6); and the undo (L9-7). Needs `../data/cpo-duplex-lighting.ttl` in GraphDB. |
| [`cpo-below-minimum-efficacy.rq`](cpo-below-minimum-efficacy.rq) | Lecture 8: which luminaire types have a luminous efficacy below 110 lm/W? On `../rules/cpo-rules.ttl`. One row: the Pleiad G4 165, 938 lm, 9.5 W. The same condition as the SHACL-SPARQL constraint in `../shapes/` and the opposite of SWRL rule R1 in `../rules/`. |

Copy one query at a time, from the line under its number down to the next line of double bars, paste it into the SPARQL editor and click Run.

## The competency questions

| CQ | Query | Result |
|---|---|---|
| CQ1 · status of each building project | Q8 | Södra skolan: `cpo:active` |
| CQ2 · products in a building project | Q9 | 27 luminaires |
| CQ3 · projects and their budgets | Q10 | Södra skolan, new school building: 48,000,000 |
| CQ4 · luminaires in each room | Q11 | Classroom 2.14: 8 · Classroom 2.15: 15 · Corridor 2.C1: 4 |
| CQ5 · flux, power and manufacturer of each luminaire type | Q12 | 4231 lm, 37 W · 3853 lm, 30.5 W · 938 lm, 9.5 W; Fagerhult |
| CQ6 · required illuminance per room | Q13 | 500 lx, EN 12464-1:2021, for both classrooms |
| CQ7 · classrooms below the requirement | L9-2, then L9-3 | Classroom 2.14: 271 lx · Classroom 2.15: 462 lx · A102: 491 lx; all below 500 lx. B102: 539 lx, PASS |

## The two routes, linked

The school data was made by hand (route 1); the Duplex comes from the IFC model (route 2). Q19 asks whether any luminaire is installed in the Duplex living room A102: no. Q20, a SPARQL update, writes a luminaire of type Pleiad G4 into the school graph, installed in the space A102 that it finds in the Duplex graph by its name: 3 statements. Q19 then answers yes, and Q11 shows A102 with one luminaire next to the school's rooms. Q21 removes the three statements again.

Updates change the data for everyone who uses the repository: run them only in your own repository and named graphs, and keep the query that undoes them.
