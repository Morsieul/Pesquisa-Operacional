from __future__ import annotations

from typing import Hashable, Iterable

Vertex = Hashable


class DirectedWeightedGraph:
    """Grafo direcionado e ponderado, representado por lista de adjacência."""

    def __init__(self) -> None:
        self._adjacency: dict[Vertex, dict[Vertex, float]] = {}

    @property
    def vertices(self) -> set[Vertex]:
        return set(self._adjacency)

    def add_vertex(self, vertex: Vertex) -> None:
        self._adjacency.setdefault(vertex, {})

    def add_arc(self, origin: Vertex, destination: Vertex, cost: float = 1) -> None:
        """Adiciona o arco origin -> destination com seu custo."""
        self.add_vertex(origin)
        self.add_vertex(destination)
        self._adjacency[origin][destination] = cost

    def has_vertex(self, vertex: Vertex) -> bool:
        return vertex in self._adjacency

    def has_arc(self, origin: Vertex, destination: Vertex) -> bool:
        return (
            origin in self._adjacency
            and destination in self._adjacency[origin]
        )

    def arc_cost(self, origin: Vertex, destination: Vertex) -> float:
        """Retorna o custo do arco; lança KeyError se ele não existir."""
        return self._adjacency[origin][destination]

    def neighbors(self, vertex: Vertex) -> Iterable[Vertex]:
        return self._adjacency[vertex].keys()

    def __len__(self) -> int:
        return len(self._adjacency)
