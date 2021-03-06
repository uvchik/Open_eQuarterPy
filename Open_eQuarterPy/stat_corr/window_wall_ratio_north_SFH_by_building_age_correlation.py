# OeQ autogenerated correlation for 'Window/Wall Ratio North in Correlation to the Building Age'

import math
import numpy as np
from . import oeqCorrelation as oeq
def get(*xin):

    # OeQ autogenerated correlation for 'Window to Wall Ratio in Northern Direction'
    A_WIN_N_BY_AW= oeq.correlation(
    const= 12970.3948493,
    a=     -26.6534988176,
    b=     0.0205282054259,
    c=     -7.02311790303e-06,
    d=     9.00546817637e-10,
    mode= "lin")

    return dict(A_WIN_N_BY_AW=A_WIN_N_BY_AW.lookup(*xin))

