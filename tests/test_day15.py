import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from day15 import dijkstra, Graph

EXAMPLE = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
map_example = [[int(char) for char in row] for row in EXAMPLE.split('\n')]


customGraph = Graph()

# adding nodes of the graph
for row in range(len(map_example)):
    for col in range(len(map_example[0])):
        customGraph.addNode(str(row)+str(col))

# adding edges: moves towards the right   
for row in range(len(map_example)):
    for col in range(len(map_example[0])-1):
            customGraph.addEdge(str(row)+str(col), str(row)+str(col+1) , map_example[row][col+1])
     
# adding edges: moves towards the bottom  
for row in range(len(map_example)-1):
    for col in range(len(map_example[0])):
            customGraph.addEdge(str(row)+str(col), str(row+1)+str(col) , map_example[row+1][col])

def test_example():
    assert dijkstra(customGraph ,'00')[str(len(map_example)-1) + str(len(map_example[0])-1)] == 40
    
