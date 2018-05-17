#!/bin/bash
#location des fichiers omnetpp.ini et ned
#/Users/joffreyherard/Documents/Master_2/Projet_fin_etude/igraph/grapheCampagneSimulation/graphe/ 
#/Users/joffreyherard/Documents/Master_2/Projet_fin_etude/igraph/grapheCampagneSimulation/omnetppini/ 

#fichier ned de destination 
#/Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/simulations/lora.ned
#fichier ini de destination 
#/Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
current_degree_IN=1
current_degree_GW=1

IN="_IN_"
GW="_GW_"
msg1="-1MSG.ini"
msg2="-2MSG.ini"
msg10="-10MSG.ini"
msg24="-24MSG.ini"
NA="-NA"
#!/bin/bash
for current_degree_IN in {1..4}
do
	#echo "IN: $current_degree_IN"
   	for current_degree_GW in {1..4}
	do
		#echo " GW: $current_degree_GW"
  		for current_graph in 0
  		do
  			echo "--------------Current graph--------------> graphe$current_graph$IN$current_degree_IN$GW$current_degree_GW.ned"
  		 	fichier_ned="graphe$current_graph$IN$current_degree_IN$GW$current_degree_GW.ned"

  		 	fichier="graphe$current_graph$IN$current_degree_IN$GW$current_degree_GW"

  		 	fichier_config_1_msg="$fichier$msg1"
  		 	fichier_config_2_msg="$fichier$msg2"
  		 	fichier_config_10_msg="$fichier$msg10"
  		 	fichier_config_24_msg="$fichier$msg24"
  		 	fichier_config_NA_1_msg="$fichier$NA$msg1"
  		 	fichier_config_NA_2_msg="$fichier$NA$msg2"
  		 	fichier_config_NA_10_msg="$fichier$NA$msg10"
  		 	fichier_config_NA_24_msg="$fichier$NA$msg24"

  		 	#préparation des changements
  		 	rm /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/simulations/lora.ned
  		 	#mise en place du graphe 
  		 	cp /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/igraph/grapheCampagneSimulation/graphe/$fichier_ned /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/simulations/lora.ned
  		 	#mise en place du fichier ini
  		 	rm /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
  		 	echo "--------------Current .ini --------------> $fichier_config_1_msg"
  		 	#mise en place du .ini 
  		 	cp /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/igraph/grapheCampagneSimulation/omnetppini/$fichier_config_1_msg /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
  		 	src/LoRa  -m -u Cmdenv -n src:simulations omnetpp.ini
  		 	echo "Fin du run avec $fichier_config_1_msg"
  		 	sleep 2
  		 	#préparation des changements
  		 	rm /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
			echo "--------------Current .ini -------------->  $fichier_config_2_msg"
  		 	#mise en place du .ini 
  		 	cp /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/igraph/grapheCampagneSimulation/omnetppini/$fichier_config_2_msg /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
  		 	src/LoRa  -m -u Cmdenv -n src:simulations omnetpp.ini
  		 	echo "Fin du run avec $fichier_config_2_msg"
  		 	sleep 2
  		 	#préparation des changements
  		 	rm /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
			echo "--------------Current .ini -------------->  $fichier_config_10_msg"
  		 	#mise en place du .ini 
  		 	cp /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/igraph/grapheCampagneSimulation/omnetppini/$fichier_config_10_msg /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
  		 	src/LoRa  -m -u Cmdenv -n src:simulations omnetpp.ini
  		 	echo "Fin du run avec $fichier_config_10_msg"
  		 	sleep 2
  		 	#préparation des changements
  		 	rm /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
			echo "--------------Current .ini -------------->  $fichier_config_24_msg"
  		 	#mise en place du .ini 
  		 	cp /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/igraph/grapheCampagneSimulation/omnetppini/$fichier_config_24_msg /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
  		 	src/LoRa  -m -u Cmdenv -n src:simulations omnetpp.ini

  		 	echo "Fin du run avec $fichier_config_24_msg"
  		 	sleep 2
  		 	#préparation des changements
  		 	rm /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
			echo "--------------Current .ini -------------->  $fichier_config_NA_1_msg"
  		 	#mise en place du .ini 
  		 	cp /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/igraph/grapheCampagneSimulation/omnetppini/$fichier_config_NA_1_msg /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
			src/LoRa  -m -u Cmdenv -n src:simulations omnetpp.ini
  		 	echo "Fin du run avec $fichier_config_NA_1_msg"
  		 	sleep 2
  		 	#préparation des changements
  		 	rm /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
			echo "--------------Current .ini -------------->  $fichier_config_NA_2_msg"
  		 	#mise en place du .ini 
  		 	cp /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/igraph/grapheCampagneSimulation/omnetppini/$fichier_config_NA_2_msg /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
  		 	src/LoRa  -m -u Cmdenv -n src:simulations omnetpp.ini
  		 	echo "Fin du run avec $fichier_config_NA_2_msg"
  		 	sleep 2
  		 	#préparation des changements
  		 	rm /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
			echo "--------------Current .ini -------------->  $fichier_config_NA_10_msg"
  		 	#mise en place du .ini 
  		 	cp /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/igraph/grapheCampagneSimulation/omnetppini/$fichier_config_NA_10_msg /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
  		 	src/LoRa  -m -u Cmdenv -n src:simulations omnetpp.ini
  		 	echo "Fin du run avec $fichier_config_NA_10_msg"
  		 	sleep 2
  		 	#préparation des changements
  		 	rm /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
			echo "--------------Current .ini -------------->  $fichier_config_NA_24_msg"
  		 	#mise en place du .ini 
  		 	cp /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/igraph/grapheCampagneSimulation/omnetppini/$fichier_config_NA_24_msg /Users/joffreyherard/Documents/Master_2/Projet_fin_etude/dev/src/omnetpp.ini
  		 	src/LoRa  -m -u Cmdenv -n src:simulations omnetpp.ini
  		 	echo "Fin du run avec $fichier_config_NA_24_msg"
  		 	sleep 2
  		done
	done
done