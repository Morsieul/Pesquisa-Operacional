import unittest

from graph.directed_weighted_graph import DirectedWeightedGraph
from services.path_validator import validate_hamiltonian_path


def example_graph() -> DirectedWeightedGraph:
    graph = DirectedWeightedGraph()
    for u, v in [
        (1, 2), (1, 3),
        (2, 3), (2, 4),
        (3, 2), (3, 4),
        (4, 2),
    ]:
        graph.add_arc(u, v, 1)
    return graph


class TestHamiltonianPathValidator(unittest.TestCase):
    def setUp(self):
        self.graph = example_graph()

    def test_valid_path(self):
        self.assertTrue(
            validate_hamiltonian_path(
                self.graph, [(1, 2), (2, 3), (3, 4)]
            )[0]
        )

    def test_arc_does_not_exist(self):
        valid, _ = validate_hamiltonian_path(
            self.graph, [(1, 4), (4, 2), (2, 3)]
        )
        self.assertFalse(valid)

    def test_disconnected_sequence(self):
        valid, _ = validate_hamiltonian_path(
            self.graph, [(1, 2), (3, 4), (4, 2)]
        )
        self.assertFalse(valid)

    def test_repeated_vertex(self):
        valid, _ = validate_hamiltonian_path(
            self.graph, [(1, 2), (2, 3), (3, 2)]
        )
        self.assertFalse(valid)

    def test_wrong_destination(self):
        valid, _ = validate_hamiltonian_path(
            self.graph, [(1, 3), (3, 2), (2, 4)]
        )
        # O caminho termina em 4, então neste grafo ele é válido.
        self.assertTrue(valid)

    def test_wrong_number_of_arcs(self):
        valid, _ = validate_hamiltonian_path(
            self.graph, [(1, 2), (2, 4)]
        )
        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main()
