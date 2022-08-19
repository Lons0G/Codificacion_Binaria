import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import codificacion
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

_vars = {
    'window': False,
    'fig_agg': False,
    'plt_fig': False
}

def create_step_plot(y, negative = False):
    _vars['plt_fig'] = plt.figure() 
    plt.step(np.arange(len(y)), y, label = 'pre default', where = 'mid')
    if negative == False:
        plt.yticks([0, 1])
    else:
        plt.yticks([-1, 0, 1])
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    #plt.gca().invert_yaxis()
    _vars['fig_agg'] = draw_figure(_vars['window']['-Canva-'].TKCanvas, _vars['plt_fig'])

def update_step_plot(y, negative = False):
    _vars['fig_agg'].get_tk_widget().forget()
    plt.clf()
    plt.step(np.arange(len(y)), y, label = 'pre default', where = 'mid')
    if negative == False:
        plt.yticks([0, 1])
    else:
        plt.yticks([-1, 0, 1])
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    _vars['fig_agg'] = draw_figure(_vars['window']['-Canva-'].TKCanvas, _vars['plt_fig'])

def draw_figure(canvas, figure): 
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

encoding = ['NRZ Unipolar', 'NRZ Bipolar', 'NRZ-I', 'RZ Unipolar', 'RZ Bipolar', 'Manchester']
layout = [ 
    [sg.Text('Bits'), sg.Input(key = '-Bits-'), sg.Combo(encoding, default_value = encoding[0], key = '-Combo-'), sg.Button('Graficar', key = '-Graficar-')],
    [sg.Canvas(size = (500, 500), key = '-Canva-')]
]
_vars['window'] = sg.Window('Codificacion Binaria', layout, finalize = True)

def main():
    while True:
        event, values = _vars['window'].Read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '-Graficar-':
            input = values['-Bits-']
            bits = codificacion.Validate(input)
            if bits is not None:
                bits, negative = codificacion.Encoding_Method(bits, values['-Combo-'])
                update_step_plot(bits, negative)
            else:
                sg.popup('Valores Incorrectos')
    _vars['window'].close()
if __name__ == '__main__':
    create_step_plot([], False)
    main()
