"""
LatexifyTest.py
Tests for the latexify packages
Makes plots of different sizes for a 11pt report latex document. 
"""

"""Packages"""
from Latexify import Latexify
import numpy as np
import matplotlib.pyplot as plt

"""
Options:

text_width : The width of the latex documents where text exist in cm. 
Common text widths:
10 pt report: 
11 pt report: 12.65076cm
12 pt report: 
2 column scientific journal: 
Tufte Computer Modern: 
Tufte Computer Modern margin: 
"""
text_width = 12.65076 *0.99 # in cm
column_width = 6.19893 *0.98

"""Make some data"""
x1 = np.arange(0,10.05,0.1)
y1 = 2*x1+1
x2 = np.arange(0,10.05,0.1)
y2 = 0.5*x2**2+x2-1

xlabel = "Time $(\mu)$"
ylabel = "Cake (kg)"
legend = (["Linear","Parabola"])

"""Two column - full width - Golden ratio"""
Latexify.Latexify(fig_width = column_width)
fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x2, y2)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.legend(legend)
ax = Latexify.format_axes(ax)
fig.tight_layout(pad=0.1)
plt.savefig("TexTests/fig/TwoGolden.pdf", format = "pdf")

"""Two column - full width - Inner figure is golden ratio"""
Latexify.Latexify(fig_width = column_width, label_size=[1.05, 1.05])
fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x2, y2)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.legend(legend)
ax = Latexify.format_axes(ax)
fig.tight_layout(pad=0.1)
plt.savefig("TexTests/fig/TwoInnerGolden.pdf", format = "pdf")

"""Two column - full width - Golden ratio - 11 pt"""
Latexify.Latexify(fig_width = column_width, fontsize=11)
fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x2, y2)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.legend(legend)
ax = Latexify.format_axes(ax)
fig.tight_layout(pad=0.1)
plt.savefig("TexTests/fig/TwoGolden11.pdf", format = "pdf")

"""Two column - full width - Inner figure is golden ratio - 11 pt"""
Latexify.Latexify(fig_width = column_width, fontsize=11, label_size=[1.05, 1.05])
fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x2, y2)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.legend(legend)
ax = Latexify.format_axes(ax)
fig.tight_layout(pad=0.1)
plt.savefig("TexTests/fig/TwoInnerGolden11.pdf", format = "pdf")

"""One column - 0.8 width - Golden ratio"""
Latexify.Latexify(fig_width = text_width*0.8/0.99, columns=1)
fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x2, y2)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.legend(legend)
ax = Latexify.format_axes(ax)
fig.tight_layout(pad=0.1)
plt.savefig("TexTests/fig/OneGoldenSmall.pdf", format = "pdf")

"""One column - full width - Golden ratio"""
Latexify.Latexify(fig_width = text_width, columns=1)
fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x2, y2)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.legend(legend)
ax = Latexify.format_axes(ax)
fig.tight_layout(pad=0.1)
plt.savefig("TexTests/fig/OneGoldenFull.pdf", format = "pdf")

"""Show"""
plt.show()