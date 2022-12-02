class Nums:
    # handle number button operation
    def num_click(self, num):
        # displays numbers
        if self.current == 0:
            self.reset_disp()
            self.current = num
        else:
            self.current = str(self.current) + str(num)

        # deals with duplicate numbers in comp list
        if len(self.comp) > 0 and self.comp[-1] not in self.ops[0:4]:
            self.comp[-1] = str(self.current).lstrip("0")
        else:
            self.comp.append(str(self.current))

        # deal with numbers exceeding display
        self.dec_disp()

        # update display
        self.display["text"] = self.current


class Eval:
    # evaluates computation
    def eval_comp(self):
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


class Syms(Eval):
    # handle operation button operations
    def sym_click(self, sym):
        # reset display size after operation is selected
        self.reset_disp()

        # deals with "all clear"
        if sym == "AC":
            self.reset_disp()
            self.current = 0
            self.new_current()

        # deals with evaluating computation
        if sym == "=":
            self.float_result()
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

        # evaluates computation

    # evaluates unary operations (–, %)
    def unary_exp(self, u1, u2):
        self.comp.insert(0, u1 + "(")
        self.comp.append(")" + u2)
        self.current = self.eval_comp()

    def float_result(self):
        result = self.eval_comp()

        # handles computation int, float results
        li_result = str(result).split(".")
        if float(li_result[-1]) == 0:
            result = li_result[0]

        self.current = result


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
