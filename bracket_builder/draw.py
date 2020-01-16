import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from matplotlib.collections import LineCollection
from matplotlib.backends.backend_pdf import PdfPages


def collect_lines(x_array, y_arrays, colors='black',
                  linewidths=1, linestyles='solid'):
    ## Simple function to create a matplotlib line collection based
    #   on an array of xs and many arrays of y
    return LineCollection([np.column_stack([x_array, y])
                           for y in y_arrays],
                          linewidths=linewidths,
                          colors=colors,
                          linestyles=linestyles)

class Bracket:
    def __init__(self, n_teams, team_names, win_probabilities=None):
        self.n_teams = n_teams
        self.team_names = team_names
        self.win_probabilities = win_probabilities

    def draw_bracket(self):

        ## manipulate plt to draw all the lines based on how many teams
        if self.n_teams == 64:
            ## draw 64 team bracket
            fig, ax = plt.subplots()

            # We need to set the plot limits, they will not autoscale
            plt.xlim([-1, 221])
            plt.ylim([-1, 67])

            ### X values for left/right side
            ## Left side of bracket
            r1_left_x = np.array([0, 20])  # 1st round range x from 0 to 20
            r1_left_connect_x = np.array([20, 20]) # Xs to connect the two teams playing each other
            r2_left_x = np.array([20, 40])
            r2_left_connect_x = np.array([40, 40])
            r3_left_x = np.array([40, 60])
            r3_left_connect_x = np.array([60, 60])
            r4_left_x = np.array([60, 80])
            r4_left_connect_x = np.array([80, 80])
            r5_left_x = np.array([80, 100])
            r5_left_connect_x = np.array([100, 100])
            final_left_x = np.array([115,100])

            ## Right side of bracket
            r1_right_x = np.array([200, 220])  # 1st round range x from 0 to 20
            r1_right_connect_x = np.array([200, 200])  # Xs to connect the two teams playing each other
            r2_right_x = np.array([180, 200])
            r2_right_connect_x = np.array([180, 180])
            r3_right_x = np.array([160, 180])
            r3_right_connect_x = np.array([160, 160])
            r4_right_x = np.array([140, 160])
            r4_right_connect_x = np.array([140, 140])
            r5_right_x = np.array([120, 140])
            r5_right_connect_x = np.array([120, 120])
            final_right_x = np.array([120,105])

            ## Champion Xs
            champ_x = np.array([90,130])

            ### Y values can correspond to either side (reuse these arrays)
            r1_ys = [np.repeat(np.array([x]), 2) for x in np.arange(0, 32, 2)]
            r1_ys.extend([np.repeat(np.array([x]), 2) for x in np.arange(36, 67, 2)])
            r1_connect_ys = [np.arange(x, x+3, 2) for x in np.arange(0, 29, 4)]
            r1_connect_ys.extend([np.arange(x, x+3, 2) for x in np.arange(36, 65, 4)])

            r2_ys = [np.repeat(np.array([x]), 2) for x in np.arange(1, 30, 4)]
            r2_ys.extend([np.repeat(np.array([x]), 2) for x in np.arange(37, 68, 4)])
            r2_connect_ys = [np.arange(x, x+5, 4) for x in np.arange(1, 28, 8)]
            r2_connect_ys.extend([np.arange(x, x+5, 4) for x in np.arange(37, 63, 8)])

            r3_ys = [np.repeat(np.array([x]), 2) for x in np.arange(3, 28, 8)]
            r3_ys.extend([np.repeat(np.array([x]), 2) for x in np.arange(38, 64, 8)])
            r3_connect_ys = [np.array([3,11]), np.array([19, 27]),
                             np.array([38, 46]), np.array([54, 62])]

            r4_ys = [np.repeat(np.array([x]), 2) for x in np.arange(7, 24, 16)]
            r4_ys.extend([np.repeat(np.array([x]), 2) for x in np.arange(42, 59, 16)])
            r4_connect_ys = [np.array([7,23]), np.array([42, 58])]

            r5_ys = [np.array([15, 15]), np.array([50, 50])]
            r5_connect_ys = [np.array([15,50]), np.array([15, 50])]

            final_left_y = [np.array([35, 35])]
            final_right_y = [np.array([30, 30])]
            champ_ys = [np.array([60, 60])]

            ## Make sequences of x,y pairs
            left_r1_lines = collect_lines(r1_left_x, r1_ys)
            left_r1_connect_lines = collect_lines(r1_left_connect_x, r1_connect_ys)
            left_r2_lines = collect_lines(r2_left_x, r2_ys)
            left_r2_connect_lines = collect_lines(r2_left_connect_x, r2_connect_ys)
            left_r3_lines = collect_lines(r3_left_x, r3_ys)
            left_r3_connect_lines = collect_lines(r3_left_connect_x, r3_connect_ys)
            left_r4_lines = collect_lines(r4_left_x, r4_ys)
            left_r4_connect_lines = collect_lines(r4_left_connect_x, r4_connect_ys)
            left_r5_lines = collect_lines(r5_left_x, r5_ys)
            left_r5_connect_lines = collect_lines(r5_left_connect_x, r5_connect_ys)

            right_r1_lines = collect_lines(r1_right_x, r1_ys)
            right_r1_connect_lines = collect_lines(r1_right_connect_x, r1_connect_ys)
            right_r2_lines = collect_lines(r2_right_x, r2_ys)
            right_r2_connect_lines = collect_lines(r2_right_connect_x, r2_connect_ys)
            right_r3_lines = collect_lines(r3_right_x, r3_ys)
            right_r3_connect_lines = collect_lines(r3_right_connect_x, r3_connect_ys)
            right_r4_lines = collect_lines(r4_right_x, r4_ys)
            right_r4_connect_lines = collect_lines(r4_right_connect_x, r4_connect_ys)
            right_r5_lines = collect_lines(r5_right_x, r5_ys)
            right_r5_connect_lines = collect_lines(r5_right_connect_x, r5_connect_ys)

            final_left_line = collect_lines(final_left_x, final_left_y)
            final_right_line = collect_lines(final_right_x, final_right_y)

            champ_line = collect_lines(champ_x, champ_ys)

            ### Add the line segments to the plot
            ## Left side
            ax.add_collection(left_r1_lines)
            ax.add_collection(left_r1_connect_lines)
            ax.add_collection(left_r2_lines)
            ax.add_collection(left_r2_connect_lines)
            ax.add_collection(left_r3_lines)
            ax.add_collection(left_r3_connect_lines)
            ax.add_collection(left_r4_lines)
            ax.add_collection(left_r4_connect_lines)
            ax.add_collection(left_r5_lines)
            ax.add_collection(left_r5_connect_lines)

            ## Right side
            ax.add_collection(right_r1_lines)
            ax.add_collection(right_r1_connect_lines)
            ax.add_collection(right_r2_lines)
            ax.add_collection(right_r2_connect_lines)
            ax.add_collection(right_r3_lines)
            ax.add_collection(right_r3_connect_lines)
            ax.add_collection(right_r4_lines)
            ax.add_collection(right_r4_connect_lines)
            ax.add_collection(right_r5_lines)
            ax.add_collection(right_r5_connect_lines)

            ## Final lines
            ax.add_collection(final_left_line)
            ax.add_collection(final_right_line)
            ax.add_collection(champ_line)

        if self.n_teams == 32:
            ## draw 32 team bracket
            plt.xlim([0, 220])
            plt.ylim([0, 34])

        plt.axis('off')
        plt.show()
    
    def label_teams(self):
        ## Manipulate plt to
        pass
        # return plt

    def draw_weighted_lines(self):
        if self.win_probabilities is None:
            pass
        else:
            pass
            # return plt

    def export_bracket(self, type='png', filename="bracket"):
        ## Save to image
        if type == 'png':
            plt.savefig(f"{filename}.{type}")

        ##  Save as PDF
        elif type == 'pdf':
            pp = PdfPages(f"{filename}.{type}")
            pp.savefig()
            pp.close()
