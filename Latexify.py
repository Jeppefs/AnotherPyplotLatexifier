import matplotlib.pyplot as plt
import matplotlib

import numpy as np
import pandas as pd

def Latexify(fig_width=None, fig_height=None, columns=1, fontsize=8):
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.

    Standard size is 12.65076 cm used for standard report class of 11pt font size 

    Parameters

    ----------
    fig_width : float, optional, cm
    fig_height : float,  optional, cm
    columns : {1, 2, 3}
    fontsize : float, optional, standard 8pt
    """

    assert(columns in [1,2,3])

    label_width = 1.25 # cm
    label_height = 1.05 # cm 

    if fig_width is None:
        fig_width = cmToInch(12.65076) # width in inches. The standard is report with 11pt font
    

    if columns == 1:
        fig_width = fig_width * 0.99
    elif  columns == 2:
        #fig_width = fig_width * (1/0.49)
        fig_width = fig_width * 0.49
    elif columns == 3:
        fig_width = fig_width * 0.32

    if fig_height is None:
        golden_mean = (np.sqrt(5)-1.0)/2.0 # Aesthetic ratio
        fig_height = fig_width*golden_mean * 1.5 # height in inches

    params = {'backend': 'ps',
              #'text.latex.preamble': ['\usepackage{gensymb}'],
              'axes.labelsize': fontsize+2, # fontsize for x and y labels (was 10)
              'axes.titlesize': fontsize+2,
              'legend.fontsize': fontsize, # was 10
              'xtick.labelsize': fontsize,
              'ytick.labelsize': fontsize,
              'text.usetex': True,
              'figure.figsize': [fig_width,fig_height]
             # 'font.family': 'serif'
    }

    matplotlib.rcParams.update(params)


    return 

def format_axes(ax):
    
    SPINE_COLOR = 'black'

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    for spine in ['left', 'bottom']:
        ax.spines[spine].set_color(SPINE_COLOR)
        ax.spines[spine].set_linewidth(0.5)

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_tick_params(direction='out', color=SPINE_COLOR)

    return ax

def cmToInch(cm):
    return cm * 0.393701

