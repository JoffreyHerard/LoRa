import sys
import random
import os


#Getting numbers of LoRaWAN gateways and LoRagateways and Isolated nodes
max_degree_IN= 4
max_degree_GW= 4
nb_vertex= 1000
nb_graph=100
current_degree_IN=1
current_degree_GW=1
while current_degree_IN < max_degree_IN+1:
	while current_degree_GW < max_degree_GW+1:
		i = 0
		while i < nb_graph:
			filename="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-1MSG"
			if not os.path.exists(filename):
 				os.makedirs(filename)
			filename="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-2MSG"
			if not os.path.exists(filename):
 				os.makedirs(filename)
			filename="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-10MSG"
			if not os.path.exists(filename):
 				os.makedirs(filename)
			filename="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-24MSG"
			if not os.path.exists(filename):
 				os.makedirs(filename)
 			filename="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-NA-1MSG"
			if not os.path.exists(filename):
 				os.makedirs(filename)
			filename="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-NA-2MSG"
			if not os.path.exists(filename):
 				os.makedirs(filename)
			filename="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-NA-10MSG"
			if not os.path.exists(filename):
 				os.makedirs(filename)
			filename="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-NA-24MSG"
			if not os.path.exists(filename):
 				os.makedirs(filename)
			i=i+1
		current_degree_GW=current_degree_GW+1
	current_degree_GW=1
	current_degree_IN=current_degree_IN+1