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
    whatTc = 'A'
    if (not allPlots):
        plotter.plot_all(
            pathData=pathData,
            pathPlot=pathPlot,
            find=whatTc,
            )
    else:
        find = ['0']
        for i in range(len(find)):
            plotter.plot_all(
                pathData=pathData,
                pathPlot=pathPlot,
                find=find[i],
                xPos=1,
                yPos=2,
                )
except KeyboardInterrupt:
    print('Cancel')
