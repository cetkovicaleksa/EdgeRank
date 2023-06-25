from typing import List, Dict

from entiteti.status import Status
from entiteti.comment import Comment
from entiteti.share import Share
from entiteti.reaction import Reaction
from entiteti.person import Person
from pretraga.time_factor import time_decay

from strukture.graph import Graph
from konstante import HIW



def eval_share(share: Share):
    pass

def eval_comment(comment: Comment):
    pass

def eval_reaction(reaction: Reaction):
    pass

def make_affinity_graph(fren: List[Person], statusi_dict: Dict[str, Status], komentari: List[Comment], djeljenja: List[Share], reakcije: List[Reaction]) -> Graph:
    graph = Graph(fren, 1)
    establish_connections(graph, statusi_dict, komentari, djeljenja, reakcije)
    return graph



def establish_connections(graph: Graph, statusi_dict: Dict[str, Status], komentari: List[Comment], djeljenja: List[Share], reakcije: List[Reaction]):
    fren = graph.vertices()

    for person1, person2 in fren:
        if person1 in person2.friends: graph.increase_edge_weight(person2, person1, HIW.friends)
        if person2 in person1.friends: graph.increase_edge_weight(person1, person2, HIW.friends)

    for share in djeljenja:
        graph.increase_edge_weight(share.who_shared, statusi_dict[share.status_id].author, HIW.share * time_decay(share.date_shared))

    for comment in komentari:
        graph.increase_edge_weight(comment.comment_author, statusi_dict[comment.status_id].author, eval_comment(comment) )

    for reaction in reakcije:
        graph.increase_edge_weight(reaction.who_reacted, statusi_dict[reaction.status_id].author, eval_reaction(reaction))