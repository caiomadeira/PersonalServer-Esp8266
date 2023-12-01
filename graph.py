import numpy as np
import matplotlib.pyplot as plt
from get_data import *

salary = "5192.50"
vr_va = "680.00"

def draw_graph(criteria):
    if criteria == "LIGHT":
        get_bills_from_emails(criteria, bills)
        line_plot(months_2023, bills, "g")
    elif criteria == "CLARO":
        get_bills_from_emails(criteria, bills)
        line_plot(months_2023_short, claro_MANUAL_VALUES, "r")

def line_plot(arg1, arg2, line_color):
    plt.plot(arg1, arg2, c=line_color, lw=5)
    plt.show()


draw_graph("CLARO")
