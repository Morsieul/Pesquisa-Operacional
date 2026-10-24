from collections.abc import Sequence
from typing import Hashable

from graph.directed_weighted_graph import DirectedWeightedGraph

Vertex = Hashable
Arc = tuple[Vertex, Vertex]


def validate_hamiltonian_path(
    graph: DirectedWeightedGraph,
    arcs: Sequence[Arc],
    source: Vertex = 1,
    destination: Vertex | None = None,
) -> tuple[bool, str]:
    """
    Verifica se `arcs` descreve um caminho Hamiltoniano válido.

    Por padrão, a origem é o vértice 1 e o destino é o vértice n,
    assumindo vértices inteiros numerados de 1 a n.

    Retorna (válido, motivo). A função valida a sequência, não procura
    um caminho nem minimiza seu custo.
    """
    n = len(graph)

    if destination is None:
        destination = n

    if n < 2:
        return False, "O grafo precisa ter pelo menos dois vértices."

    if source == destination:
        return False, "A origem e o destino devem ser diferentes."

    if not graph.has_vertex(source):
        return False, f"A origem {source!r} não existe no grafo."

    if not graph.has_vertex(destination):
        return False, f"O destino {destination!r} não existe no grafo."

    if len(arcs) != n - 1:
        return False, (
            f"Quantidade incorreta de arcos: esperado {n - 1}, "
            f"recebido {len(arcs)}."
        )

    visited = [source]
    current = source

    for index, arc in enumerate(arcs, start=1):
        if not isinstance(arc, (tuple, list)) or len(arc) != 2:
            return False, f"O item {index} não é um arco (origem, destino)."

        origin, next_vertex = arc

        if origin != current:
            return False, (
                f"Sequência desconexa no arco {index}: "
                f"esperava saída de {current!r}, recebeu {origin!r}."
            )

        if not graph.has_arc(origin, next_vertex):
            return False, f"O arco ({origin!r}, {next_vertex!r}) não existe."

        if next_vertex in visited:
            return False, f"O vértice {next_vertex!r} foi visitado mais de uma vez."

        # Não podemos chegar ao destino antes do último arco.
        if next_vertex == destination and index != len(arcs):
            return False, "O destino foi alcançado antes do fim da sequência."

        visited.append(next_vertex)
        current = next_vertex

    if current != destination:
        return False, (
            f"O caminho termina em {current!r}, mas deveria terminar "
            f"em {destination!r}."
        )

    if len(visited) != n or set(visited) != graph.vertices:
        missing = graph.vertices - set(visited)
        return False, f"O caminho não visita todos os vértices. Faltando: {missing}."

    return True, "Caminho Hamiltoniano válido."
