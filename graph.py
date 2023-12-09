import datetime

import numpy as np
import matplotlib.pyplot as plt
from get_data import *

salary = "5192.50"
vr_va = "680.00"


class Graphs:
    def __init__(self, criteria):
        self.criteria = criteria

    def draw_graph(self):
        if self.criteria == "LIGHT":
            get_bills_from_emails(self.criteria, bills)
            self.line_plot(months_2023, bills, "b", points_color='y', graph_title='Contas de energia de 2023')
            # last_update = datetime.datetime.now()
            return [bills, months_2023]
        elif self.criteria == "CLARO":
            get_bills_from_emails(self.criteria, bills)
            self.line_plot(months_2023_short, claro_MANUAL_VALUES, "r", points_color='b', graph_title='Contas de Internet de 2023')
            # last_update = datetime.datetime.now()
            return [claro_MANUAL_VALUES, months_2023_short]

    def line_plot(self, arg1, arg2, line_color, points_color, graph_title):
        plt.figure(figsize=(18, 8))
        plt.suptitle(graph_title, fontsize=16)
        plt.ylabel('Contas')
        plt.xlabel('Meses')
        plt.xticks()
        plt.yticks(size=14)
        plt.grid(visible=True)
        plt.plot(arg1, arg2, c=line_color, lw=5)
        plt.plot(arg1, arg2, 'o', c=points_color)
        plt.savefig(f"static/graphs/graph_{self.criteria}.png")
