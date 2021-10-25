import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("Project108data.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=False)
fig.show()
