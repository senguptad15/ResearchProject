# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:16:03 2020

@author: debdi
"""
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv (r'D:\AccidentsResearchProject\Data\US_Accidents_June20.csv').query("City=='Los Angeles'")


fig = px.density_mapbox(df, lat='Start_Lat', lon='Start_Lng', radius=5, zoom=7,
                        color_continuous_scale=px.colors.sequential.YlOrRd,
                        mapbox_style="stamen-terrain")
fig.update_layout(
        title = 'Mapbox Density Heatmap - Accidents',
)
fig.show(warn = True)




