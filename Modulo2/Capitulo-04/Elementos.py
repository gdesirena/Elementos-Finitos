import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
class ElementosTriangular:
    def __init__(self):
        self.el = None
    
    def DesarrolloElementoTriangularL(self, x,y,n):
        '''
        param:
        x : lista de coordenadas en x
        y : lista de coordenadas en y
        n : Número de nodos
        Output:
        el: Diccionario con los parámetros 'n','x', 'y' , 'A' 'b1, 'c1' , 'b2', 'c2', 'b3', 'c3', 'K', 'F'
        '''
        el = {'x':x, 'y':y, 'n':n}

        A = (1/2)*np.abs(el['x'][0]*(el['y'][1] - el['y'][2]) + 
               el['x'][1]*(el['y'][2] - el['y'][0]) +
               el['x'][2]*(el['y'][0] - el['y'][1]))
        el.update(A=A)
        el.update(b1 = el['y'][1] - el['y'][2])
        el.update(c1 = el['x'][2] - el['x'][1])
        el.update(b2 = el['y'][2] - el['y'][0])
        el.update(c2 = el['x'][0] - el['x'][2])
        el.update(b3 = el['y'][0] - el['y'][1])
        el.update(c3 = el['x'][1] - el['x'][0])

        Kb = np.array([[el['b1']*el['b1'], el['b1']*el['b2'], el['b1']*el['b3']],
                       [el['b2']*el['b1'], el['b2']*el['b2'], el['b2']*el['b3']],
                       [el['b3']*el['b1'], el['b3']*el['b2'], el['b3']*el['b3']] ])

        Kc = np.array([[el['c1']*el['c1'], el['c1']*el['c2'], el['c1']*el['c3']],
                       [el['c2']*el['c1'], el['c2']*el['c2'], el['c2']*el['c3']],
                       [el['c3']*el['c1'], el['c3']*el['c2'], el['c3']*el['c3']] ])

        K = (k/(4*el['A']))*(Kb + Kc)
        el.update(K=K)

        return el
    
    def graficarElemento(self, el):
        import matplotlib.pyplot as plt
        if isinstance(el, dict):
            plt.figure(figsize=(5,5))
            plt.plot(el['x'] + [el['x'][0]], el['y'] + [el['y'][0]])
            for x, y, n in zip(el['x'], el['y'], el['n']):
                plt.text(x,y,n)

        if isinstance(el, list) or isinstance(el, tuple): 
            plt.figure(figsize=(5,5))
            for ele in el:
                plt.plot(ele['x'] + [ele['x'][0]], ele['y'] + [ele['y'][0]] )
                for x, y, n in zip(ele['x'], ele['y'], ele['n']):
                    plt.text(x,y,n)
        plt.grid()
        plt.axis('equal')
        plt.show()