# Dynamo: from GraphDB back to Revit

Lecture 9, step 6 of the information delivery cycle. A Python script for one **Python Script** node in Dynamo for Revit 2024 (CPython3). It sends query L9-6 of [`../queries/cpo-deliver-queries.rq`](../queries/cpo-deliver-queries.rq) to your GraphDB repository and writes the answers into the rooms of the open Revit model.

| File | What it does |
|---|---|
| [`cpo-graphdb-to-revit.py`](cpo-graphdb-to-revit.py) | Asks GraphDB over HTTP (the SPARQL protocol, answer as SPARQL JSON) for each room's number, calculated illuminance, status and recommended luminaire type, and sets three room parameters. Rooms are matched by their number. |
| [`cpo-graphdb-to-revit.dyn`](cpo-graphdb-to-revit.dyn) | The Dynamo graph used in Lecture 9, with the script already in the Python node: open it in Dynamo for Revit 2024, set the endpoint, Run. |
| [`cpo-room-results-shared-parameters.txt`](cpo-room-results-shared-parameters.txt) | A Revit shared parameter file with the three parameters, in the group *Analysis Results*. |

## Before you run it

1. In GraphDB, run the rule **L9-2** (after **L9-7** if it has run before), so that the results graph `https://w3id.org/cpo/results` exists.
2. In Revit, add three room parameters: **Manage › Project Parameters › Add**, **Shared parameter**, **Select…**, and pick them from `cpo-room-results-shared-parameters.txt` (Manage › Shared Parameters › Browse, to point Revit to the file). A project parameter with the same name and type works too. Category **Rooms**, **Instance**:

| Name | Type |
|---|---|
| Lighting Status | Text |
| Calculated Illuminance | Number |
| Recommended Luminaire | Text |

## The Dynamo graph

**Manage › Dynamo**, then open `cpo-graphdb-to-revit.dyn`, or build it yourself from three nodes: a **String** node with the SPARQL endpoint of your repository (`https://<server>/repositories/<repository>`), connected to IN[0] of a **Python Script** node with the script pasted into it, and a **Watch** node on its output. Then **Run**. The Watch node lists each room written, for example `A102: 491 lx, FAIL Multilume Flat Delta 600x600`.

The repository must be readable without login. If yours needs a login, click **+** on the Python node twice and connect two more String nodes, the user name to IN[1] and the password to IN[2]; never save a file with a password in it.

## Show the result

- **Room schedule:** View › Schedules › Schedule/Quantities › Rooms, with the three parameters as fields.
- **View filter:** View › Filters › New, *Lighting FAIL*, category Rooms, rule *Lighting Status equals FAIL*. In Visibility/Graphics › Filters, add it with a solid red surface pattern, and switch on **Rooms › Interior Fill** under Model Categories.

After the designer has changed the model, export IFC again, convert, load, run L9-7 and L9-2, and run the Dynamo graph again: the colours follow the graph.

## Matching rooms

The script matches the Revit room **Number** with `props:number` from IFC. More robust is the IFC GlobalId: export IFC with *Store the IFC GUID in an element parameter after export*, then match the room parameter `IfcGUID` with `props:globalIdIfcRoot`.

## Run it again

Dynamo in **Manual** mode runs a node again only when something in the graph has changed. After a change in GraphDB, nothing in the graph has changed, so **Run** reuses the old answer. To ask GraphDB again: open the Python node (right-click › Edit), make any change (a space in a comment), and click **Save and run**.

## Tested

Run on the Duplex model in Revit 2024 with Dynamo for Revit (CPython3), against GraphDB 11.5 (repository open for reading): A102 491 lx FAIL, B102 539 lx PASS; after the type swap in A102, 539 lx PASS. To check that the values came from the script, select a room before and after Run (Properties, group Data), and look at the Undo list: the last change is the Dynamo script.
