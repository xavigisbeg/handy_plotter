import context as HP
import os

OT = '2018_0000'

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
        'A': 'Termopar A',
        }
    if (not allPlots):
        plotter.plot_all(
            pathData=pathData,
            pathPlot=pathPlot,
            find=whatTc['A'],
            )
    else:
        find = {
            '0': 'Primera Hornada',
            }
        for i in find:
            plotter.plot_all(
                pathData=pathData,
                pathPlot=pathPlot,
                find={'tag': i, 'title': find[i]},
                xPos=1,
                yPos=2,
                )
except KeyboardInterrupt:
    print('Cancel')
