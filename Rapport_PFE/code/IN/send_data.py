def sendData():
    #send some data
    global tryDataReq
    global data
    global myLoRa
    global id
    global slot
    global frequency
    print("PHASE SEND DATA STARTED\n")
    s.send('DataRes,'+str(5)+','
        +str(frequency)+','+str(slot)+','+
        str(id)+','+str(myLoRa)+','+str(data)
        +','+str(-1))
    print("DataResponse sent")
    print("PHASE SEND DATA ENDED\n")