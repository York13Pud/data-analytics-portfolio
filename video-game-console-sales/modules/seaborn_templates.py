# -- Import the required libraries / modules

import numpy as np
import pandas as pd
import seaborn as sns


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
    
    return ax