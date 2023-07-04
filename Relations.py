from py2neo import Graph
import pandas as pd
from prolog_implementation import write_fact_and_rules
graph = Graph("bolt://localhost:7689", auth=("neo4j", "12345678"))

data = pd.read_csv("Relations_set.csv",header=None)
df = pd.DataFrame(data)

def relationships():
    return list(df[0])

relations_list = relationships()

def create_relation(Person_names_rel):
    for name_index in range(len(Person_names_rel)):
        name = Person_names_rel[name_index]
        try:
            if name in relations_list:
                print("relation creation")
                if name_index > 0 and name_index != (len(Person_names_rel)-1):
                    rule = Person_names_rel[name_index].lower() +"('"+Person_names_rel[name_index-1]+"','"+Person_names_rel[name_index+1]+"')"
                    write_fact_and_rules(rule)
                    if Person_names_rel[name_index-1] not in relations_list and Person_names_rel[name_index+1] not in relations_list:
                        result = graph.run(
                                f"""
                                MATCH (a:OWNER {{name: $name1}})
                                MATCH (b:OWNER {{name: $name2}})
                                CREATE (a)-[rel:`{Person_names_rel[name_index]}`]->(b)
                                SET a.`{Person_names_rel[name_index]}` = COALESCE(a.`{Person_names_rel[name_index]}`, []) + [$name2]
                                SET b.`{Person_names_rel[name_index]}` = COALESCE(b.`{Person_names_rel[name_index]}`, []) + [$name1]
                                RETURN rel
                                """,
                                name1=Person_names_rel[name_index-1],
                                name2=Person_names_rel[name_index+1]
                            )
                        result = str(result)
                        if result == "(No data)":
                            result1 = graph.run(
                                f"""
                                MATCH (a:OWNER {{name: $name1}})
                                MERGE (b:PERSONS {{name: $name2}})
                                CREATE (a)-[rel:`{Person_names_rel[name_index]}`]->(b)
                                SET a.`{Person_names_rel[name_index]}` = COALESCE(a.`{Person_names_rel[name_index]}`, []) + [$name2]
                                SET b.`{Person_names_rel[name_index]}` = COALESCE(b.`{Person_names_rel[name_index]}`, []) + [$name1]
                                RETURN rel
                                """,
                                name1=Person_names_rel[name_index-1],
                                name2=Person_names_rel[name_index+1]
                            )
                            result1 = str(result1)
                            if result1 == "(No data)":
                                graph.run(
                                    f"""
                                    MERGE (a:PERSONS {{name: $name1}})
                                    MERGE (b:PERSONS {{name: $name2}})
                                    CREATE (a)-[rel:`{Person_names_rel[name_index]}`]->(b)
                                    SET a.`{Person_names_rel[name_index]}` = COALESCE(a.`{Person_names_rel[name_index]}`, []) + [$name2]
                                    SET b.`{Person_names_rel[name_index]}` = COALESCE(b.`{Person_names_rel[name_index]}`, []) + [$name1]
                                    """,
                                    name1=Person_names_rel[name_index-1],
                                    name2=Person_names_rel[name_index+1])

                elif name_index == 0:
                    rule = Person_names_rel[name_index].lower() +"('"+Person_names_rel[name_index+1]+"','"+Person_names_rel[name_index+2]+"')"
                    write_fact_and_rules(rule)
                    if Person_names_rel[name_index+1] not in relations_list and Person_names_rel[name_index+2] not in relations_list:
                        result = graph.run(
                            f"""
                            MATCH (a:OWNER {{name: $name1}})
                            MATCH (b:OWNER {{name: $name2}})
                            MERGE (a)-[rel:`{Person_names_rel[name_index]}`]->(b)
                            SET a.`{Person_names_rel[name_index]}` = COALESCE(a.`{Person_names_rel[name_index]}`, []) + $name2
                            SET b.`{Person_names_rel[name_index]}` = COALESCE(b.`{Person_names_rel[name_index]}`, []) + $name1
                            RETURN rel
                            """,
                            name1=Person_names_rel[name_index+1],
                            name2=Person_names_rel[name_index+2]
                        )
                        result = str(result)
                        print("2-owner",result)
                        if result == "(No data)":
                            result1 = graph.run(
                                f"""
                                Match (a:OWNER {{name: $name1}})
                                MERGE (b:PERSONS {{name: $name2}})
                                Create (a)-[rel:`{Person_names_rel[name_index]}`]->(b)
                                SET a.`{Person_names_rel[name_index]}` = COALESCE(a.`{Person_names_rel[name_index]}`, []) + $name2
                                SET b.`{Person_names_rel[name_index]}` = COALESCE(b.`{Person_names_rel[name_index]}`, []) + $name1
                                RETURN rel
                                """,
                                name1=Person_names_rel[name_index+1],
                                name2=Person_names_rel[name_index+2]
                                )
                            result1 = str(result1)
                            print("1-owner or 2-p",result1)
                            if result1 == "(No data)":
                                print("both persons")
                                result = graph.run(
                                        f"""
                                        MERGE (a:PERSONS {{name: $name1}})
                                        MERGE (b:PERSONS {{name: $name2}})
                                        CREATE (a)-[rel:`{Person_names_rel[name_index]}`]->(b)
                                        SET a.`{Person_names_rel[name_index]}` = COALESCE(a.`{Person_names_rel[name_index]}`, []) + [$name2]
                                        SET b.`{Person_names_rel[name_index]}` = COALESCE(b.`{Person_names_rel[name_index]}`, []) + [$name1]
                                        """,
                                        name1=Person_names_rel[name_index+1],
                                        name2=Person_names_rel[name_index+2]
                                    )
                elif name_index == (len(Person_names_rel)-1):
                    rule = Person_names_rel[name_index].lower() +"('"+Person_names_rel[name_index-2]+"','"+Person_names_rel[name_index-1]+"')"
                    write_fact_and_rules(rule)
                    if Person_names_rel[name_index-2] not in relations_list and Person_names_rel[name_index-1] not in relations_list:
                        result = graph.run(
                                    f"""
                                    MATCH (a:OWNER {{name: $name1}})
                                    MATCH (b:OWNER {{name: $name2}})
                                    MERGE (a)-[rel:`{Person_names_rel[name_index]}`]->(b)
                                    SET a.`{Person_names_rel[name_index]}` = COALESCE(a.`{Person_names_rel[name_index]}`, []) + [$name2]
                                    SET b.`{Person_names_rel[name_index]}` = COALESCE(b.`{Person_names_rel[name_index]}`, []) + [$name1]
                                    RETURN rel
                                    """,
                                    name1=Person_names_rel[name_index-2],
                                    name2=Person_names_rel[name_index-1]
                                )
                        result = str(result)
                        print("OWNERS", result)
                        if result == "(No data)":
                            result1 = graph.run(
                                f"""
                                MATCH (a:OWNER {{name: $name1}})
                                MERGE (b:PERSONS {{name: $name2}})
                                CREATE (a)-[rel:`{Person_names_rel[name_index]}`]->(b)
                                SET a.`{Person_names_rel[name_index]}` = COALESCE(a.`{Person_names_rel[name_index]}`, []) + [$name2]
                                SET b.`{Person_names_rel[name_index]}` = COALESCE(b.`{Person_names_rel[name_index]}`, []) + [$name1]
                                RETURN rel
                                """,
                                name1=Person_names_rel[name_index-2],
                                name2=Person_names_rel[name_index-1]
                            )
                            result1 = str(result1)
                            print("OWNER and PERSONS", result1)
                            if result1 == "(No data)":
                                graph.run(
                                    f"""
                                    MERGE (a:PERSONS {{name: $name1}})
                                    MERGE (b:PERSONS {{name: $name2}})
                                    CREATE (a)-[rel:`{Person_names_rel[name_index]}`]->(b)
                                    SET a.`{Person_names_rel[name_index]}` = COALESCE(a.`{Person_names_rel[name_index]}`, []) + [$name2]
                                    SET b.`{Person_names_rel[name_index]}` = COALESCE(b.`{Person_names_rel[name_index]}`, []) + [$name1]
                                    """,
                                    name1=Person_names_rel[name_index-2],
                                    name2=Person_names_rel[name_index-1]
                                )
        except:
            None

def create_Node(name,gender):
    graph.run(
            f"""
            MERGE (a:PERSONS{{name: $name1 , gender: $gender}})
            """,
            name1=name,
            gender=gender
            )
    fact = gender+"('"+name+"')"
    write_fact_and_rules(fact)