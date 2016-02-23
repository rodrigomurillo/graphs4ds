from graph_tool.all import *
from numpy.random import random, randint
g = Graph()

g = load_graph("coposting_graph.graphml")
cap = g.edge_properties["capacity"]
rand_index = randint(g.num_vertices())
src, tgt = g.vertex(0), g.vertex(rand_index)
res = boykov_kolmogorov_max_flow(g, src, tgt, cap)
res.a = cap.a - res.a  # the actual flow
max_flow = sum(res[e] for e in tgt.in_edges())
print "> Maximum flow:", max_flow

points = random((g.num_vertices(), 2))
points[0] = [0, 0]
points[rand_index] = [1, 1]
gv, pos = triangulation(points, type="delaunay")

print "> Drawing graph.."
graph_draw(gv, pos=pos, edge_pen_width=prop_to_size(res, mi=0, ma=3, power=1), \
        output="coposting-kolmogorov.pdf")
