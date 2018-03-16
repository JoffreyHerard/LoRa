def notRegistered():
    #send some data
    global tryRegister
    global registered
    global myLoRa
    print("PHASE NOT REGISTERED STARTED\n")
    s.send('Register,'+str(3)+','
        +str(frequency)+','+str(slot)+
        ','+str(id)+','+str(myLoRa)+
        ','+str(-1)+','+str(-1))
    print("Register sent")
    # get any data received...
    data=s.recv(128)
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.messageName == "DataReq" and msg.id_src== myLoRa:
        registered=True
    else:
        tryRegister+=1
    print("PHASE NOT REGISTERED ENDED\n")