from nums import Nums
from syms import Syms


class Operations(Nums, Syms):
    def __init__(self):
        # stores current value and computations
        super().__init__()
        self.current = 0
        self.comp = ["0"]
        self.ops = ["+", "-", "*", "/", "–", "%"]

    # resets computation to new computed value
    def new_current(self):
        self.comp.clear()
        self.comp.append(str(self.current))
