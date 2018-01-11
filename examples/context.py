import os
import sys

if (os.name == 'nt'):
    bar = '\\'
else:
    bar = '/'

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..{}..'.format(bar))
        )
    )

from handy_plotter.src.plot import HandyPlotter
# import get_ip
