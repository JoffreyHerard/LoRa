def standard():
    print("STANDARD PHASE STARTED")
    global isRegistered
    global slot
    for idDest in isRegistered:
        print(idDest)
        print('DataReq,'+str(2)+','+
        str(frequency)+','+str(slot)+
        ','+str(id)+','+str(msg.id_src)+
        ','+str(-1)+','+str(slot))
        s.send('DataReq,'+str(2)+','+
        str(frequency)+','+str(slot)+
        ','+str(id)+','+str(msg.id_src)+
        ','+str(-1)+','+str(slot))

        dataHarvested = s.recv(128)
        msgH =messageLoRa()
        msgH.fillMessage(dataHarvested)
        rnd=Random()
        print("[FIRST Send] Request data in "+str(rnd))
        print(dataHarvested)
        time.sleep(rnd)
        while msgH.id_src != idDest and msgH.id_dest != id and msgH.kind != "5":
            rnd=Random()
            print("[Try] send Request data in "+str(rnd))
            time.sleep(rnd)
            s.send('DataReq,'+str(2)+','+
                str(frequency)+','+str(slot)+
                ','+str(id)+','+str(msg.id_src)+
                ','+str(-1)+','+str(slot))
            dataHarvested = s.recv(128)
            msgH =messageLoRa()
            msgH.fillMessage(dataHarvested)
    print("STANDARD PHASE ENDED")