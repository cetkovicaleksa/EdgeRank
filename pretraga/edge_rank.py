from entiteti.status import Status
from entiteti.person import Person
from strukture.graph import Graph
from pretraga.time_factor import time_decay
from pretraga.status_eval_factor import status_score


def edge_rank_score(status: Status, person: Person, graph: Graph):
    return graph.get_edge(person, status.status_author) * status_score(status) * time_decay(status.status_date_published)
