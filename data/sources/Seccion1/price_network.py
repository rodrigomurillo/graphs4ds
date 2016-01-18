#! /usr/bin/env python

from __future__ import division, absolute_import
import sys
range = xrange					# para tener una funcion range adecuada
import os
from pylab import *				# para graficar
from numpy.random import *		# para generar muestreos aleatorios
seed(42)

# graph_tool
from graph_tool.all import *

# Empezamos con una grafica vacia
g = Graph()
g.set_directed(False)
# Creamos "property maps" para los vertices y las aristas
v_age = g.new_vertex_property("int")
e_age = g.new_edge_property("int")

# La cantidad de nodos de la red
N = 100000

# Generamos un vertice
v = g.add_vertex()
v_age[v] = 0

# Creamos una lista con los vertices que nos diga la cantidad de veces
# que ha aparecido el vertice en una adicion, lo que se traduce en la
# probabilidad que sea elegido para conectarse 
vlist = [v]

for i in range(1, N):
    # creando los vertices
    v = g.add_vertex()
    v_age[v] = i

    # generamos una arista basandonos en una eleccion aleatoria de
	# un elemento en vlist
    i = randint(0, len(vlist))
    target = vlist[i]

    # agregamos la arista
    e = g.add_edge(v, target)
    e_age[e] = i

    # ponemos target y v en la lista. Asi la frecuencia de target
	# aumenta por haber sido elegido
    vlist.append(target)
    vlist.append(v)

# hagamos una caminata aleatoria sobre la red

v = g.vertex(randint(0, g.num_vertices()))
while True:
    print "vertex:", int(v), "degree:", v.out_degree(), "age:", v_age[v]

    if v.out_degree() < 0:
        print("No hay a donde mas ir :(")
        break

    n_list = []
    for w in v.out_neighbours():
        n_list.append(w)
    v = n_list[randint(0, len(n_list))]

# guardamos la grafica para escribir a un archivo

g.vertex_properties["age"] = v_age		# hay que almacenar las propiedes en la grafica,
g.edge_properties["age"] = e_age		# para que tambien se escriban
g.save("price.xml.gz")					# escribiendo..


# grafiquemos la distribucion de los grados
hist = vertex_hist(g,"out")

y = hist[0]
err = sqrt(hist[0])
err[err >= y] = y[err >= y] - 1e-2

figure(figsize=(6,4))
errorbar(hist[1][:-1], hist[0], fmt="o", yerr=err,
        label="grados")
gca().set_yscale("log")
gca().set_xscale("log")
gca().set_ylim(1e-1, 1e5)
gca().set_xlim(0.8, 1e3)
subplots_adjust(left=0.2, bottom=0.2)
xlabel("$k$")
ylabel("$NP(k)$")
tight_layout()
# savefig("price-deg-dist.pdf")
savefig("price-deg-dist.png")
######
raw_input("Presione ENTER para continuar..")
# Dibujando el grafo
g = load_graph("price.xml.gz")
age = g.vertex_properties["age"]

pos = sfdp_layout(g)
graph_draw(g, pos, output_size=(1000, 1000), vertex_color=[1,1,1,0],
           vertex_fill_color=age, vertex_size=1, edge_pen_width=1.2,
           vcmap=matplotlib.cm.gist_heat_r, output="price.png")


