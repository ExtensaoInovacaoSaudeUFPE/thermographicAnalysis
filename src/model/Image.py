import numpy as np
class Image:
    data: np.ndarray

    def __init__(self, data: np.ndarray):
        self.data = data
