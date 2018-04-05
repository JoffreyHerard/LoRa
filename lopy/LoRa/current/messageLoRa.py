class messageLoRa:
    messageName="not set yet"
    frequency=0
    slots=0
    id_src=-1
    id_dest=-1
    data=-1
    kind=0
    toto=0
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
            self.messageName,self.kind,self.frequency,self.slots,self.id_src,self.id_dest,self.data,self.listeningtime= message.split(",")
        else:
            print("Received nothing")
    def get_name(self):
        return self.messageName

    def set_name(self, x):
        self.messageName = x

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, x):
        self.frequency = x

    def get_slots(self):
        return self.slots

    def set_slots(self, x):
        self.slots=x

    def get_src(self):
        return self.id_src

    def set_src(self, x):
        self.id_src= x

    def get_dest(self):
        return self.id_dest

    def set_dest(self, x):
        self.id_dest= x
