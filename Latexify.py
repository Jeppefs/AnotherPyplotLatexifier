import matplotlib.pyplot as plt
import matplotlib

import numpy as np
import pandas as pd

def Latexify(fig_width=12.65076, fig_height=None, columns=1, fontsize=8, label_size = None):
    """
    Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.

    Parameters
    ----------
    fig_width : float, optional, cm
    fig_height : float,  optional, cm
    columns : {1, 2, 3}, optional
    fontsize : float, optional, standard 8pt
    label_size : float list with dim(2,1) [width, height], optional, cm

    Notes
    ----------
    Standard size is 12.65076 cm used for standard report class of 11pt font size. 
    label_size is used if you want the inner figure (i.e. without figure labels and ticks) to be in a certain aspect. If in doubt leave in None. 
    """

    assert(columns in [1,2,3])
    golden_mean = (np.sqrt(5)-1.0)/2.0 # Aesthetic ratio

    """Convert fig_width to inches and reduce sizes based on column"""
    fig_width = cmToInch(fig_width) # Change from width in cm to inches That's just how it works man. The standard is report with 11pt font
    
    if columns == 1:
        fig_width = fig_width * 0.99 # 0.99 because that is the multiplier I use, to make a figure fit in latex. Should be 1.0???
    elif  columns == 2:
        fig_width = fig_width * 0.49 # 0.49 because that is the multiplier I use, to make a figure fit in latex. Should be 1.0/2.0???
    elif columns == 3:
        fig_width = fig_width * 0.32 # 0.32 because that is the multiplier I use, to make a figure fit in latex. Should be 1.0/3.0???

    """Calculate figure height"""
    if label_size is None:
        if fig_height is None:
            fig_height = fig_width*golden_mean
        else:
            fig_height = cmToInch(fig_height)
    elif fig_height is None:
        label_width = cmToInch(label_size[0])
        label_height = cmToInch(label_size[1])
        inner_fig_width = fig_width - label_width
        inner_fig_height = inner_fig_width*golden_mean
        fig_height = inner_fig_height + label_height
        

    """Insert parameters"""
    params = {'backend': 'ps',
              #'text.latex.preamble': ['\usepackage{gensymb}'],
              'axes.labelsize': fontsize, # fontsize for x and y labels (was 10)
              'axes.titlesize': fontsize,
              'legend.fontsize': fontsize, # was 10
              'xtick.labelsize': fontsize,
              'ytick.labelsize': fontsize,
              'text.usetex': True,
              'figure.figsize': [fig_width,fig_height]
             # 'font.family': 'serif'
    }

    matplotlib.rcParams.update(params)


    return 

def format_axes(ax, SPINE_COLOR = 'black'):
    """
    Formats the spines (black box around figure including x-axis and y-axis) to look nice. 
    Removes the right and upper spines and reduces the width of the spine.

    Parameters
    ----------
    ax : matplotlib.axes object, required
    SPINE_COLOR : Color of spines, optional
    """
    

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

