# Level of information need

Step 3 of the information delivery cycle (Lecture 7): the level of information need (LOIN) for classroom lighting, after ISO 7817-1:2024.

| File | What is in it |
|---|---|
| [`cpo-loin-classroom-lighting.xlsx`](cpo-loin-classroom-lighting.xlsx) | The LOIN table, on one sheet: the prerequisites, then one row per piece of information |

## The sheet

**1 · Prerequisites** (ISO 7817-1, clause 5). These inform the LOIN but are not part of it:

- **Purpose (why):** verify that the classroom lighting meets EN 12464-1:2021.
- **Milestone (when):** detail design, when the luminaire types are chosen.
- **Receiver and providers (who):** the lighting designer receives the information; the manufacturer, the architect and the client provide it.
- **Objects (what):** luminaire types and classrooms.
- **Breakdown structures:** the classification systems used, Uniclass 2015 and IEC 81346-2 (see `../classification/`).

**2 · Level of information need** (ISO 7817-1, clause 6). One row per piece of information, with these columns:

| Column | What it gives |
|---|---|
| Object | The object the information is about: luminaire type or classroom |
| Aspect | Alphanumerical (identification or information content), geometrical, or documentation |
| Information | The property: rated luminous flux, rated input power, floor area, lighting requirement, classification |
| Unit, type | The unit and the datatype, with any limit, such as lm, decimal, > 0 |
| Defined in | Where the property is defined: CEN/TS 17623:2021, EN 12464-1:2021, Uniclass, IEC 81346-2, or the model |
| Provided by | The actor who delivers it |

All six rows for this purpose are alphanumerical. Geometrical information and documentation are not required.

## From the table to SHACL

Each alphanumerical row becomes one property shape in [`../shapes/cpo-lighting-shapes.ttl`](../shapes/cpo-lighting-shapes.ttl), and each object becomes a node shape. The shapes README gives the constraint for each row and the validation report. In a project, change the table first and the shapes after it, because the shapes implement the table.
