# -- Import the required libraries / modules

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def colours(data: pd.DataFrame):
    colour_pallette = {}

    for vendor in data["vendor"]:
        if vendor == "Sony":
            add_to_dict = {vendor: "#032f8a"}
            colour_pallette.update(add_to_dict)
        elif vendor == "Microsoft":
            add_to_dict = {vendor: "#107910"}
            colour_pallette.update(add_to_dict)
        elif vendor == "Nintendo":
            add_to_dict = {vendor: "#d60011"}
            colour_pallette.update(add_to_dict)
        elif vendor == "Sega":
            add_to_dict = {vendor: "#0e6dbc"}
            colour_pallette.update(add_to_dict)
        elif vendor == "Atari":
            add_to_dict = {vendor: "#a600ff"}
            colour_pallette.update(add_to_dict)
        else:
            add_to_dict = {vendor: "#8f8f8f"}
            colour_pallette.update(add_to_dict)
            
    return colour_pallette


def sns_barplot_ax(data: pd.DataFrame,
                   x_axis: str,
                   x_axis_label: str,
                   x_axis_max_value: float,
                   y_axis: str,
                   y_axis_label: str,
                   hue: str,
                   pallette: dict,
                   title: str):
    
    ax = sns.barplot(data = data,
                     x = x_axis, 
                     y = y_axis,
                     hue = hue,
                     palette = pallette)

    # -- Show values at the end of each bar:
    for i in ax.containers:
        ax.bar_label(i, padding = 8)

    # -- Set axis labels and title:
    ax.set_xlabel(xlabel = x_axis_label, fontsize = 12)
    ax.set_ylabel(ylabel = y_axis_label, fontsize = 12)

    ax.set_title(label = title, pad = 15, 
                loc = "left", fontdict = {"fontsize": 16})

    # -- Build the legend:
    legend = ax.legend(framealpha=1)
    legend.set_title(title = hue.capitalize())
    legend.set_loc(loc = "lower right")

    # -- Set the legends background to white:
    frame = legend.get_frame()
    frame.set_facecolor("white")

    # -- Set the x-axis to be 20 higher than the rounded max value:
    ax.set_xlim(0, round(x_axis_max_value/10)*10 + 20)

    return ax