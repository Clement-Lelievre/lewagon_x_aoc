import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from day15 import dijkstra, customGraph, map_example


def test_example():
    graph = customGraph
    assert dijkstra(graph ,'00')[str(len(map_example)-1) + str(len(map_example[0])-1)] == 40