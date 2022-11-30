class Eval:
    def __init__(self):
        self.comp = None
        self.font_fam = None
        self.display = None

    # evaluates computation
    def eval_comp(self):
        # uses eval() safely (prevents hidden values/dangerous functions)
        # 1. user is restricted to number/operation keys only
        # 2. all possible exceptions have been accounted for
        # Source: https://lybniz2.sourceforge.net/safeeval.html
        try:
            round_int = 5
            result = round(eval("".join(self.comp), {"__builtins__": None}, {}), round_int)

            # handle result display text size
            result_width = len(str(round(result)))
            sizes = [range(8), [8], [9], [10, 11], [12, 13], range(14, 17),
                     range(17, 22), range(22, 33), range(33, 63)]
            init_size = 45
            for size_group in sizes:
                for size in size_group:
                    if result_width == size:
                        self.set_font_size(init_size)
                init_size -= 5

        # handle exceptions (more than one decimal, divided by 0, etc.)
        except ZeroDivisionError:
            result = "Zero Division Error"
            self.set_font_size(17)
            self.comp.clear()
        except SyntaxError:
            result = "Syntax Error"
            self.set_font_size(25)
            self.comp.clear()

        return result

    def set_font_size(self, size):
        self.display["font"] = (self.font_fam, size)
