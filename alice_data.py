import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('test_data.xlsx')

# print(df)

fig, ax = plt.subplots()

ax.plot(df['P'], df['log_A'])

# plt.show()

x = [-0.1298523, -0.1266479]
y =[-7.139177, -7.171221]

x1 = [-0.05828857, -0.06149292]
y1 = [-7.142794, -7.188034]

# Initialize layout
# fig, ax = plt.subplots(figsize = (9, 9))

# Add scatterplot
ax.scatter(x, y, s=60, alpha=0.7, edgecolors="k")
ax.scatter(x1, y1, s=60, alpha=0.7, edgecolors="k")

# Fit linear regression via least squares with numpy.polyfit
# It returns an slope (b) and intercept (a)
# deg=1 means linear fit (i.e. polynomial of degree 1)
b, a = np.polyfit(x, y, deg=1)
b1, a1 = np.polyfit(x1, y1, deg=1)


# Create sequence of 100 numbers from 0 to 100 
xseq = np.linspace(-0.3, -0.0828, num=100)
xseq1 = np.linspace(-0.096, 0.06, num=100)

# Plot regression line
ax.plot(xseq, a + b * xseq, color="k", lw=1);
ax.plot(xseq1, a1 + b1 * xseq1, color="k", lw=1);

from shapely.geometry import LineString
line_1 = LineString(np.column_stack((xseq, a + b * xseq)))
line_2 = LineString(np.column_stack((xseq1, a1 + b1 * xseq1)))
intersection = line_1.intersection(line_2)
ax.plot(*intersection.xy, 'ro')


px,py = intersection.xy
print(px[0],py[0])
print(type(px[0]))

text = f"({round(px[0],4)},{round(py[0],4)})"

print(text)

ax.annotate(text, xy=(px[0], py[0]), xytext=(px[0],py[0]+0.9), arrowprops = dict(facecolor='blue', shrink = 0.15))

plt.show()



import plotly.express as px
import plotly.graph_objects as go
fig = px.line(x = xseq, y =a + b * xseq)
fig.add_trace(go.Scatter(x = xseq1 , y = a1 + b1 * xseq1, mode='lines'))
fig.add_scatter(x=df['P'], y=df['log_A'])
fig.show()






# reference
url = "https://www.python-graph-gallery.com/scatterplot-with-regression-fit-in-matplotlib"
url1 = "https://www.youtube.com/watch?v=heGBqav2TbU"