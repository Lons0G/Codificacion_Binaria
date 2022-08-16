def Validate(input):
    bits = []
    for i in input:
        if i == '0' or i == '1':   
            bits.append(i)
        else:
            return None
    return bits

# NRZ-BIPOLAR
def NRZ_Bipolar(input):
    bits = []  
    for i in input:
        if i == '0':
            bits.append(-1)
        else:
            bits.append(1)
    return bits
# NZR-I
def NZRI(input):
    bits = []
    state = 'Down'
    for i in input:
        if i == '1': 
            if state == 'Down':
                state = 'Up'
                bits.append(0)
                bits.append(1)
            elif state == 'Up':
                state = 'Down'
                bits.append(1)
                bits.append(0)
        elif i == '0':
            if state == 'Down':
                bits.append(0)
            elif state == 'Up':
                bits.append(1)
    return bits

# RZ
def RZ_Unipolar(input):
    bits = []
    for i in input:
        if i == '1':
            bits.append(1)
            bits.append(0)
        else:
            bits.append(0)
    return bits
# MANCHESTER
# MANCHESTER DIFERENCIAL
# AMI

