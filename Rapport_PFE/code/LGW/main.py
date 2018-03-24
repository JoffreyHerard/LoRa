while True:
    if isListening:
        print("I am awake")
        pycom.rgbled(0x007f00) # green
        data = s.recv(128)
        handle_message(data)
        time.sleep(0.500)
        recolte=standard()
        print(recolte)
        time.sleep(0.500)
        if recolte !="" :
            changetoLW()
            s.setblocking(True)
            send_datatoLWGW(s,recolte)
            s.setblocking(False)
            changetoLoRa(lora)
    else:
        pycom.rgbled(0x7f0000) #red
        print("I am sleeping")
        time.sleep(slot)
        isListening=True
        del clock
        clock = TimerL(slot)

