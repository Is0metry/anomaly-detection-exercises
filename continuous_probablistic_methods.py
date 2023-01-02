import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Tuple

def get_lower_and_upper_bounds(s:pd.Series, range: float = 1.5) -> Tuple[float,float]:
    '''
    ## Parameters
    df: `DataFrame` containing values to mark as outliers
    s: `string` where `s in df.columns` indicating which column to operate on
    k: `float` indicating how many Standard Deviations
    outside of the IQR a value must be
    to be marked as an outlier
    ## Returns
    `DataFrame` with outlier status marked as `s + '_outlier'`
    '''
    mean = s.mean()
    q1, q3 = s.quantile([.25, .75])
    iqr = q3-q1
    return mean - iqr * range, mean + iqr * range