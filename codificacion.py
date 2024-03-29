def Validate(input):
    bits = []
    if input == '':
        return None
    else:
        for i in input:
            if i == '0' or i == '1':   
                bits.append(i)
    return bits
# Encoding
def Encoding_Method(input, encoding):
    bits = []
    negative = False
    if encoding == 'NRZ Bipolar':
        bits, negative =  NRZ_Bipolar(input)
    elif encoding == 'NRZ-I':
        bits, negative = NRZI(input)
    elif encoding == 'RZ Unipolar':
        bits, negative = RZ_Unipolar(input)
    elif encoding == 'RZ Bipolar':
        bits, negative = RZ_Bipolar(input)
    elif encoding == 'Manchester':
        bits, negative = Manchester(input)
    elif encoding == 'NRZ Unipolar':
        bits, encoding = NRZ_Unipolar(input)
    return bits, negative
# NRZ Unipolar
def NRZ_Unipolar(input):
    bits = []
    negative = False
    for i in input:
        if i == '0':
            bits.append(0)
        else:
            bits.append(1)
    return bits, negative
# NRZ-BIPOLAR
def NRZ_Bipolar(input):
    bits = []  
    negative = True
    for i in input:
        if i == '0':
            bits.append(-1)
        else:
            bits.append(1)
    return bits, negative
# NZR-I
def NRZI(input):
    bits = []
    negative = False
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
    return bits, negative
# RZ Unipolar
def RZ_Unipolar(input):
    bits = []
    negative = False
    for i in input:
        if i == '1':
            bits.append(1)
            bits.append(0)
        else:
            bits.append(0)
    return bits, negative
# RZ Bipolar
def RZ_Bipolar(input):
    bits = []
    negative = True
    state = 'Down'
    for i in input:
        if i == '1':
            if state == 'Down':
                state = 'Up'
                bits.append(1)
                bits.append(0)
            elif state == 'Up':
                state = 'Down'
                bits.append(-1)
                bits.append(0)
        else:
            bits.append(0)
    return bits, negative
# MANCHESTER
def Manchester(input):
    bits = []
    negative = False
    for i in input:
        if i == '0':
            bits.append(0)
            bits.append(1)
        else:
            bits.append(1)
            bits.append(0)
    return bits, negative
# MANCHESTER DIFERENCIAL
# AMI

