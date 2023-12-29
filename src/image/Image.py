import numpy as np
from abc import ABC, abstractmethod
class Image(ABC):
    data: np.ndarray

    def __init__(self, data: np.ndarray):
        self.data = data
