import matplotlib.pyplot as plt
import numpy as np
import os


class HandyPlotter:
    """Class to plot everything in a directory with the possibility of making
        more plots where data has been smoothened through averaging"""

    def __init__(self):
        self.plt = plt
        self.title = {
            'A': 'Primer clavado',
            'B': 'Segundo clavado',
            'C': 'Tercer clavado',
            }

    def plot_all(
            self,
            pathData,
            pathPlot,
            find,
            nAvg=None,
            xLim=None,
            yLim=None,
            xTicks=None,
            yTicks=None,
            ):
        'Function that generates all the graphs'
        if (os.name == 'nt'):
            self.bar = '\\'
        else:
            self.bar = '/'

        ls = sorted(os.listdir(pathData))
        for fle in ls:
            fle_name = fle.split('.')[0]
            if ('log' not in fle and os.path.isfile('{}{}{}'.format(
                    pathData,
                    self.bar,
                    fle,
                    ))):
                if ((find in fle) and True):
                    """and - or True: change to enable or disable the A, B or C
                    differentiation"""
                    title = find

                    xVals, yVals, xAvgVals, yAvgVals = self.read_excels(
                        path='{}{}{}'.format(
                            pathData,
                            self.bar,
                            fle),
                        nAvg=nAvg,
                        )

                    self.plt.figure(1)
                    self.plt.figure(1).suptitle(self.title[title])
                    self.plt.xlabel('Tiempo [s]')
                    self.plt.ylabel('Fuerza [digital]')
                    self.plt = self.add_plot(
                        xvals=xVals,
                        yvals=yVals,
                        # color='b',
                        label=fle_name,
                        plt=self.plt,
                        )
                    self.plt.legend(handler_map={}, loc=4)

                    for i in range(len(xAvgVals)):
                        thisTitle = '{}, media {}'.format(
                            self.title[title],
                            nAvg[i],)
                        self.plt.figure(i + 2)
                        self.plt.figure(i + 2).suptitle(thisTitle)
                        self.plt.xlabel('Tiempo [s]')
                        self.plt.ylabel('Fuerza [digital]')
                        self.plt = self.add_plot(
                            xvals=xAvgVals[i],
                            yvals=yAvgVals[i],
                            # color='b',  # To enforce a color
                            label=fle_name,
                            plt=self.plt,
                            )
                        self.plt.legend(handler_map={}, loc=4)

        plotPlotF = '{}{}{}'.format(
            pathPlot,
            self.bar,
            find,)
        if (not os.path.exists(pathPlot)):
            os.mkdir(pathPlot)
        if (not os.path.exists(plotPlotF)):
            os.mkdir(plotPlotF)

        for i in range(len(xAvgVals) + 1):
            self.plt.figure(i + 1)
            self.save_plot(
                xLim=xLim,
                yLim=yLim,
                xTicks=xTicks,
                yTicks=yTicks,
                plt=self.plt,
                path='{}{}graf{}.png'.format(
                    plotPlotF,
                    self.bar,
                    i,),
                )
            plt.clf()

    def add_plot(
            self,
            xvals,
            yvals,
            plt,
            label,
            color=None,
            ):
        if (color is not None):
            plt.plot(xvals, yvals, color, label=label, linewidth=1.0)
        else:
            plt.plot(xvals, yvals, label=label, linewidth=1.0)
        return plt

    def read_excels(
            self,
            path,
            nAvg=None,
            ):
        with open(path, 'r') as f:
            lines = f.readlines()
            x = []
            y = []
            for line in lines:
                if ('TimeOS' in line):
                    pass
                else:
                    msg = line.split(';')
                    if (float(msg[1].replace(',', '.')) > 2.0):
                        break
                    else:
                        x.append(float(msg[1].replace(',', '.')))
                        y.append(int(msg[2].replace('\n', '')))

            """ Get averages """
            if (nAvg is not None):
                xAvg, yAvg = [], []
                for i in range(len(nAvg)):
                    xAvg.append(self.avg_excels(inp=x, nAvg=nAvg[i]))
                    yAvg.append(self.avg_excels(inp=y, nAvg=nAvg[i]))
            else:
                xAvg, yAvg = None, None
            return x, y, xAvg, yAvg

    def avg_excels(
            self,
            inp,
            nAvg,
            ):
        av = []
        for i in range(len(inp)):
            avg = 0
            if (i < nAvg - 1):
                for ii in range(i + 1):
                    avg += inp[ii]
                av.append(avg / (i + 1))
            else:
                for ii in range(nAvg):
                    avg += inp[i - ii]
                av.append(avg / (nAvg))
        return av

    def save_plot(
            self,
            xLim,
            yLim,
            xTicks,
            yTicks,
            plt,
            path,  # ='/home/pi/results/plots/graf.png',
            ):
        'Saves a simple plot with the introduced data'

        if (xLim is not None):
            plt.xlim(xLim)
        else:
            plt.xlim(xmin=0)  # To only set the lower limit
        if (yLim is not None):
            plt.ylim(yLim)
        else:
            plt.ylim(ymin=0)  # To only set the lower limit
        if (xTicks is not None):
            plt.xticks(np.arange(xTicks[0], xTicks[1], xTicks[2]))
        if (yTicks is not None):
            plt.yticks(np.arange(yTicks[0], yTicks[1], yTicks[2]))
        plt.grid()
        plt.savefig('{}'.format(path), dpi=300)


if __name__ == "__main__":
    print('Invoke the module, do not run it directly')
