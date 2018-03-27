import context as HP
import os

OT = '2018_9012'

if (os.name == 'nt'):
	pathData = '{}{}/{}'.format(
		'//SERVIDORSQL/Datos/Desarrollos y pruebas/',
		'Automatitzacio/Dades Proves/Insertion',
		OT)
	pathPlot = '{}{}/{}'.format(
		'//SERVIDORSQL/Datos/Desarrollos y pruebas/',
		'Automatitzacio/Dades Proves/Insertion',
		OT)
else:
	pathData = '/home/pi/results/insert/{}'.format(OT)
	pathPlot = '/home/pi/results/plots/{}'.format(OT)

try:
	plotter = HP.HandyPlotter()
	allPlots = True
	whatInsert = 'A'
	if (not allPlots):
		plotter.plot_all(
			pathData=pathData,
			pathPlot=pathPlot,
			find=whatInsert,
		)
	else:
		find = {
			'A': 'Primer clavado',
			'B': 'Segundo clavado',
			'C': 'Tercer clavado',
		}
		for i in find:
			plotter.plot_all(
				pathData=pathData,
				pathPlot=pathPlot,
				find={'tag': i, 'title': find[i]},
				naming='file',
				nAvg=[5, 10, 15],
				xPos=1,
				yPos=[2],
				xLabel='Tiempo [s]',
				yLabel='Fuerza [ADC]',
				xLim=(0, 2),
				yLim=(0, 20000),
				xTicks=(0, 2, 0.2),
				yTicks=(0, 20000, 1000),
			)
except KeyboardInterrupt:
	print('Cancel')
