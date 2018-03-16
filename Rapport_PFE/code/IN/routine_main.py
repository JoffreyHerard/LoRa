while True:
    if isListening:
        print("I am awake : my LoRaGW is "
            +str(myLoRa)+" and my slot is "+str(slot))
        pycom.rgbled(0x007f00) # green
        #We are not discovered yet
        while not discovered:
            notDiscovered()
            rnd=Random()
            print("Try Discover in "+str(rnd))
            time.sleep(rnd)
        while not registered and discovered:
            notRegistered()
            rnd=Random()
            print("Try Register in "+str(rnd))
            time.sleep(rnd)
        dataR=s.recv(128)
        msg =messageLoRa()
        msg.fillMessage(dataR)
        if msg.kind=="4":
            sendData()
            slot=int(msg.listeningtime)
            clock = TimerL(float(msg.listeningtime))
            print("I sent my data")
        data+=1
    else:
        pycom.rgbled(0x7f0000) #red
        print("I am sleeping")
        del clock
        time.sleep(slot)
        isListening=True
        clock = TimerL(slot)
