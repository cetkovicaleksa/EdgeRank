from typing import Any, List, Hashable, Set, Union
from collections import defaultdict, Callable, namedtuple


class Graph:
    """Implementacija usmjerenog grafa gdje svaki vertex sadrzi kolekiju susjednih."""
    __slots__ = "_adj", "_vertices _default_edge_weight"

    class Edge(namedtuple("Edge", "outgoing incoming value")): #maby make it hashable for ordered pair (outgoing, incoming)
        pass
    class InvalidVertexException(Exception):
        pass
    class VertexAlreadyExistsException(Exception):
        pass
    class EdgeAlreadyExistsException(Exception):
        pass



    def __init__(self, vertices: List[Hashable], default_weight: float = 0) -> None:
        self._adj = OutgoingDict(lambda: IncomingDict(default_weight))    # {  v0:{v2:weight},   v1:{v0:weight},  v2:{v1:weight, v0:weight}  }
        self._vertices = set(vertices)   #only to know if the vertex exists in the graph
        self._default_edge_weight = default_weight #to make it easier and faster to get the IncomingDict default value


        
    def _validate_vertex(self, v) -> Union[None, 'Graph.InvalidVertexException']:
        if v in self._vertices:
            return
        raise self.InvalidVertexException(f"Vertex {v} doesn't exist in the graph.")
    
    def vertex_count(self) -> int:
        return len(self._vertices)

    def vertices(self) -> Set[Hashable]:
        return self._vertices

    def edge_count(self) -> int:
        return sum( [len(x) for x in self._adj.values()] )

    def edges(self) -> List['Graph.Edge']: #can't be set because Graph.Edge is not hashable in the desirable way (1, 2) <=> (2,1)
        return [ 
                self.Edge(outgoing, incoming, value)
                for outgoing, incoming_dict in self._adj.items()
                for incoming, value in incoming_dict.items()
               ]


    def get_edge(self, u, v) -> Union[float, 'Graph.InvalidVertexException']:
        self._validate_vertex(u)
        self._validate_vertex(v)        
        return self._adj[u][v]  #will return the default value if the edge doesn't exist between u and v


    def insert_vertex(self, v: Hashable) -> Union[None, 'Graph.VertexAlreadyExistsException']:
        if v in self._vertices:
            raise self.VertexAlreadyExistsException(f"Vertex {v} already exists in the graph.")
        self._vertices.add(v)

    def insert_edge(self, u, v, w: float) -> Union[None, 'Graph.InvalidVertexException', 'Graph.EdgeAlreadyExistsException']:
        #Inserts a new edge from u to v if it doesn't exist already.
        self._validate_vertex(u)
        self._validate_vertex(v)
        
        if v in self._adj[u].keys():  #prevents overwrites, this won't ignore the edges implicitly set to default value
            raise self.EdgeAlreadyExistsException(f"Edge from '{u}' to '{v}' already exists.") 
        
        self._adj[u][v] = w


    def remove_vertex(self, v) -> Union[None, 'Graph.InvalidVertexException']: #TODO: recheck
        """
        Removes the vertex and all outgoing and incoming edges.
        Raises InvalidVertexException if vertex doesn't exist in the graph.
        """
        self._validate_vertex(v)

        del self._adj[v]  #removing all outgoing edges

        for incoming_dict in self._adj.values():  #removing all incoming edges
            del incoming_dict[v]  #can use del without caring if the key exists because IncomingDict never raises KeyError and passing a nonexistent key to del is not a problem

    def remove_edge(self, u, v) -> Union[bool, 'Graph.InvalidVertexException']:
        """
        After the call the edge will have been removed.
        Returns True if the edge existed, False if it didn't.
        Raises InvalidVertexException if either u or v is invalid.
        """
        self._validate_vertex(u)
        self._validate_vertex(v)
        
        if v not in self._adj[u].keys(): #this will count the edges implicitly set to default value as valid edges
            return False
        
        del self._adj[u][v]
        return True
    
    
    def modify_edge(self, u, v, f: Callable[[float], float]) -> Union[None, 'Graph.InvalidVertexException']:
        """
        Substitutes the current weight of the edge with its image in the provided function f.
        The function must be defined as 'f: R -> X', where R is the set of real numbers and X ⊆ R.
        Raises InvalidVertexException if either u or v is invalid.
        """
        self._validate_vertex(u)
        self._validate_vertex(v)

        if not callable(f):
            raise ValueError("The provided parameter 'f' is not a function. [ {f} ]")

        self._adj[u][v]: float = f(self._adj[u][v])
    
    def increase_edge_weight(self, u, v, w: float) -> Union[None, 'Graph.InvalidVertexException']:
        self._validate_vertex(u)
        self._validate_vertex(v)

        self._adj[u][v] += w  #make sure it will work when the u,v is not initially in the graph


    def degree(self, v, outgoing = True) -> Union[int, 'Graph.InvalidVertexException']:
        #Doesn't validate vertex because it calls incident_edges which validates it.
        return len(self.incident_edges(v, outgoing))        #hmm

    def incident_edges(self, v, outgoing = True) -> Union[List['Graph.Edge'], 'Graph.InvalidVertexException']:
        self._validate_vertex(v)
        if outgoing is True:
            return [ self.Edge(v, u, w) for u, w in self._adj[v].items() ]

        return [ self.Edge(u, v, u[v]) for u in self._adj.keys() 
                if self._adj[u][v] != self._default_edge_weight ] #TODO:  #don't like it bc it ignores the edges that are implicitly set to default value and is slow
    

    #Only call if you really have to.
    def change_default_weight(self, new_weight: float) -> None:
        new_adj = OutgoingDict(lambda: IncomingDict(new_weight))
        new_adj.update(self._adj)
        for incomingDict in new_adj.values():
            incomingDict.set_default_value(new_weight)

        self._adj = new_adj
        self._default_edge_weight = new_weight





class IncomingDict(dict):
    """
    Custom class similar to defaultdict except it doesn't have a default_factory function
    but a default value. Also it doesn't expand the dictionary when using __getitem__ for 
    nonexistent keys.
    """
    __slots__ = "_default_value"

    def __init__(self, def_value):
        super().__init__()
        self._default_value = def_value


    def __getitem__(self, __key: Any) -> Any:
        try:
            return super().__getitem__(__key)
        except KeyError:            
            return self._default_value  

    def __contains__(self, __key: object) -> bool:
        return __key in self.keys()


    def set_default_value(self, new_value: float) -> None:
        self._default_value = new_value

    def get_default_value(self) -> float:
        return self._default_value


class OutgoingDict(defaultdict):
    pass    