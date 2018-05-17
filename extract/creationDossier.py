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
		filename=str(current_degree_IN)+"-"+str(current_degree_GW)
		if not os.path.exists(filename):
			os.makedirs(filename)
			directory1=filename+"/1"
			if not os.path.exists(directory1):
				os.makedirs(directory1)
			directory2=filename+"/2"
			if not os.path.exists(directory2):
				os.makedirs(directory2)
			directory10=filename+"/10"
			if not os.path.exists(directory10):
				os.makedirs(directory10)
			directory24=filename+"/24"
			if not os.path.exists(directory24):
				os.makedirs(directory24)
			directoryN1=filename+"/N1"
			if not os.path.exists(directoryN1):
				os.makedirs(directoryN1)
			directoryN2=filename+"/N2"
			if not os.path.exists(directoryN2):
				os.makedirs(directoryN2)
			directoryN10=filename+"/N10"
			if not os.path.exists(directoryN10):
				os.makedirs(directoryN10)
			directoryN24=filename+"/N24"
			if not os.path.exists(directoryN24):
				os.makedirs(directoryN24)
		current_degree_GW=current_degree_GW+1
	current_degree_GW=1
	current_degree_IN=current_degree_IN+1
