import context as HP
import os

OT = '2018_0002'

if (os.name == 'nt'):
    pathData = '{}{}/{}'.format(
        '//SERVIDORSQL/Datos/Desarrollos y pruebas/',
        'Automatitzacio/Dades Proves/Termoparell',
        OT)
    pathPlot = '{}{}/{}'.format(
        '//SERVIDORSQL/Datos/Desarrollos y pruebas/',
        'Automatitzacio/Dades Proves/Termoparell',
        OT)
else:
    pathData = '/home/pi/results/therm/{}'.format(OT)
    pathPlot = '/home/pi/results/plots/{}'.format(OT)

try:
    plotter = HP.HandyPlotter()
    allPlots = True
    whatTc = {
        'L1': 'Termopar A',
        }
    if (not allPlots):
        plotter.plot_all(
            pathData=pathData,
            pathPlot=pathPlot,
            find=whatTc['A'],
            )
    else:
        find = {
            'L1': 'Primera Hornada',
            }
        for i in find:
            plotter.plot_all(
                pathData=pathData,
                pathPlot=pathPlot,
                find={'tag': i, 'title': find[i]},
                xPos=1,
                yPos=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                xLabel='Tiempo [min]',
                yLabel='Temperatura [ºC]',
                yLim=(0, 200),
                xTicks=(0, 1500, 60),
                yTicks=(0, 200, 10),
                )
except KeyboardInterrupt:
    print('Cancel')
