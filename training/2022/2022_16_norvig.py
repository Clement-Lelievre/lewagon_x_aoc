import re
from typing import Dict, Tuple

INPUT = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


valve_data_pattern = re.compile("^Valve (\w+).*?(\d+).*?valves? (.*?)$", re.IGNORECASE)
valves = [row for v in INPUT.splitlines() if (row := v.strip())]
valve_dict = {}
for valve in valves:
    valve_name, valve_power, valve_connections = (
        (regex_search := valve_data_pattern.search(valve)).group(1),
        regex_search.group(2),
        tuple(map(str.strip, regex_search.group(3).split(","))),
    )
    valve_dict[valve_name] = {
        "flow rate": int(valve_power),
        "connections": valve_connections,
    }
# up to now I re used my own parsing the input
in16 = [(v, valve_dict[v]['flow rate'], valve_dict[v]['connections']) for v in valve_dict]

Costs = Dict[tuple, int] # {(room, room): travel_cost}
Flow  = Dict[str, int]   # {room: flow_rate}

def floyd(graph) -> Costs:
    """Floyd-Warshall algorithm for all-pairs shortest path.
    Returns dict of `{(u, v): cost_of_shortest_path}."""
    cost = {(u, v): (0 if u == v else 1 if v in graph[u] else float('inf')) 
            for u in graph for v in graph}
    for r in graph:
        for u in graph:
            for v in graph:
                cost[u, v] = min(cost[u, v], cost[u, r] + cost[r, v])
    return cost

def costs_and_flow(valves, start='AA') -> Tuple[Costs, Flow]:
    """Given the valves, return two dicts: (costs, flow)."""
    costs = floyd({v: neighbors for (v, _, neighbors) in valves})
    flow  = {v: flow for (v, flow, _) in valves if flow > 0 or v == start}
    return costs, flow
    
def valve_search(costs, flow, valve='AA', opened=set(), time_left=30) -> int:
    """Depth-first search for the most flow we can produce. Returns total flow."""
    if time_left < 0:
        return 0
    else:
        opened1 = opened | {valve}
        valves1 = set(flow) - opened1
        flow1   = flow[valve] * time_left
        flow2   = max((valve_search(costs, flow, v, opened1, time_left - costs[valve, v] - 1)
                      for v in valves1), default=0)
        return flow1 + flow2

print(valve_search(*costs_and_flow(in16)))