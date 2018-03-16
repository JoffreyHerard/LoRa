def pairing_phase(msg):
    global slot
    global idRegistered
    #print("PAIRING PHASE WITH "+str(msg.id_src)+" STARTED")
    s.send('Accept,'+str(2)+','+
    	str(frequency)+','+str(slot)+
    	','+str(id)+','+str(msg.id_src)+
    	','+str(-1)+','+str(slot))
    idRegistered.append(msg.id_src)
    #print("PAIRING PHASE WITH "+str(msg.id_src)+" ENDED")