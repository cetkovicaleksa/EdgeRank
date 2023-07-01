from typing import List, Dict, Set
from data.data_tools.stopwatch import StopwatchMessageMaker

from entiteti.status import Status
from entiteti.comment import Comment
from entiteti.share import Share
from entiteti.reaction import Reaction
from entiteti.person import Person
from pretraga.time_factor import time_decay

from strukture.graph import Graph
from konstante import HIW, RW



def eval_share(share: Share):
    return HIW.share * time_decay(share.date_shared)

def eval_comment(comment: Comment):
    return HIW.comment * (
        RW.likes*comment.number_of_likes +
        RW.angrys*comment.number_of_angrys +
        RW.hahas*comment.number_of_hahas +
        RW.loves*comment.number_of_loves +
        RW.sads*comment.number_of_sads +
        RW.special*comment.number_of_special +
        RW.wows*comment.number_of_wows) * time_decay(comment.date_commented)
    

def eval_reaction(reaction: Reaction):    
    reaction_score = HIW.reaction * time_decay(reaction.date_reacted)

    if reaction.reaction_type == "angrys": return RW.angrys * reaction_score
    if reaction.reaction_type == "sads": return RW.sads * reaction_score
    if reaction.reaction_type == "likes": return RW.likes * reaction_score
    if reaction.reaction_type == "loves": return RW.loves * reaction_score
    if reaction.reaction_type == "hahas": return RW.hahas * reaction_score
    if reaction.reaction_type == "special": return RW.special * reaction_score
    if reaction.reaction_type == "wows": return RW.wows * reaction_score

@StopwatchMessageMaker("No graph cache, making graph...", "Made graph in: ")
def make_affinity_graph(fren: Dict[str, Person], statusi_dict: Dict[str, Status], comments: List[Comment], shares: List[Share], reactions: List[Reaction]) -> Graph:
    graph = Graph(fren.values(), 1)
    establish_connections(graph, fren, statusi_dict, comments, shares, reactions)
    return graph


#@StopwatchMessageMaker("Making graph connections...", "Made graph connections in: ")
def establish_connections(graph: Graph, friends_dict: Dict[str, Person], statusi_dict: Dict[str, Status], komentari: List[Comment], djeljenja: List[Share], reakcije: List[Reaction]):
    fren: Set[Person] = graph.vertices() 
    aquaintances = HIW.friends // 3

    for person in fren:  #maby add multiple levels
        for person_fren in person.friends:
            graph.increase_edge_weight(person, person_fren, HIW.friends)
            for persons_fren_fren in person_fren.friends:
                graph.increase_edge_weight(person_fren, persons_fren_fren, aquaintances)
    
    print('finished friends')
    print(graph.vertex_count(),graph.edge_count(), sep='|')

    for share in djeljenja:
        graph.increase_edge_weight(share.who_shared, share.status.status_author, eval_share(share)) #status_id is now a status
    print('finished shares')

    for comment in komentari:
        graph.increase_edge_weight(comment.comment_author, comment.status.status_author, eval_comment(comment))
    print('finished comments')
    for reaction in reakcije:
        graph.increase_edge_weight(reaction.who_reacted, reaction.status.status_author, eval_reaction(reaction))
    print('finished reactions')

    print(graph.vertex_count(),graph.edge_count(),graph.get_default_edge_weight(), sep='|')

        #u statusu, komentaru i reakciji autor nije person nego samo string ali imaju istu hesh vrijednost