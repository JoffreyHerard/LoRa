#frequency accepts values between 863000000 and 870000000
#FROM SPEC LORAWAN LORA
#868000000 F1
#868100000 F2
#868300000 F3
#868500000 F4
#864100000 F5
#864300000 F6
#864500000 F7
def change_frequency(frequency_d):
    current_frequency=lora.frequency()
    if current_frequency != frequency_d:
        if frequency_d == 1:
            lora.frequency(868000000)
        if frequency_d == 2:
            lora.frequency(868100000)
        if frequency_d == 3:
            lora.frequency(868300000)
        if frequency_d == 4:
            lora.frequency(868500000)
        if frequency_d == 5:
            lora.frequency(864100000)
        if frequency_d == 6:
            lora.frequency(864300000)
        if frequency_d == 7:
            lora.frequency(864500000)
        print("FREQUENCY WAS CHANGED FROM :"+current_frequency+" TO= "+frequency_d)
    else:
        print("FREQUENCY ALREADY CHANGED")
