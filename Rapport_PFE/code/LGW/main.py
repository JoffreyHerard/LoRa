while True:
    if isListening:
        print("I am awake")
        pycom.rgbled(0x007f00) # green
        data = s.recv(128)
        handle_message(data)
        standard()
    else:
        pycom.rgbled(0x7f0000) #red
        print("I am sleeping")
        time.sleep(slot)
        isListening=True
        del clock
        clock = TimerL(slot)
