import plotly.figure_factory as pff 
import pandas as pd
import csv 
df = pd.read_csv("data1.csv")
fig = pff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist = False)
fig.show()