import plotly.figure_factory as pff 
import pandas as pd
import csv 
df = pd.read_csv("data2.csv")
fig = pff.create_distplot([df["Avg Rating"].tolist()],["Mobile Brand"],show_hist = False)
fig.show()