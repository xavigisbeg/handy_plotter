import matplotlib.pyplot as plt
import numpy as np
import os


class HandyPlotter:
    """Class to plot everything in a directory with the possibility of making
        more plots where data has been smoothened through averaging"""

    def __init__(self):
        pass

    def plot_all(
            self,
            path,
            plt,
            nAvg,
            ):
        path = '/home/pi/results/insert/2017_0011'
        ls = sorted(os.listdir(path))

        for fle in ls:
            if ('log' not in fle):
                xVals, yVals, xAvgVals, yAvgVals = self.read_excels(
                    path='{}/{}'.format(
                        path,
                        fle),
                    nAvg=nAvg,
                    )

                plt.figure(1)
                plt = self.add_plot(
                    xvals=xVals,
                    yvals=yVals,
                    # color='b',
                    plt=plt,
                    )

                for i in range(len(xAvgVals)):
                    plt.figure(i + 2)
                    plt = self.add_plot(
                        xvals=xAvgVals[i],
                        yvals=yAvgVals[i],
                        # color='b',
                        plt=plt,
                        )

        for i in range(len(xAvgVals) + 1):
            plt.figure(i + 1)
            self.save_plot(
                xlim=(0, 2),
                ylim=(0, 18000),
                xticks=(0, 2, 0.2),
                yticks=(0, 18000, 1000),
                plt=plt,
                path='/home/pi/results/plots/graf{}.png'.format(i),
                )

    def add_plot(
            self,
            xvals,
            yvals,
            plt,
            color=None,
            ):
        if (color is not None):
            plt.plot(xvals, yvals, color)
        else:
            plt.plot(xvals, yvals)
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
            nAvg,  # =15,
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
            xlim,
            ylim,
            xticks,
            yticks,
            plt,
            path='/home/pi/results/plots/graf.png',
            ):
        'Saves a simple plot with the introduced data'

        plt.xlim(xlim)
        # plt.ylim(ylim)
        plt.ylim(ymin=0)
        plt.xticks(np.arange(xticks[0], xticks[1], xticks[2]))
        plt.yticks(np.arange(yticks[0], yticks[1], yticks[2]))
        plt.grid()
        plt.savefig('{}'.format(path), dpi=300)  # /graf.png


if __name__ == "__main__":
    path = '/home/pi/results/insert/2017_0011'
    plotter = HandyPlotter()
    plotter.plot_all(
        path=path,
        nAvg=[5, 10, 15],
        plt=plt,
        )
