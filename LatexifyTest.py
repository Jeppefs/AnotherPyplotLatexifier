"""
LatexifyTest.py
Tests for the latexify packages
Makes plots of different sizes for a 11pt report latex document. 
"""

"""Initialise"""
import Latexify as Latexify
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
text_width = 12.65076 # in cm

"""Make some data"""
x1 = np.arange(0,10.05,0.1)
y1 = 2*x1+1
x2 = np.arange(0,10.05,0.1)
y2 = 0.5*x2**2+x2-1

xlabel = "Time $(\mu)$"
ylabel = "Cake (kg)"
legend = (["Linear","Parabola"])

"""Two column - full width - Golden ratio"""
Latexify.Latexify(fig_width = text_width, columns=2)
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
Latexify.Latexify(fig_width = text_width, columns=2, fontsize=10)
fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x2, y2)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.legend(legend)
ax = Latexify.format_axes(ax)
fig.tight_layout(pad=0.1)
plt.savefig("TexTests/fig/TwoInnerGolden.pdf", format = "pdf")

"""One column - 0.8 width - Golden ratio"""
Latexify.Latexify(fig_width = text_width*0.8, columns=1)
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
#plt.show()