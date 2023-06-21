from konstante import STATUS_WEIGHTS as SW
from konstante import REACTION_WEIGHTS as RW
from entiteti.status import Status




def status_score(status: Status) -> float:

    reaction_score = SW.reactions * (

          RW.likes * status.number_of_likes
        + RW.loves * status.number_of_loves
        + RW.wows * status.number_of_wows
        + RW.hahas * status.number_of_hahas
        + RW.sads * status.number_of_sads
        + RW.angrys * status.number_of_angrys
        + RW.special * status.number_of_special

    )

    comment_score = SW.comments * status.number_of_comments
    share_score = SW.shares * status.number_of_shares

    #some function to decrease the ovarall value of status score

    return reaction_score + comment_score + share_score
