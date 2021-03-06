# OeQ autogenerated correlation for 'Window/Wall Ratio South in Correlation to the Building Age'

import math
import numpy as np
from . import oeqCorrelation as oeq
def get(*xin):

    # OeQ autogenerated correlation for 'Window to Wall Ratio in Southern Direction'
    A_WIN_S_BY_AW= oeq.correlation(
    const= -13703.8617287,
    a=     28.4461323872,
    b=     -0.022129294795,
    c=     7.6463202807e-06,
    d=     -9.90104359078e-10,
    mode= "lin")

    return dict(A_WIN_S_BY_AW=A_WIN_S_BY_AW.lookup(*xin))

