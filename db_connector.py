from neo4j import GraphDatabase

class Customized_Neo4J_Connector:
    def __init__(self, url, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    greeter = Customized_Neo4J_Connector("bolt://localhost:7687", "neo4j", "password")
    greeter.print_greeting("hello, world")
    greeter.close()