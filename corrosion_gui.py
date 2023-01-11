import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


# Create a GUI
import tkinter as tk
import ttkbootstrap as ttkb
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkbootstrap.constants import *

root = ttkb.Window(themename="cosmo")
root.geometry("1500x800")


# list excel files
files = list(filter(lambda x: 'xlsx' in x, os.listdir()))


#-----------------------user input------------------------
x0_label = ttkb.Label(root, text='x0')
x0_label.place(x=10,y=50)
x0_inp = ttkb.Entry(root, bootstyle="primary")
x0_inp.place(x=50,y=50)

y0_label = ttkb.Label(root, text='y0')
y0_label.place(x=300,y=50)
y0_inp = ttkb.Entry(root, bootstyle="primary")
y0_inp.place(x=340,y=50)

x1_label = ttkb.Label(root, text='x1')
x1_label.place(x=10,y=100)
x1_inp = ttkb.Entry(root, bootstyle="primary")
x1_inp.place(x=50,y=100)

y1_label = ttkb.Label(root, text='y1')
y1_label.place(x=300,y=100)
y1_inp = ttkb.Entry(root, bootstyle="primary")
y1_inp.place(x=340,y=100)

x2_label = ttkb.Label(root, text='x2')
x2_label.place(x=10,y=150)
x2_inp = ttkb.Entry(root, bootstyle="primary")
x2_inp.place(x=50,y=150)

y2_label = ttkb.Label(root, text='y2')
y2_label.place(x=300,y=150)
y2_inp = ttkb.Entry(root, bootstyle="primary")
y2_inp.place(x=340,y=150)

x3_label = ttkb.Label(root, text='x3')
x3_label.place(x=10,y=200)
x3_inp = ttkb.Entry(root, bootstyle="primary")
x3_inp.place(x=50,y=200)

y3_label = ttkb.Label(root, text='y3')
y3_label.place(x=300,y=200)
y3_inp = ttkb.Entry(root, bootstyle="primary")
y3_inp.place(x=340,y=200)

lpx_label = ttkb.Label(root, text='lp_x')
lpx_label.place(x=10,y=250)
lpx_inp = ttkb.Entry(root, bootstyle="primary")
lpx_inp.place(x=50,y=250)

lpy_label = ttkb.Label(root, text='lp_y')
lpy_label.place(x=300,y=250)
lpy_inp = ttkb.Entry(root, bootstyle="primary")
lpy_inp.place(x=340,y=250)
#-----------------------user input------------------------

# create a entry to take the file name for plotting
file_inp = ttkb.Label(root, text='Choose a file to open')
file_inp.place(x=180,y=300)

cb = ttkb.Combobox(root, values=files)
cb.place(x=170,y=340)

# create a button to set chosen file name
open_file = ttkb.Button(root, text='Open file', command=(lambda : on_submit()), bootstyle=SUCCESS)
open_file.place(x=230,y=390)


# Create an Entry widget to accept user input
img_name_label = ttkb.Label(root, text='Enter name for saved image')
img_name_label.place(x=180,y=450)

img_name = ttkb.Entry(root, bootstyle="primary")
img_name.focus_set()
img_name.place(x=180,y=480)

# Create a button to save the image
save_fig = ttkb.Button(root, text='save image', command=(lambda:save_image()), bootstyle=SUCCESS)
save_fig.place(x=220,y=530)


# Create a button using destroy command to close a Tkinter window
quit_button = ttkb.Button(root, text='Close window', command=root.quit, bootstyle=SUCCESS)
quit_button.place(x=210,y=580)

# set action label
action_label = ttkb.Label(root, text='Action statement will show here when pressing any button')
action_label.place(x=30,y=640)

# Functions
# Create a save image function
def save_image():
    global entry
    string = img_name.get()
    figure.savefig(string)
    text = ' '*37 + 'image is saved'
    action_label.configure(text=text)




figure = plt.Figure(figsize=(5, 4), dpi=100)
ax = figure.add_subplot(111)

def file_open():
	text = ' '*35 + 'plot is drawed'
	action_label.configure(text=text)




def on_submit():

	file_open()

	filename = cb.get()

	df = pd.read_excel(filename)

	ax.plot(df['P'], df['log_A'])

	#---------------------------test data-------------------------
	x0 = [-0.2558899, -0.1789856]
	y0 =[-6.40058, -6.803409]

	x1 = [-0.05828857, -0.06149292]
	y1 = [-7.142794, -7.188034]

	lowest_point = [-0.09246826, -9.323564]

	#-----------------------User input-----------------------------

	# x0 = [float(x0_inp.get()), float(x1_inp.get())]
	# y0 =[float(y0_inp.get()), float(y1_inp.get())]

	# x1 = [float(x2_inp.get()), float(x3_inp.get())]
	# y1 =[float(y2_inp.get()), float(y3_inp.get())]


	# lowest_point = [float(lpx_inp.get()), float(lpy_inp.get())]

	#-----------------------User input-----------------------------
	x2 = [lowest_point[0], lowest_point[0]]
	y2 = [lowest_point[1], lowest_point[1] + 3 ]


	# Add scatterplot
	ax.scatter(x0, y0, s=60, alpha=0.7, edgecolors="k")
	ax.scatter(x1, y1, s=60, alpha=0.7, edgecolors="k")
	ax.scatter(x2, y2, s=60, alpha=0.7, edgecolors="k")


	# Fit linear regression via least squares with numpy.polyfit
	# It returns an slope (b) and intercept (a)
	# deg=1 means linear fit (i.e. polynomial of degree 1)
	b0, a0 = np.polyfit(x0, y0, deg=1)
	b1, a1 = np.polyfit(x1, y1, deg=1)




	# Create sequence of 100 numbers from 0 to 100 

	ocp = lowest_point[0] # input ocp (changable parameter)
	xseq = np.linspace(ocp-0.25, ocp+0.25, num=100)
	xseq1 = np.linspace(ocp-0.25, ocp+0.25, num=100)

	# Plot regression line
	ax.plot(xseq, a0 + b0 * xseq, color="k", lw=1);
	ax.plot(xseq1, a1 + b1 * xseq1, color="k", lw=1);
	ax.plot(x2, y2, color="k", lw=1)


	from shapely.geometry import LineString
	line_1 = LineString(np.column_stack((xseq, a0 + b0 * xseq)))
	line_2 = LineString(np.column_stack((xseq1, a1 + b1 * xseq1)))
	line_3 = LineString(np.column_stack((x2, y2)))
	intersection = line_1.intersection(line_2)
	intersection1 = line_1.intersection(line_3)
	intersection2 = line_2.intersection(line_3)

	ax.plot(*intersection.xy, 'ro')
	ax.plot(*intersection1.xy, 'bo')
	ax.plot(*intersection2.xy, 'yo')



	px0,py0 = intersection.xy
	px1,py1 = intersection1.xy
	px2,py2 = intersection2.xy
	print(px0[0],py0[0])
	print(px1[0],py1[0])
	print(px2[0],py2[0])


	text = f" point1: ({round(px0[0],4)},{round(py0[0],4)}),\n point2: ({round(px1[0],4)},{round(py1[0],4)}),\n point3: ({round(px2[0],4)},{round(py2[0],4)})"

	print(text)

	# ax.annotate(text, xy=(px[0], py[0]), xytext=(px[0],py[0]+0.9), arrowprops = dict(facecolor='blue', shrink = 0.15))
	ax.annotate(text, xy=(px0[0], py0[0]), xytext=(px0[0],py0[0]+0.9))

	scatter = FigureCanvasTkAgg(figure, root)
	scatter.get_tk_widget().place(x=600,y=10)


root.mainloop()