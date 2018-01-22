import context as HP
import os

OT = '2017_2426'

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
        find = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        for i in range(len(find)):
            plotter.plot_all(
                pathData=pathData,
                pathPlot=pathPlot,
                find=find[i],
                )
except KeyboardInterrupt:
    print('Cancel')
