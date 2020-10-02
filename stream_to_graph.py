"""
    Transform a stream in a time-directed graph
    Author: Tiphaine Viard

"""
import sys


filepath = sys.argv[1]
last_time = {}
nodes = set()
int_nodes = {}
edges = []
CPT = 0

with open(filepath) as fp:
    for line in fp:
        contents = line.split(" ")
        u = int(contents[0])
        v = int(contents[1])
        t = int(contents[2])

        assert u != v

        if u not in last_time:
            last_time[u] = t
        if v not in last_time:
            last_time[v] = t

        if (t, u) not in nodes:
            nodes.add((t, u))
            int_nodes[(t, u)] = CPT
            CPT += 1
        if (t, v) not in nodes:
            nodes.add((t, v))
            int_nodes[(t, v)] = CPT
            CPT += 1

        if last_time[u] != t:
            edges.append(frozenset([(last_time[u], u), (t, u)])) #  Use TimeNode
        if last_time[v] != t:
            edges.append(frozenset([(last_time[v], v), (t, v)])) #  Use TimeNode
        if u != v:
            edges.append(frozenset([(t, u), (t, v)])) #  Use TimeNode

for e in edges:
    t, u = list(e)[0]
    s, v = list(e)[1]
    print(int_nodes[(t, u)], int_nodes[(s, v)], sep="\t")
