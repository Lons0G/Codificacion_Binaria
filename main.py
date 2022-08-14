import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def Validate(input):
    bits = []
    for i in input:
        if i == '0' or i == '1':   
            bits.append(i)
        else:
            return None
    return bits

x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def create_plot(x, y):
    plt.plot(x, y, color = 'blue', marker = 'o')
    plt.title('Grafica simple')
    plt.xlabel('datos x')
    plt.ylabel('datos y')
    plt.grid(True)
    return plt.gcf()

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def main():
    layout = [ 
        [sg.Text('Bits'), sg.Input(key = '-Bits-'), sg.Button('Graficar', key = '-Graficar-')],
        [sg.Canvas(size = (500, 500), key = '-Canva-')]
    ]

    window = sg.Window('Codificacion Binaria', layout, finalize = True)
    draw_figure(window['-Canva-'].TKCanvas, create_plot(x_data, y_data))
    
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
