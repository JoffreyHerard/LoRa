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
		filename=str(current_degree_IN)+"-"+str(current_degree_GW)+"/1"
		if (len(os.listdir(filename)) != 100 ):
			print("ERROR ON "+filename)
			#sys.exit(0)
		filename=str(current_degree_IN)+"-"+str(current_degree_GW)+"/2"
		if (len(os.listdir(filename)) !=100):
			print("ERROR ON "+filename)
			#sys.exit(0)
		filename=str(current_degree_IN)+"-"+str(current_degree_GW)+"/10"
		if (len(os.listdir(filename)) != 100):
			print("ERROR ON "+filename)
			#sys.exit(0)
		filename=str(current_degree_IN)+"-"+str(current_degree_GW)+"/24"
		if (len(os.listdir(filename))!= 100):
			print("ERROR ON "+filename)
			#sys.exit(0)
		filename=str(current_degree_IN)+"-"+str(current_degree_GW)+"/N1"
		if (len(os.listdir(filename)) !=100):
			print("ERROR ON "+filename)
			#sys.exit(0)
		filename=str(current_degree_IN)+"-"+str(current_degree_GW)+"/N2"
		if (len(os.listdir(filename)) !=100):
			print("ERROR ON "+filename)
			#sys.exit(0)
		filename=str(current_degree_IN)+"-"+str(current_degree_GW)+"/N10"
		if (len(os.listdir(filename))!= 100):
			print("ERROR ON "+filename)
			#sys.exit(0)
		filename=str(current_degree_IN)+"-"+str(current_degree_GW)+"/N24"
		if (len(os.listdir(filename)) !=100):
			print("ERROR ON "+filename)
			#sys.exit(0)
		current_degree_GW=current_degree_GW+1
	current_degree_GW=1
	current_degree_IN=current_degree_IN+1