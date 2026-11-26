# TADS23 Lecture 9 · Back to Revit
# Dynamo Python Script node (CPython3, Dynamo for Revit 2024).
# Sends a SPARQL query to GraphDB and writes the answers into room parameters of the open Revit model;
# here for the Lecture 9 use case, classroom lighting: query L9-6 in queries/cpo-deliver-queries.rq.
#
# Inputs of the node:
#   IN[0]  SPARQL endpoint of your GraphDB repository, e.g. https://<server>/repositories/<repository>
#   IN[1]  optional: user name, only if the repository needs a login (add inputs with + on the node)
#   IN[2]  optional: password; never save a password in a file you share
#
# Before you run it, add three project parameters to the category Rooms (instance parameters):
#   Lighting Status          Text
#   Calculated Illuminance   Number
#   Recommended Luminaire    Text
# Rooms are matched by their number (Revit: Number; in the graph: props:number, from IFC).

import clr, json
import urllib.request, urllib.parse

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, BuiltInParameter
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

endpoint = IN[0]; user, password = (IN[1], IN[2]) if len(IN) > 2 else ('', '')

QUERY = """
PREFIX cpo:   <https://w3id.org/cpo#>
PREFIX qudt:  <http://qudt.org/schema/qudt/>
PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
PREFIX props: <https://w3id.org/props#>
SELECT ?number ?calculated ?status ?recommended
WHERE {
  ?room props:number ?number ;
        cpo:lightingStatus ?status ;
        cpo:hasCalculatedIlluminance/qudt:numericValue ?calculated .
  OPTIONAL {
    SELECT ?room (GROUP_CONCAT(?fix; separator=", ") AS ?recommended)
    WHERE {
      { SELECT ?room (COUNT(?lum) AS ?n) WHERE { ?lum a cpo:Luminaire ; cpo:installedIn ?room . } GROUP BY ?room }
      ?room cpo:lightingStatus "FAIL" ;
            cpo:hasArea/qudt:numericValue ?area ;
            cpo:hasLightingRequirement/cpo:hasRequiredIlluminance/qudt:numericValue ?required .
      ?type a cpo:LuminaireType ; rdfs:label ?fix ;
            cpo:hasLuminousFlux/qudt:numericValue ?flux .
      FILTER (ROUND(?n * ?flux * 0.6 * 0.8 / ?area) >= ?required)
    }
    GROUP BY ?room
  }
}
"""

# 1 · Ask GraphDB: an HTTP GET with the query, the answer as SPARQL JSON
headers = {'Accept': 'application/sparql-results+json'}
if user:
    # GraphDB with security on: log in once; the answer carries a token for the next requests
    server = endpoint.split('/repositories/')[0]
    login = urllib.request.Request(server + '/rest/login', method='POST',
                                   data=json.dumps({'username': user, 'password': password}).encode('utf-8'),
                                   headers={'Content-Type': 'application/json'})
    headers['Authorization'] = urllib.request.urlopen(login, timeout=30).headers['Authorization']
url = endpoint + '?' + urllib.parse.urlencode({'query': QUERY})
request = urllib.request.Request(url, headers=headers)
rows = json.loads(urllib.request.urlopen(request, timeout=30).read().decode('utf-8'))['results']['bindings']

# one entry per room number: {'A102': {'calculated': 491.0, 'status': 'FAIL', 'recommended': '...'}}
results = {}
for row in rows:
    results[row['number']['value']] = {
        'calculated': float(row['calculated']['value']),
        'status': row['status']['value'],
        'recommended': row['recommended']['value'] if 'recommended' in row else ''}

# 2 · Write the answers into the rooms of the open model, in one transaction
doc = DocumentManager.Instance.CurrentDBDocument
rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms) \
                                     .WhereElementIsNotElementType().ToElements()
report = []
TransactionManager.Instance.EnsureInTransaction(doc)
for room in rooms:
    number = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()
    if number not in results:
        continue
    r = results[number]
    room.LookupParameter('Lighting Status').Set(r['status'])
    room.LookupParameter('Calculated Illuminance').Set(r['calculated'])
    room.LookupParameter('Recommended Luminaire').Set(r['recommended'])
    report.append('{}: {} lx, {} {}'.format(number, int(r['calculated']), r['status'], r['recommended']).strip())
TransactionManager.Instance.TransactionTaskDone()

OUT = report        # e.g. ['A102: 491 lx, FAIL Multilume Flat Delta 600x600', 'B102: 539 lx, PASS']
