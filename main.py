import PySimpleGUI as sg

def Validate(input):
    bits = []
    for i in input:
        if i == '0' or i == '1':   
            bits.append(i)
        else:
            return None
    return bits

def main():
    layout = [ 
        [sg.Text('Bits'), sg.Input(key = '-Bits-'), sg.Button('Graficar', key = '-Graficar-')]
    ]

    window = sg.Window('Codificacion Binaria', layout)
    while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '-Graficar-':
            input = values['-Bits-']
            bits = Validate(input)
            if bits is not None:
                print('valores correctos')
            else:
                print('valores incorrectos')
            
    window.close()
if __name__ == '__main__':
    main()
