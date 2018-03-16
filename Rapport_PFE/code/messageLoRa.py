class messageLoRa:
    messageName="not set yet"
    frequency=0
    slots=0
    id_src=-1
    id_dest=-1
    data=-1
    kind=0
    listeningtime=0
    def __init__(self):
        self.messageName="not set yet"
        self.kind=-1
        self.frequency=0
        self.slots=0
        self.id_src=-1
        self.id_dest=-1
        self.data=-1
        self.listeningtime=0
    def fillMessage(self, data):
        message=data.decode()
        if message != '':
            self.messageName,
            self.kind,
            self.frequency,
            self.slots,
            self.id_src,
            self.id_dest,
            self.data,
            self.listeningtime= message.split(",")
        else:
            print("Received nothing")