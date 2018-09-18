# AnotherPyplotLatexifyer
Python Matplotlib plotting settings for latex

Inspired by https://nipunbatra.github.io/blog/2014/latexify.html which written by Nitun Batra

---###---
User guide
---###---

1. Install the package
In terminal write: 
pip install git+https://github.com/Jeppefs/AnotherPyplotLatexifyer.git

2. Load the package 
To load the package, write: 
from AnotherPyplotLatexifyer import Latexify

3. Measure you latex document
Measure the width of the figure in the lated document and other changes you want to make to the plot, and note them down.
To find the text width in cm of your latex document load the package \usepackage{printlen}. In the document write \uselengthunit{cm}\printlength{\textwidth}. This will display the width in cm in the pdf. This also works in columns and subfigures. 

4. Use the package
Before plotting call: 
Latexify.Latexify()
No input is required, but it only work well, if you input the correct measures. The most important input is the fig_width. The input is in cm. 
If you would like to change the spines, call, after plotting before saving write:
Latexify.format_axes(ax)
where ax is the axis object. This only works when using the object oriented approach of matplotlib (which I highly recommend).  

5. Pad yoursself on the back
Congratulations, you are now ready to make exceptionally nice plots in matplotlib in you latex documents! Never bother with figure dimensions again!

Example of usage is given in the Latexify/LatexifyTest.py file. 