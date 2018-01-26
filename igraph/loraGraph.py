#! /usr/bin/python

from igraph import *
import sys
import random

#Random number is the probability which have a LoraGateway to have one isolated node 
p=random.random()
#Random number is the probability which have a LoraGateway to have another isolated node 
p2=random.random()
#Random number is the probability  have an Isolated Node to have a connection with another isolated node 
p3=random.random()


#Getting numbers of LoRaWAN gateways and LoRagateways and Isolated nodes
nb_LWGW = int(sys.argv[1])
nb_LGW = int(sys.argv[2])
nb_IN = int(sys.argv[3])
nbVertex=nb_LWGW+nb_LGW+nb_IN
#make the graph
g = Graph()
#Adding LoRaWAN, LGW, IN
g.add_vertices(nbVertex)

#First step and the second step are: Connecting the LoRagateways to the LoRaWAN and connecting LoRaGateways between her

for i in range(1,nb_LGW+1):
	g.add_edges([(0,i)])
	for j in range(1,nb_LGW+1):
		if (i != j and i>j):
			g.add_edges([(i,j)])

#Connecting the Isolated node to the LoRa gateway because an..
#.. Isolated node must have at less one LoRa gateway around
nb_IN_remaining=nb_IN
firtIN=nb_LWGW+nb_LGW
for j in range (nb_LGW+1,nbVertex):
		i=random.randint(nb_LWGW,nb_LGW)
		
		g.add_edges([(i,j)])

#Connecting another Isolated node to the LoRagateway because random is fun 
nb_IN_remaining=nb_IN
firtIN=nb_LWGW+nb_LGW
for j in range (nb_LGW+1,nbVertex):
	i=random.randint(nb_LWGW,nb_LGW)
	pj=random.random()
	if(pj<p2 and -1==g.get_eid(i, j, directed=False, error=False)):
		g.add_edges([(i,j)])

#Last step is consist in making neighborhood between the INs
for j in range (nb_IN,nbVertex-1):
	i=random.randint(nb_IN,nbVertex-1)
	pj=random.random()
	if(pj<p3 and i!=j and -1==g.get_eid(i, j, directed=False, error=False)):
		g.add_edges([(i,j)])
#Changing the name of each vertex
names=[]
names.append("LWGW")
for i in range(1,nb_LGW+1):
	names.append("LGW")
for j in range (nb_LGW+1,nbVertex):
	names.append("IN")


g.vs["label"] =names
g.es[0]
#Writing NED file like the sample provided
fic=open("randomGrapheLoRa.ned","a")
for l in g.get_edgelist():
    fic.write("\t\t\t" + "node["+str(l[0])+"].neigh++" + " <--> " + "node["+str(l[1])+"].neigh++" + ";\n")
fic.write("}")
fic.close()

#Writing .dot file #Graphviz
g.write_dot("loraGraph.dot")