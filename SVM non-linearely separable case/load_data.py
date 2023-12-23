import pandas as pd
import numpy as np


def load_data(file):
    df = pd.read_csv(file, sep=' ', header=None)
    return df[[0,1]].to_numpy().astype(float), (df[2].to_numpy()[:, np.newaxis]).astype(float)