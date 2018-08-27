import unittest
from algo.find_shortest_path import find_shortest_path


class TestDijkstra(unittest.TestCase):

    def test_dijkstra(self):
        name_txt = '/Users/sunduo/Dijkstra.txt'
        start = 1.0
        end = 4.0
        path, dis = find_shortest_path(name_txt,start,end)
        assert (path, dis) == ([1.0, 2.0, 4.0], 7)

