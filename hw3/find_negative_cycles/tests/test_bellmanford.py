import unittest
from algo.find_negative_cycles import find_negative_cycles


class TestBellmanFord(unittest.TestCase):

    def test_bellman_ford(self):
        name_txt1 = '/Users/sunduo/Dijkstra.txt'
        ans1 = find_negative_cycles(name_txt1)
        assert ans1 == []
        name_txt2 = '/Users/sunduo/Bellman-ford.txt'
        ans2 = find_negative_cycles(name_txt2)
        assert ans2 == [5, 7, 8, 5]
