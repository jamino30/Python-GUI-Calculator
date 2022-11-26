from eval import Eval


class Syms(Eval):
    # handle operation button operations
    def __init__(self):
        super().__init__()
        self.current = None

    def sym_click(self, sym):
        # deals with "all clear"
        if sym == "AC":
            self.reset_disp()
            self.current = 0
            self.new_current()

        # deals with evaluating computation
        if sym == "=":
            result = self.eval_comp()

            # handles computation int, float results
            if type(result) != str:
                li_result = str(result).split(".")
                if float(li_result[-1]) == 0:
                    result = li_result[0]

                self.round_result(result)
            else:
                self.current = result

            self.new_current()

        # deals with negation
        if sym == "–":
            self.unary_exp("-", "")

        # deals with percent
        if sym == "%":
            self.unary_exp("", "/100")

        # deals with binary computations
        if sym in self.ops[0:4] and self.comp[-1] not in self.ops[0:4]:
            self.comp.append(str(sym))
            self.current = sym

        # update display
        self.display["text"] = self.current
        self.current = ""

        # TODO: ensure eval() is utilized 100% safely
        # evaluates computation

    # evaluates unary operations (–, %)
    def unary_exp(self, u1, u2):
        self.comp.insert(0, u1 + "(")
        self.comp.append(")" + u2)
        self.current = self.eval_comp()

    # rounds result (based on length)
    def round_result(self, r):
        if len(str(r).split(".")[-1]) > 5:
            self.current = round(r, 5)
        else:
            self.current = r
