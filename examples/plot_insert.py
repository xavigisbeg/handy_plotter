import context as HP
import os

if (os.name == 'nt'):
    pathData = '//SERVIDORSQL/Datos/Desarrollos y pruebas/Automatitzacio/Dades Proves/Insertion/2017_2426'
    pathPlot = '//SERVIDORSQL/Datos/Desarrollos y pruebas/Automatitzacio/Dades Proves/Insertion/2017_2426'
else:
    pathData = '/home/pi/results/insert/{}'.format(OT)
    pathPlot = '/home/pi/results/plots/{}'.format(OT)

try:
    plotter = HP.HandyPlotter()
    allPlots = True
    if (not allPlots):
        plotter.plot_all(
            pathData=pathData,
            pathPlot=pathPlot,
            find=whatInsert
            )
    else:
        find = ['A', 'B', 'C']
        for i in range(len(find)):
            plotter.plot_all(
                pathData=pathData,
                pathPlot=pathPlot,
                find=find[i],
                nAvg=[5, 10, 15],
                xLim=(0, 2),
                yLim=(0, 20000),
                xTicks=(0, 2, 0.2),
                yTicks=(0, 20000, 1000),
                )
except KeyboardInterrupt:
    print('Cancel')
