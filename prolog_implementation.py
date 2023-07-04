from pyswip import Prolog

prolog = Prolog()
prolog.consult('knowledgebase.pl')

def write_fact_and_rules(query):
    with open('knowledgebase.pl', 'a') as kb_file:
        kb_file.write(query + '.\n')
        
def get_results(query):
    results = list(prolog.query(query))
    return results

def print_results(results):
    for result in results:
        for key, value in result.items():
            print(key + ': ' + value)
        print('---')

def check_relation(name, relation):
    query = relation + '(' + 'X, ' + name + ')'
    results = get_results(query)
    if results:
        print('The following person(s) have the ' + relation + ' relation with ' + name + ':')
        print_results(results)
    else:
        print('No one has the ' + relation + ' relation with ' + name + '.')
