!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials"

"""Read the RDF file as shown in class"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**

"""

# TO DO
# Visualize the results
ns = Namespace("http://somewhere#")
g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

# TO DO
# Visualize the results
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

# TO DO
jane_smith = ns.JaneSmith
g.add((jane_smith, RDF.type, ns.Researcher))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the email address, fullName, given and family names**"""

# TO DO
g.add((jane_smith, ns.email, Literal("jane.smith@email.com")))
g.add((jane_smith, ns.fullName, Literal("Jane Smith")))
g.add((jane_smith, ns.givenName, Literal("Jane")))
g.add((jane_smith, ns.familyName, Literal("Smith")))

# Visualize the results

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

# TO DO
g.add((jane_smith, ns.worksAt, ns.UPM))
# Visualize the results

"""**Task 6.6: Add that Jown knows Jane using the FOAF vocabulary**"""

# TO DO
g.add((ns.JohnSmith, ns.knows, jane_smith))
# Visualize the results
