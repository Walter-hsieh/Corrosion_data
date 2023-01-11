import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read data
df = pd.read_excel('test_data.xlsx')

# set figure
fig, ax = plt.subplots()
ax.plot(df['P'], df['log_A'])

# User input
#-------------------------------------------------------

x0 = [-0.2558899, -0.1789856]
y0 =[-6.40058, -6.803409]

x1 = [-0.05828857, -0.06149292]
y1 = [-7.142794, -7.188034]

lowest_point = [-0.09246826, -9.323564]

#-------------------------------------------------------

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


plt.show()


'''
import plotly.express as px
import plotly.graph_objects as go
fig = px.line(x = xseq, y =a0 + b0 * xseq)
fig.add_trace(go.Scatter(x = xseq1 , y = a1 + b1 * xseq1, mode='lines'))
fig.add_trace(go.Scatter(x = x2 , y = y2, mode='lines'))
fig.add_scatter(x=df['P'], y=df['log_A'])
# fig.show()
'''






# reference
url = "https://www.python-graph-gallery.com/scatterplot-with-regression-fit-in-matplotlib"
url1 = "https://www.youtube.com/watch?v=heGBqav2TbU"