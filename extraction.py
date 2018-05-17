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
			print("run :"+str(i)+" ->")
			current_graph_mean_msg_in=0.0
			current_graph_mean_msg_gw=0.0
			current_graph_mean_msg_well=0.0
			current_graph_mean_battery_in=0.0
			current_graph_mean_battery_gw=0.0
			#Resultat moyenne dans extract/X-X/1
			filename1="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-1MSG"
			dirs = os.listdir( "results/"+filename1)
			compteur_in=0
			compteur_gw=0
			compteur_well=0
			print(filename1)
			for file in dirs:
				if(file.startswith("IN")):
					with open("results/"+filename1+"/"+file) as f :
						current_graph_mean_msg_in=current_graph_mean_msg_in+int(f.readline())
						current_graph_mean_battery_in=current_graph_mean_battery_in+float(f.readline())
						f.close()
					compteur_in=compteur_in+1
				if(file.startswith("WGW")):
					with open("results/"+filename1+"/"+file) as f :
						current_graph_mean_msg_gw=current_graph_mean_msg_gw+int(f.readline())
						current_graph_mean_battery_gw=current_graph_mean_battery_gw+float(f.readline())
						f.close()
					compteur_gw=compteur_gw+1
				if(file.startswith("WELL")):
					with open("results/"+filename1+"/"+file) as f :
						current_graph_mean_msg_well=current_graph_mean_msg_well+int(f.readline())
						f.close()
					compteur_well=compteur_well+1
			if(compteur_in==0):
				current_graph_mean_msg_in=0
				current_graph_mean_battery_in=0
			else:
				current_graph_mean_msg_in=current_graph_mean_msg_in/compteur_in
				current_graph_mean_battery_in=current_graph_mean_battery_in/compteur_in
			if(compteur_gw ==0 ):
				current_graph_mean_msg_gw=0
				current_graph_mean_battery_gw=0
			else:
				current_graph_mean_msg_gw=current_graph_mean_msg_gw/compteur_gw
				current_graph_mean_battery_gw=current_graph_mean_battery_gw/compteur_gw
			if(compteur_well ==0):	
				current_graph_mean_msg_well=0
			else:
				current_graph_mean_msg_well=current_graph_mean_msg_well/compteur_well
			
			#fichier de sortie : extract/X-X/1
			fic=open("extract/"+str(current_degree_IN)+"-"+str(current_degree_GW)+"/1/"+str(i)+".dat","w")
			fic.write(str(current_graph_mean_msg_in)+"\n")
			fic.write(str(current_graph_mean_msg_gw)+"\n")
			fic.write(str(current_graph_mean_msg_well)+"\n")
			fic.write(str(current_graph_mean_battery_in)+"\n")
			fic.write(str(current_graph_mean_battery_gw)+"\n")
			fic.close()





			print("run :"+str(i)+" ->")
			current_graph_mean_msg_in=0.0
			current_graph_mean_msg_gw=0.0
			current_graph_mean_msg_well=0.0
			current_graph_mean_battery_in=0.0
			current_graph_mean_battery_gw=0.0
			#Resultat moyenne dans extract/X-X/1
			filename2="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-2MSG"
			dirs = os.listdir( "results/"+filename2)
			compteur_in=0
			compteur_gw=0
			compteur_well=0
			print(filename2)
			for file in dirs:
				if(file.startswith("IN")):
					with open("results/"+filename2+"/"+file) as f :
						current_graph_mean_msg_in=current_graph_mean_msg_in+int(f.readline())
						current_graph_mean_battery_in=current_graph_mean_battery_in+float(f.readline())
						f.close()
					compteur_in=compteur_in+1
				if(file.startswith("WGW")):
					with open("results/"+filename2+"/"+file) as f :
						current_graph_mean_msg_gw=current_graph_mean_msg_gw+int(f.readline())
						current_graph_mean_battery_gw=current_graph_mean_battery_gw+float(f.readline())
						f.close()
					compteur_gw=compteur_gw+1
				if(file.startswith("WELL")):
					with open("results/"+filename2+"/"+file) as f :
						current_graph_mean_msg_well=current_graph_mean_msg_well+int(f.readline())
						f.close()
					compteur_well=compteur_well+1
			if(compteur_in==0):
				current_graph_mean_msg_in=0
				current_graph_mean_battery_in=0
			else:
				current_graph_mean_msg_in=current_graph_mean_msg_in/compteur_in
				current_graph_mean_battery_in=current_graph_mean_battery_in/compteur_in
			if(compteur_gw ==0 ):
				current_graph_mean_msg_gw=0
				current_graph_mean_battery_gw=0
			else:
				current_graph_mean_msg_gw=current_graph_mean_msg_gw/compteur_gw
				current_graph_mean_battery_gw=current_graph_mean_battery_gw/compteur_gw
			if(compteur_well ==0):	
				current_graph_mean_msg_well=0
			else:
				current_graph_mean_msg_well=current_graph_mean_msg_well/compteur_well
			#fichier de sortie : extract/X-X/1
			fic=open("extract/"+str(current_degree_IN)+"-"+str(current_degree_GW)+"/2/"+str(i)+".dat","w")
			fic.write(str(current_graph_mean_msg_in)+"\n")
			fic.write(str(current_graph_mean_msg_gw)+"\n")
			fic.write(str(current_graph_mean_msg_well)+"\n")
			fic.write(str(current_graph_mean_battery_in)+"\n")
			fic.write(str(current_graph_mean_battery_gw)+"\n")
			fic.close()










			print("run :"+str(i)+" ->")
			current_graph_mean_msg_in=0.0
			current_graph_mean_msg_gw=0.0
			current_graph_mean_msg_well=0.0
			current_graph_mean_battery_in=0.0
			current_graph_mean_battery_gw=0.0
			#Resultat moyenne dans extract/X-X/1
			filename10="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-10MSG"
			dirs = os.listdir( "results/"+filename10)
			compteur_in=0
			compteur_gw=0
			compteur_well=0
			print(filename10)
			for file in dirs:
				if(file.startswith("IN")):
					with open("results/"+filename10+"/"+file) as f :
						current_graph_mean_msg_in=current_graph_mean_msg_in+int(f.readline())
						current_graph_mean_battery_in=current_graph_mean_battery_in+float(f.readline())
						f.close()
					compteur_in=compteur_in+1
				if(file.startswith("WGW")):
					with open("results/"+filename10+"/"+file) as f :
						current_graph_mean_msg_gw=current_graph_mean_msg_gw+int(f.readline())
						current_graph_mean_battery_gw=current_graph_mean_battery_gw+float(f.readline())
						f.close()
					compteur_gw=compteur_gw+1
				if(file.startswith("WELL")):
					with open("results/"+filename10+"/"+file) as f :
						current_graph_mean_msg_well=current_graph_mean_msg_well+int(f.readline())
						f.close()
					compteur_well=compteur_well+1
			if(compteur_in==0):
				current_graph_mean_msg_in=0
				current_graph_mean_battery_in=0
			else:
				current_graph_mean_msg_in=current_graph_mean_msg_in/compteur_in
				current_graph_mean_battery_in=current_graph_mean_battery_in/compteur_in
			if(compteur_gw ==0 ):
				current_graph_mean_msg_gw=0
				current_graph_mean_battery_gw=0
			else:
				current_graph_mean_msg_gw=current_graph_mean_msg_gw/compteur_gw
				current_graph_mean_battery_gw=current_graph_mean_battery_gw/compteur_gw
			if(compteur_well ==0):	
				current_graph_mean_msg_well=0
			else:
				current_graph_mean_msg_well=current_graph_mean_msg_well/compteur_well
			#fichier de sortie : extract/X-X/1
			fic=open("extract/"+str(current_degree_IN)+"-"+str(current_degree_GW)+"/10/"+str(i)+".dat","w")
			fic.write(str(current_graph_mean_msg_in)+"\n")
			fic.write(str(current_graph_mean_msg_gw)+"\n")
			fic.write(str(current_graph_mean_msg_well)+"\n")
			fic.write(str(current_graph_mean_battery_in)+"\n")
			fic.write(str(current_graph_mean_battery_gw)+"\n")
			fic.close()











			print("run :"+str(i)+" ->")
			current_graph_mean_msg_in=0.0
			current_graph_mean_msg_gw=0.0
			current_graph_mean_msg_well=0.0
			current_graph_mean_battery_in=0.0
			current_graph_mean_battery_gw=0.0
			#Resultat moyenne dans extract/X-X/1
			filename24="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-24MSG"
			dirs = os.listdir( "results/"+filename24)
			compteur_in=0
			compteur_gw=0
			compteur_well=0
			print(filename24)
			for file in dirs:
				if(file.startswith("IN")):
					with open("results/"+filename24+"/"+file) as f :
						current_graph_mean_msg_in=current_graph_mean_msg_in+int(f.readline())
						current_graph_mean_battery_in=current_graph_mean_battery_in+float(f.readline())
						f.close()
					compteur_in=compteur_in+1
				if(file.startswith("WGW")):
					with open("results/"+filename24+"/"+file) as f :
						current_graph_mean_msg_gw=current_graph_mean_msg_gw+int(f.readline())
						current_graph_mean_battery_gw=current_graph_mean_battery_gw+float(f.readline())
						f.close()
					compteur_gw=compteur_gw+1
				if(file.startswith("WELL")):
					with open("results/"+filename24+"/"+file) as f :
						current_graph_mean_msg_well=current_graph_mean_msg_well+int(f.readline())
						f.close()
					compteur_well=compteur_well+1
			if(compteur_in==0):
				current_graph_mean_msg_in=0
				current_graph_mean_battery_in=0
			else:
				current_graph_mean_msg_in=current_graph_mean_msg_in/compteur_in
				current_graph_mean_battery_in=current_graph_mean_battery_in/compteur_in
			if(compteur_gw ==0 ):
				current_graph_mean_msg_gw=0
				current_graph_mean_battery_gw=0
			else:
				current_graph_mean_msg_gw=current_graph_mean_msg_gw/compteur_gw
				current_graph_mean_battery_gw=current_graph_mean_battery_gw/compteur_gw
			if(compteur_well ==0):	
				current_graph_mean_msg_well=0
			else:
				current_graph_mean_msg_well=current_graph_mean_msg_well/compteur_well
			#fichier de sortie : extract/X-X/1
			fic=open("extract/"+str(current_degree_IN)+"-"+str(current_degree_GW)+"/24/"+str(i)+".dat","w")
			fic.write(str(current_graph_mean_msg_in)+"\n")
			fic.write(str(current_graph_mean_msg_gw)+"\n")
			fic.write(str(current_graph_mean_msg_well)+"\n")
			fic.write(str(current_graph_mean_battery_in)+"\n")
			fic.write(str(current_graph_mean_battery_gw)+"\n")
			fic.close()












			print("run :"+str(i)+" ->")
			current_graph_mean_msg_in=0.0
			current_graph_mean_msg_gw=0.0
			current_graph_mean_msg_well=0.0
			current_graph_mean_battery_in=0.0
			current_graph_mean_battery_gw=0.0
			#Resultat moyenne dans extract/X-X/1
			filenameN1="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-NA-1MSG"
			dirs = os.listdir( "results/"+filenameN1)
			compteur_in=0
			compteur_gw=0
			compteur_well=0
			print(filenameN1)
			for file in dirs:
				if(file.startswith("IN")):
					with open("results/"+filenameN1+"/"+file) as f :
						current_graph_mean_msg_in=current_graph_mean_msg_in+int(f.readline())
						current_graph_mean_battery_in=current_graph_mean_battery_in+float(f.readline())
						f.close()
					compteur_in=compteur_in+1
				if(file.startswith("WGW")):
					with open("results/"+filenameN1+"/"+file) as f :
						current_graph_mean_msg_gw=current_graph_mean_msg_gw+int(f.readline())
						current_graph_mean_battery_gw=current_graph_mean_battery_gw+float(f.readline())
						f.close()
					compteur_gw=compteur_gw+1
				if(file.startswith("WELL")):
					with open("results/"+filenameN1+"/"+file) as f :
						current_graph_mean_msg_well=current_graph_mean_msg_well+int(f.readline())
						f.close()
					compteur_well=compteur_well+1
			if(compteur_in==0):
				current_graph_mean_msg_in=0
				current_graph_mean_battery_in=0
			else:
				current_graph_mean_msg_in=current_graph_mean_msg_in/compteur_in
				current_graph_mean_battery_in=current_graph_mean_battery_in/compteur_in
			if(compteur_gw ==0 ):
				current_graph_mean_msg_gw=0
				current_graph_mean_battery_gw=0
			else:
				current_graph_mean_msg_gw=current_graph_mean_msg_gw/compteur_gw
				current_graph_mean_battery_gw=current_graph_mean_battery_gw/compteur_gw
			if(compteur_well ==0):	
				current_graph_mean_msg_well=0
			else:
				current_graph_mean_msg_well=current_graph_mean_msg_well/compteur_well
			#fichier de sortie : extract/X-X/1
			fic=open("extract/"+str(current_degree_IN)+"-"+str(current_degree_GW)+"/N1/"+str(i)+".dat","w")
			fic.write(str(current_graph_mean_msg_in)+"\n")
			fic.write(str(current_graph_mean_msg_gw)+"\n")
			fic.write(str(current_graph_mean_msg_well)+"\n")
			fic.write(str(current_graph_mean_battery_in)+"\n")
			fic.write(str(current_graph_mean_battery_gw)+"\n")
			fic.close()












			print("run :"+str(i)+" ->")
			current_graph_mean_msg_in=0.0
			current_graph_mean_msg_gw=0.0
			current_graph_mean_msg_well=0.0
			current_graph_mean_battery_in=0.0
			current_graph_mean_battery_gw=0.0
			#Resultat moyenne dans extract/X-X/1
			filenameN2="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-NA-2MSG"
			dirs = os.listdir( "results/"+filenameN2)
			compteur_in=0
			compteur_gw=0
			compteur_well=0
			print(filenameN2)
			for file in dirs:
				if(file.startswith("IN")):
					with open("results/"+filenameN2+"/"+file) as f :
						current_graph_mean_msg_in=current_graph_mean_msg_in+int(f.readline())
						current_graph_mean_battery_in=current_graph_mean_battery_in+float(f.readline())
						f.close()
					compteur_in=compteur_in+1
				if(file.startswith("WGW")):
					with open("results/"+filenameN2+"/"+file) as f :
						current_graph_mean_msg_gw=current_graph_mean_msg_gw+int(f.readline())
						current_graph_mean_battery_gw=current_graph_mean_battery_gw+float(f.readline())
						f.close()
					compteur_gw=compteur_gw+1
				if(file.startswith("WELL")):
					with open("results/"+filenameN2+"/"+file) as f :
						current_graph_mean_msg_well=current_graph_mean_msg_well+int(f.readline())
						f.close()
					compteur_well=compteur_well+1
			if(compteur_in==0):
				current_graph_mean_msg_in=0
				current_graph_mean_battery_in=0
			else:
				current_graph_mean_msg_in=current_graph_mean_msg_in/compteur_in
				current_graph_mean_battery_in=current_graph_mean_battery_in/compteur_in
			if(compteur_gw ==0 ):
				current_graph_mean_msg_gw=0
				current_graph_mean_battery_gw=0
			else:
				current_graph_mean_msg_gw=current_graph_mean_msg_gw/compteur_gw
				current_graph_mean_battery_gw=current_graph_mean_battery_gw/compteur_gw
			if(compteur_well ==0):	
				current_graph_mean_msg_well=0
			else:
				current_graph_mean_msg_well=current_graph_mean_msg_well/compteur_well
			#fichier de sortie : extract/X-X/1
			fic=open("extract/"+str(current_degree_IN)+"-"+str(current_degree_GW)+"/N2/"+str(i)+".dat","w")
			fic.write(str(current_graph_mean_msg_in)+"\n")
			fic.write(str(current_graph_mean_msg_gw)+"\n")
			fic.write(str(current_graph_mean_msg_well)+"\n")
			fic.write(str(current_graph_mean_battery_in)+"\n")
			fic.write(str(current_graph_mean_battery_gw)+"\n")
			fic.close()













			print("run :"+str(i)+" ->")
			current_graph_mean_msg_in=0.0
			current_graph_mean_msg_gw=0.0
			current_graph_mean_msg_well=0.0
			current_graph_mean_battery_in=0.0
			current_graph_mean_battery_gw=0.0
			#Resultat moyenne dans extract/X-X/1
			filenameN10="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-NA-10MSG"
			dirs = os.listdir( "results/"+filenameN10)
			compteur_in=0
			compteur_gw=0
			compteur_well=0
			print(filenameN10)
			for file in dirs:
				if(file.startswith("IN")):
					with open("results/"+filenameN10+"/"+file) as f :
						current_graph_mean_msg_in=current_graph_mean_msg_in+int(f.readline())
						current_graph_mean_battery_in=current_graph_mean_battery_in+float(f.readline())
						f.close()
					compteur_in=compteur_in+1
				if(file.startswith("WGW")):
					with open("results/"+filenameN10+"/"+file) as f :
						current_graph_mean_msg_gw=current_graph_mean_msg_gw+int(f.readline())
						current_graph_mean_battery_gw=current_graph_mean_battery_gw+float(f.readline())
						f.close()
					compteur_gw=compteur_gw+1
				if(file.startswith("WELL")):
					with open("results/"+filenameN10+"/"+file) as f :
						current_graph_mean_msg_well=current_graph_mean_msg_well+int(f.readline())
						f.close()
					compteur_well=compteur_well+1
			if(compteur_in==0):
				current_graph_mean_msg_in=0
				current_graph_mean_battery_in=0
			else:
				current_graph_mean_msg_in=current_graph_mean_msg_in/compteur_in
				current_graph_mean_battery_in=current_graph_mean_battery_in/compteur_in
			if(compteur_gw ==0 ):
				current_graph_mean_msg_gw=0
				current_graph_mean_battery_gw=0
			else:
				current_graph_mean_msg_gw=current_graph_mean_msg_gw/compteur_gw
				current_graph_mean_battery_gw=current_graph_mean_battery_gw/compteur_gw
			if(compteur_well ==0):	
				current_graph_mean_msg_well=0
			else:
				current_graph_mean_msg_well=current_graph_mean_msg_well/compteur_well
			#fichier de sortie : extract/X-X/1
			fic=open("extract/"+str(current_degree_IN)+"-"+str(current_degree_GW)+"/N10/"+str(i)+".dat","w")
			fic.write(str(current_graph_mean_msg_in)+"\n")
			fic.write(str(current_graph_mean_msg_gw)+"\n")
			fic.write(str(current_graph_mean_msg_well)+"\n")
			fic.write(str(current_graph_mean_battery_in)+"\n")
			fic.write(str(current_graph_mean_battery_gw)+"\n")
			fic.close()














			print("run :"+str(i)+" ->")
			current_graph_mean_msg_in=0.0
			current_graph_mean_msg_gw=0.0
			current_graph_mean_msg_well=0.0
			current_graph_mean_battery_in=0.0
			current_graph_mean_battery_gw=0.0
			#Resultat moyenne dans extract/X-X/1
			filenameN24="graphe"+str(i)+"_IN_"+str(current_degree_IN)+"_GW_"+str(current_degree_GW)+"-NA-24MSG"
			dirs = os.listdir( "results/"+filenameN24)
			compteur_in=0
			compteur_gw=0
			compteur_well=0
			print(filenameN24)
			for file in dirs:
				if(file.startswith("IN")):
					with open("results/"+filenameN24+"/"+file) as f :
						current_graph_mean_msg_in=current_graph_mean_msg_in+int(f.readline())
						current_graph_mean_battery_in=current_graph_mean_battery_in+float(f.readline())
						f.close()
					compteur_in=compteur_in+1
				if(file.startswith("WGW")):
					with open("results/"+filenameN24+"/"+file) as f :
						current_graph_mean_msg_gw=current_graph_mean_msg_gw+int(f.readline())
						current_graph_mean_battery_gw=current_graph_mean_battery_gw+float(f.readline())
						f.close()
					compteur_gw=compteur_gw+1
				if(file.startswith("WELL")):
					with open("results/"+filenameN24+"/"+file) as f :
						current_graph_mean_msg_well=current_graph_mean_msg_well+int(f.readline())
						f.close()
					compteur_well=compteur_well+1
			if(compteur_in==0):
				current_graph_mean_msg_in=0
				current_graph_mean_battery_in=0
			else:
				current_graph_mean_msg_in=current_graph_mean_msg_in/compteur_in
				current_graph_mean_battery_in=current_graph_mean_battery_in/compteur_in
			if(compteur_gw ==0 ):
				current_graph_mean_msg_gw=0
				current_graph_mean_battery_gw=0
			else:
				current_graph_mean_msg_gw=current_graph_mean_msg_gw/compteur_gw
				current_graph_mean_battery_gw=current_graph_mean_battery_gw/compteur_gw
			if(compteur_well ==0):	
				current_graph_mean_msg_well=0
			else:
				current_graph_mean_msg_well=current_graph_mean_msg_well/compteur_well
			#fichier de sortie : extract/X-X/1
			fic=open("extract/"+str(current_degree_IN)+"-"+str(current_degree_GW)+"/N24/"+str(i)+".dat","w")
			fic.write(str(current_graph_mean_msg_in)+"\n")
			fic.write(str(current_graph_mean_msg_gw)+"\n")
			fic.write(str(current_graph_mean_msg_well)+"\n")
			fic.write(str(current_graph_mean_battery_in)+"\n")
			fic.write(str(current_graph_mean_battery_gw)+"\n")
			fic.close()





			i=i+1
		current_degree_GW=current_degree_GW+1
	current_degree_GW=1
	current_degree_IN=current_degree_IN+1