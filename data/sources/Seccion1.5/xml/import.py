import requests
import os
import time
from py2neo import neo4j, authenticate, Graph
import tweepy

# Connect to graph and add constraints.
url = "http://localhost:7474/db/data/"
authenticate("localhost:7474", "neo4j", "test1234")
graph = Graph(url)

# Add uniqueness constraints.
graph.cypher.execute("CREATE CONSTRAINT ON (i:Image) ASSERT i.filename IS UNIQUE;")
graph.cypher.execute("CREATE CONSTRAINT ON (t:Tag) ASSERT t.text IS UNIQUE;")
graph.cypher.execute("CREATE CONSTRAINT ON (l:Lex) ASSERT l.text IS UNIQUE;")
graph.cypher.execute("CREATE CONSTRAINT ON (s:State) ASSERT s.name IS UNIQUE;")
graph.cypher.execute("CREATE CONSTRAINT ON (c:City) ASSERT c.name IS UNIQUE;")

# fetch XML data

from process_xml import parse_xml

while True:
        # Pass dict to Cypher and build query.
        query = """
        UNWIND {images} AS i

        WITH i
        ORDER BY i.filename

        WITH i,
             i.tags AS t,
             i.lexes AS l,
             i.state AS s,
             i.city AS c

        MERGE (image:Image {filename:i.filename})
        SET image.filename = i.filename,
            image.address = i.address

        MERGE (city:City {name:c.name})
        SET city.name = c.name

        MERGE (image)-[:FROM]->(city)

        MERGE (state:State {name:s.name})
        SET state.name = s.name

        MERGE (image)-[:FROM]->(state)

        FOREACH (t IN i.tags |
          MERGE (tag:Tag {text:LOWER(t.text)})
          MERGE (image)-[:TAG]->(tag)
        )

        FOREACH (l IN i.lexes |
          MERGE (lex:Lex {text:LOWER(l.text)})
          MERGE (image)-[:LEX]->(lex)
        )
        """

        # Send Cypher query.
        graph.cypher.execute(query, images=parse_xml())
        print("Iamges added to graph!\n")
        # ----
        break
