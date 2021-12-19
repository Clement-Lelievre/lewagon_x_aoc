import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from day15 import dijkstra


def test_example():
    # EXAMPLE = """1163751742
    # 1381373672
    # 2136511328
    # 3694931569
    # 7463417111
    # 1319128137
    # 1359912421
    # 3125421639
    # 1293138521
    # 2311944581"""
    assert dijkstra() == 40