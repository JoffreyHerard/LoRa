def notDiscovered():
    global tryDiscover
    global discovered
    global myLoRa
    global id
    global frequency
    global slot
    print("PHASE NOT DISCOVERED STARTED "+str(tryDiscover))
    s.send('Discover,'+str(1)+','
        +str(frequency)+','+str(slot)+','+
        str(id)+','+str(-1)+','+str(-1)+','+str(-1))
    print("Discover sent by "+str(id))
    data=s.recv(128)
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.messageName == "Accept":
        myLoRa=msg.id_src
        frequency=msg.frequency
        change_frequency(msg.frequency)
        print("Receive ACCEPT msg")
        discovered=True
    tryDiscover+=1
    print("PHASE NOT DISCOVERED ENDED\n")