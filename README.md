# handy_plotter
Handy plotter class to plot all csv files in a directory.

# Usage
Import the module and create an instance of the class. Then use the function **plot_all()**, passing the *path* argument to the directory with the csv files and, if you want other graphs averaged, pass the *nAvg* argument with a list of the several modulus of averaging. If not, don't use the *nAvg* parameter.
Example:
```
import HandyPlotter

path = '<yourPath>'
plotter = HandyPlotter()
plotter.plot_all(
    path=path,
    nAvg=[5, 10, 15],
    plt=plt,
    )
```

# Extra info
Is the name geeky? Yes
