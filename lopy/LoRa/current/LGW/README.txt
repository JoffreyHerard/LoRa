Pour decoder des données LoRaWAN recu coté objenious

binascii.unhexlify(data).decode('utf8')

Pour les packs:

data1="toto:4568;titi:6544564;bob:5465456"
taille=str(len(data1))+'s'
databytes = struct.pack(taille, data1)
