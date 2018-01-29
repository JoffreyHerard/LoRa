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

if(len(sys.argv) ==6):

	#Getting numbers of LoRaWAN gateways and LoRagateways and Isolated nodes
	nb_LWGW = int(sys.argv[1])
	nb_LGW = int(sys.argv[2])
	nb_IN = int(sys.argv[3])
	lower_bound= int(sys.argv[4])
	upper_bound= int(sys.argv[5])
	#nb_LWGW = 1
	#nb_LGW = 3
	#nb_IN = 6

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
	fic.write("\t submodules:\n");
	fic.write("\t\t LWGW["+str(nb_LWGW)+"]: LWGW; \n");
	fic.write("\t\t LGW["+str(nb_LGW)+"]: LGW; \n");
	fic.write("\t\t IN["+str(nb_IN)+"]: IsoN; \n");
	fic.write("\t connections:\n");
	for l in g.get_edgelist():
		#we have to know if the node l[0] & l[1] is a LWGW or a LGW or a IN.
		if (l[0] <nb_LWGW and l[0]>=0):
			#It's a LoRaWANGATEWAY
			nomSommet0="LWGW"
			num_sommet0=l[0] 
		elif (l[0] <nb_LGW+1 and  l[0]>=nb_LWGW):
			nomSommet0="LGW"
			num_sommet0=l[0]-nb_LWGW
		elif (l[0] <nbVertex+1 and  l[0]>=nb_LGW):	
			nomSommet0="IN"
			num_sommet0=l[0]-nb_LGW-1
			if num_sommet0 ==6:
				print "toto"
			

		if(l[1] <nb_LWGW and l[1]>=0):
			#It's a LoRaWANGATEWAY
			nomSommet1="LWGW"
			num_sommet1=l[1]
		elif (l[1] <nb_LGW+1 and  l[1]>=nb_LWGW):
			nomSommet1="LGW"
			num_sommet1=l[1]-nb_LWGW
		elif (l[1] <nbVertex+1 and  l[1]>=nb_LGW):	
			nomSommet1="IN"
			num_sommet1=l[1]-nb_LGW-1
			if num_sommet1 ==6:
				print "toto"


		#Writing into the file
		delay1=random.randint(lower_bound,upper_bound)
		delay2=random.randint(lower_bound,upper_bound)

		fic.write("\t\t\t" + ""+nomSommet0+"["+str(num_sommet0)+"].channelsO++" + " --> " +"{delay="+str(delay1)+"ms;}" + " --> " +""+nomSommet1+"["+str(num_sommet1)+"].channelsI++" + ";\n")
		fic.write("\t\t\t" + ""+nomSommet0+"["+str(num_sommet0)+"].channelsI++" + " <-- " +"{delay="+str(delay2)+"ms;}" + " <-- " +  ""+nomSommet1+"["+str(num_sommet1)+"].channelsO++" + ";\n")

	fic.write("}")
	fic.close()

	#Writing .dot file #Graphviz
	g.write_dot("loraGraph.dot")
else:
	print "6 arguments is needed, the right way to use this python script is :\n"
	print "python loraGraph.py <NUMBER_LORAWANGATEWAY> <NUMBER_LORAGATEWAY> <NUMBER_ISOLATED_NODES> <LOWER BOUND> <UPPER BOUND>"