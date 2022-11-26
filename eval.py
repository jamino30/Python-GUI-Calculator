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
            result = eval("".join(self.comp), {"__builtins__": None}, {})
        # handle exceptions (more than one decimal, divided by 0, etc.)
        except ZeroDivisionError:
            result = "Zero Division Error"
            self.display["font"] = (self.font_fam, 17)
            self.comp.clear()
        except SyntaxError:
            result = "Syntax Error"
            self.display["font"] = (self.font_fam, 25)
            self.comp.clear()

        return result
