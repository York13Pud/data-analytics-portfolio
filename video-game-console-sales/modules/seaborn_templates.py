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
                   y_axis: str,
                   y_axis_label: str,
                   hue: str):
    
    
    
    ax = sns.barplot(data=data, 
            x = x_axis, 
            y = y_axis,
            hue = hue,
            palette = "Greens",
            err_kws={'linewidth': 0}
            )

    # -- Show values at the end of each bar:
    for i in ax.containers:
        ax.bar_label(i)
    
    # -- Set axis labels:
    ax.set(xlabel = x_axis_label, 
           ylabel = y_axis_label)
    
    ax.spines["right"].set_visible(False)
    
    ax.grid(visible = True, axis = "x")
    
    
    return ax