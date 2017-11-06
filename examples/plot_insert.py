import context as HP

pathIn = '/home/pi/results/insert/2017_0011'
pathOut = '/home/pi/results/plots'
plotter = HP.HandyPlotter()
plotter.plot_all(
    pathIn=pathIn,
    pathOut=pathOut,
    nAvg=[5, 10, 15],
    xLim=(0, 2),
    yLim=(0, 18000),
    xTicks=(0, 2, 0.2),
    yTicks=(0, 18000, 1000),
    )
