


from _collections_abc import dict_items, dict_keys, dict_values
from typing import Any, List, Hashable, Union
from collections import defaultdict, Callable, namedtuple


class Graph:
    """Implementacija usmjerenog grafa gdje svaki vertex sadrzi kolekiju susjednih."""
    __slots__ = "_adj", "_vertices"

    class Edge(namedtuple("Edge", "outgoing incoming value")):
        pass
    class InvalidVertexException(Exception):
        pass

    def __init__(self, vertices: List[Hashable], default_weight: float = 0) -> None:
        self._adj = OutgoingDict(lambda: IncomingDict(default_weight))    # {  v0:{v2:weight},   v1:{v0:weight},  v2:{v1:weight, v0:weight}  }
        self._vertices = set(vertices)   #only to know if the vertex exists when asigning a new edge value


    #only call if you really have to
    def change_default_weight(self, new_weight: float) -> None:
        new_adj = OutgoingDict(lambda: IncomingDict(new_weight))
        new_adj.update(self._adj)
        for incomingDict in new_adj.values():
            incomingDict.set_default_value(new_weight)

        self._adj = new_adj

        

    def _validate_vertex(self, v) -> Union[None, 'Graph.InvalidVertexException']:
        if v in self._vertices:
            return
        raise self.InvalidVertexException()
    
    def vertex_count(self) -> int:
        return len(self.vertices())
        return len(self._vertices)

    def vertices(self) -> list:
        return list(self._vertices)


    def edge_count(self) -> int:
        return sum([len(x) for x in self._adj.values()])

    def edges(self) -> List['Graph.Edge']:
        return [ 
                self.Edge(outgoing, incoming, value)
                for outgoing, incoming_dict in self._adj.items()
                for incoming, value in incoming_dict.items()
               ]


    def get_edge(self, u, v) -> Union[float, 'Graph.InvalidVertexException']:
        self._validate_vertex(u)
        self._validate_vertex(v)        
        return self._adj[u][v]


    def insert_vertex(self, v: Hashable) -> Union[None, 'Graph.InvalidVertexException']:
        self._validate_vertex(v)
        self._vertices.add(v)

    def insert_edge(self, u, v, w: float) -> Union[None, 'Graph.InvalidVertexException']:
        self._validate_vertex(u)
        self._validate_vertex(v) #TODO: don't let the old value be overwritten
        self._adj[u][v] = w

    def remove_vertex(self, v) -> Union[None, 'Graph.InvalidVertexException']:
        ...

    def remove_edge(self, u, v) -> Union[None, 'Graph.InvalidVertexException']:
        ...


    def degree(self, v, outgoing = True) -> int:
        return len(self.incident_edges(v, outgoing))        


    def incident_edges(self, v, outgoing = True) -> List['Graph.Edge']:  #TODO: finish
        self._validate_vertex(v)
        if outgoing is True:
            return [ self.Edge(v, u, w) for u, w in self._adj[v].items() ]
        
        ... #TODO: find out the default value of incoming dict or add the field to Graph

        return [ self.Edge(u, v, u[v]) for u in self._adj.keys() 
                if self._adj[u][v] != ... ]









class IncomingDict(dict):
    def __init__(self, def_value):
        super().__init__()
        self._default_value = def_value


    def __getitem__(self, __key: Any) -> Any:
        try:
            return super().__getitem__(__key)
        except KeyError:            
            return self._default_value
        

    def set_default_value(self, new_value: float) -> None:
        self._default_value = new_value

    def get_default_value(self) -> float:
        return self._default_value


class OutgoingDict(defaultdict):
    pass    
    
    
        
    
    

    # def __repr__(self) -> str:
    #     return f'GraphDict({super().__repr__()})'



def main():
    g = Graph()
    g._adj['aki']['ana'] = 3
    print(g._adj[1])
    print(g._adj[1][2])
    g._adj[1][3] = 'aki'
    print(g._adj)
    print(g._adj[1][2])
    print(g._adj)
    print(g._adj['aki']['ana'])
    



if __name__ == "__main__":
    main()
#     def _validate_vertex(self, v):
# if not isinstance(v, self.Vertex):
# raise TypeError('Vertex expected')
# if v not in self._outgoing:
# raise ValueError('Vertex does not belong to this graph.')
# def is_directed(self):
# return self._incoming is not self._outgoing
# def vertex_count(self):
# return len(self._outgoing)
# def vertices(self):
# return self._outgoing.keys()
# def edge_count(self):
# total = sum(len(self._outgoing[v]) for v in self._outgoing)
# return total if self.is_directed() else total // 2
# def edges(self):
# result = set() # avoid double-reporting edges of undirected graph
# for secondary_map in self._outgoing.values():
# result.update(secondary_map.values()) # add edges to resulting set
# return result
# def get_edge(self, u, v):
# self._validate_vertex(u)
# self._validate_vertex(v)
# return self._outgoing[u].get(v) # returns None if v not adjacent
# def degree(self, v, outgoing=True):
# self._validate_vertex(v)
# adj = self._outgoing if outgoing else self._incoming
# return len(adj[v])

# def incident_edges(self, v, outgoing=True):
# self._validate_vertex(v)
# adj = self._outgoing if outgoing else self._incoming
# for edge in adj[v].values():
# yield edge
# def insert_vertex(self, x=None):
# v = self.Vertex(x)
# self._outgoing[v] = {}
# if self.is_directed():
# self._incoming[v] = {} # need distinct map for incoming edges
# return v
# def insert_edge(self, u, v, x=None):
# if self.get_edge(u, v) is not None: # includes error checking
# raise ValueError('u and v are already adjacent')
# e = self.Edge(u, v, x)
# self._outgoing[u][v] = e
# self._incoming[v][u] = e