"""
Quantiphyse plugin for perfusion simulation

Author: Martin Craig <martin.craig@eng.ox.ac.uk>
Copyright (c) 2016-2017 University of Oxford, Martin Craig
"""
from .widget import PerfSimWidget
from .process import PerfSimProcess
QP_MANIFEST = {
    "widgets" : [PerfSimWidget],
    "processes" : [PerfSimProcess],
}
