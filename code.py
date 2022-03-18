import json

import pandas as pd 

import networkx as nx

import matplotlib.pyplot as plt

from pyvis import network as net

arquivo = open('/clientes.json', 'r')

arq = arquivo.read()

arquivo.close()

train = json.loads(arq)

G = nx.DiGraph()

for i,elem in enumerate(train):

      dicionario = train[i]

      valores = list(dicionario.values())

      chaves = list(dicionario.keys())

      G.add_node(valores[0], color = "#f8db4fff")

      for j,elemm in enumerate(chaves):

        G.nodes[valores[0]][chaves[j]] = valores[j]

        if j == 0:

          G.nodes[valores[0]]['title'] = str(str(chaves[j])+':'+str(valores[j])+'</br>')

        else:

            G.nodes[valores[0]]['title'] = str(str(G.nodes[valores[0]]['title']) + str(chaves[j])+':'+str(valores[j])+'</br>')

arquivo = open('/movimentacoes.json', 'r')

arq = arquivo.read()

arquivo.close()

train = json.loads(arq)

for i,elem in enumerate(train):

      dicionario = train[i]

      valores = list(dicionario.values())

      chaves = list(dicionario.keys())

      valores[2] = valores[2].replace(",",".") 

      aux = "{} : {}".format(chaves[2] ,float(valores[2]))

      G.add_edge(int(valores[0]),int(valores[1]),attr_dict = aux,title = str(aux),color = "white")

nt = net.Network(height='750px', width='100%', bgcolor="black", font_color="#f8db4fff", directed= True)       

g = nt.from_nx(G)

nt.show("ex.html")
