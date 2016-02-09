#! /usr/bin/env python

from __future__ import division, absolute_import
import sys
range = xrange					# para tener una funcion range adecuada
import os
from pylab import *				# para graficar
from numpy.random import *		# para generar muestreos aleatorios
seed(42)
import time
# graph_tool
from graph_tool.all import *



# Graph class
class PageRank:
    def __init__(self, num_nodes=10000, damping_factor=0.85):
        # Empezamos con una grafica vacia
        self.load_graph()
        if not self.g:
            self.g = Graph()
            self.g.set_directed(True)
            # Creamos "property maps" para los vertices y las aristas
            self.v_age = self.g.new_vertex_property("int")
            self.page_rank = None
            self.custom_page_rank = self.g.new_vertex_property("float")

        # La cantidad de nodos de la red
        self.num_nodes = num_nodes

        # dumping factor
        self.damping_factor = damping_factor

        # lista de nodos
        self.vlist = None

    def create_graph(self):
        print "Armando grafo"
        stime = time.time()

        # Generamos un vertice
        v = self.g.add_vertex()
        self.v_age[v] = 0

        # Creamos una lista con los vertices que nos diga la cantidad de veces
        # que ha aparecido el vertice en una adicion, lo que se traduce en la
        # probabilidad que sea elegido para conectarse
        self.vlist = [v]

        for i in range(1, self.num_nodes):
            # creando los vertices
            v = self.g.add_vertex()
            self.v_age[v] = i

            # generamos una arista basandonos en una eleccion aleatoria de
            # un elemento en vlist
            i = randint(0, len(self.vlist))
            target = self.vlist[i]

            # agregamos la arista
            e = self.g.add_edge(v, target)

            # ponemos target y v en la lista. Asi la frecuencia de target
            # aumenta por haber sido elegido
            self.vlist.append(target)
            self.vlist.append(v)

        print "Grafo completo, tardamos", time.time()-stime

    def calculate_page_rank(self):
        self.page_rank = pagerank(self.g) ## Tenemos page rank!!!

        t = 60
        for vertex in self.g.vertices():
            self.custom_page_rank[vertex]=1/self.num_nodes

        for i in xrange(t):
            for v in self.g.vertices():
                temp_factor = 0.0
                for n in v.in_neighbours():
                    temp_factor += (self.custom_page_rank[n]/n.out_degree())
                self.custom_page_rank[v] = ((1-self.damping_factor)/self.num_nodes)+\
                    self.damping_factor*(temp_factor)

        for v in self.g.vertices():
            print "PageRanks: ",
            print "Graph-Tool Rank: ", self.page_rank[v],
            print "Custom Rank: ", self.custom_page_rank[v]

    def save_graph(self):
        # guardamos la grafica para escribir a un archivo
        g.vertex_properties["age"] = self.v_age		# hay que almacenar las propiedes en la grafica,
        g.vertex_properties["page_rank"] = self.custom_page_rank		# nuestro page rank
        g.save("price.xml.gz")					# escribiendo..

    def load_graph(self):
        try:
            self.g = load_graph("price.xml.gz")
            self.v_age = self.g.vertex_properties["age"]
        except:
            self.g = None
            pass

    def draw_graph(self):
        import numpy as np
        pos = sfdp_layout(self.g)
        ebet = betweenness(self.g)[1]
        ebet.a /= ebet.a.max() / 10.
        self.custom_page_rank.a = np.log(self.custom_page_rank.a * 10000)
        graph_draw(self.g, pos, output_size=(1000, 1000), vertex_color=[1,1,1,0],
               vertex_fill_color=self.custom_page_rank, edge_pen_width=ebet,
               vcmap=matplotlib.cm.gist_heat_r, output="page_rank.png")


if __name__=="__main__":
    pr = PageRank()
    pr.create_graph()
    pr.calculate_page_rank()
    pr.draw_graph()
