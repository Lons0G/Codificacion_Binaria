import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import codificacion
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_step_plot(y, negative = False):
    plt.step(np.arange(len(y)), y, label = 'pre default', where = 'mid')
    if negative == False:
        plt.yticks([0, 1])
    else:
        plt.yticks([-1, 0, 1])
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    #plt.gca().invert_yaxis()
    return plt.gcf()

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def main():
    encoding = ['NRZ Bipolar', 'NRZ-I', 'RZ Unipolar', 'RZ Bipolar', 'Manchester']
    layout = [ 
        [sg.Text('Bits'), sg.Input(key = '-Bits-'), sg.Combo(encoding, default_value = encoding[0], key = '-Combo-'), sg.Button('Graficar', key = '-Graficar-')],
        [sg.Canvas(size = (500, 500), key = '-Canva-')]
    ]

    window = sg.Window('Codificacion Binaria', layout, finalize = True)
    while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '-Graficar-':
            input = values['-Bits-']
            bits = codificacion.Validate(input)
            bits, negative = codificacion.Encoding_Method(bits, values['-Combo-'])
            if bits is not None:
                print('valores correctos')
                draw_figure(window['-Canva-'].TKCanvas, create_step_plot(bits, negative))
            else:
                print('valores incorrectos')
            
    window.close()
if __name__ == '__main__':
    main()
