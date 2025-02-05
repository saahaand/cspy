from networkx import DiGraph
from numpy import array

from cspy.algorithms.grasp import GRASP

from utils import TestingBase


class TestsGRASP(TestingBase):
    """
    Tests for finding the resource constrained shortest
    path of simple DiGraph using the GRASP algorithm.
    """

    def setUp(self):
        self.max_res, self.min_res = [5, 5], [0, 0]

        # Create digraph with a resource infeasible minimum cost path
        self.G = DiGraph(directed=True, n_res=2)
        self.G.add_edge('Source', 'A', res_cost=array([1, 1]), weight=1)
        self.G.add_edge('Source', 'B', res_cost=array([1, 1]), weight=1)
        # Resource infeasible edge
        self.G.add_edge('Source', 'C', res_cost=array([10, 1]), weight=10)
        self.G.add_edge('A', 'C', res_cost=array([1, 1]), weight=1)
        # Resource infeasible edge
        self.G.add_edge('A', 'E', res_cost=array([10, 1]), weight=10)
        # Resource infeasible edge
        self.G.add_edge('A', 'F', res_cost=array([10, 1]), weight=10)
        self.G.add_edge('B', 'C', res_cost=array([2, 1]), weight=-1)
        # Resource infeasible edge
        self.G.add_edge('B', 'F', res_cost=array([10, 1]), weight=10)
        # Resource infeasible edge
        self.G.add_edge('B', 'E', res_cost=array([10, 1]), weight=10)
        self.G.add_edge('C', 'D', res_cost=array([1, 1]), weight=-1)
        self.G.add_edge('D', 'E', res_cost=array([1, 1]), weight=1)
        self.G.add_edge('D', 'F', res_cost=array([1, 1]), weight=1)
        # Resource infeasible edge
        self.G.add_edge('D', 'Sink', res_cost=array([10, 10]), weight=10)
        # Resource infeasible edge
        self.G.add_edge('F', 'Sink', res_cost=array([10, 1]), weight=1)
        self.G.add_edge('E', 'Sink', res_cost=array([1, 1]), weight=1)

        self.result_path = ['Source', 'A', 'C', 'D', 'E', 'Sink']
        self.total_cost = 3
        self.consumed_resources = [5, 5]

    def test(self):
        alg = GRASP(self.G,
                    self.max_res,
                    self.min_res,
                    max_iter=50,
                    max_localiter=10)
        alg.run()
        self.check_result(alg, self.result_path, self.total_cost,
                          self.consumed_resources)

    def test_input_exceptions(self):
        # Check whether wrong input raises exceptions
        self.assertRaises(Exception, GRASP, self.G, 'x', [1, 'foo'],
                          'maxnumber')


if __name__ == '__main__':
    unittest.main()
