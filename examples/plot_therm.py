import context as HP
import os

OT = '2018_1101_B'

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
			'2018_1101_B': 'Primera Hornada Ejercicio 2018 Orden Trabajo 1101 (B)',
		}
		for i in find:
			plotter.plot_all(
				pathData=pathData,
				pathPlot=pathPlot,
				find={'tag': i, 'title': find[i]},
				naming='column',
				xPos=1,
				yPos=[i for i in range(2, 14)],  # [2, 5, 8, 12],
				xLabel='Tiempo [min]',
				yLabel='Temperatura [ºC]',
				yLim=(0, 180.05),
				xTicks=(0, 300.05, 20),
				yTicks=(0, 180.05, 10),
			)
except KeyboardInterrupt:
	print('Cancel')
