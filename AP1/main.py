from graph.directed_weighted_graph import DirectedWeightedGraph
from services.path_validator import validate_hamiltonian_path


def build_example_graph() -> DirectedWeightedGraph:
    graph = DirectedWeightedGraph()

    # Exemplo com vértices 1, 2, 3, 4.
    arcs = [
        (1, 2, 4),
        (1, 3, 2),
        (2, 3, 5),
        (2, 4, 7),
        (3, 2, 1),
        (3, 4, 3),
    ]

    for origin, destination, cost in arcs:
        graph.add_arc(origin, destination, cost)

    return graph


def main() -> None:
    graph = build_example_graph()

    # Cada item representa um arco direcionado (origem, destino).
    candidate_path = [(1, 2), (2, 3), (3, 4)]

    valid, message = validate_hamiltonian_path(graph, candidate_path)

    print(f"Arcos informados: {candidate_path}")
    print(f"Válido: {'sim' if valid else 'não'}")
    print(f"Motivo: {message}")

    if valid:
        total_cost = sum(graph.arc_cost(u, v) for u, v in candidate_path)
        print(f"Custo total do caminho: {total_cost}")


if __name__ == "__main__":
    main()
