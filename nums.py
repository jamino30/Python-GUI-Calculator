class Nums:
    # handle number button operations
    def __init__(self):
        self.display = None
        self.current = None
        self.comp = None

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

        # TODO: properly change display size based on current/result size
        # deal with numbers exceeding display
        self.dec_disp()

        # update display
        self.display["text"] = self.current

        # console testing
        print("Current Val:", self.current)
        print("Computation:", self.comp, "\n")