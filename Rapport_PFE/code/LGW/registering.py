def registering_phase(msg):
    global isRegistered
    global slot
    #print("REGISTERING PHASE WITH "+str(msg.id_src)+" STARTED")
    s.send('DataReq,'+str(2)+','+
    	str(frequency)+','+str(slot)+
    	','+str(id)+','+str(msg.id_src)+
    	','+str(-1)+','+str(slot))
    if msg.id_src in isRegistered:
        print("Added before")
    else:
        isRegistered.append(msg.id_src)