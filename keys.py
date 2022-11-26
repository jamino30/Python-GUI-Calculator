class Keys:
    def __init__(self):
        self.ops = None

    # handles keyboard input
    def key_pressed(self, event):
        # handles number input
        for i in range(10):
            if event.char == str(i):
                self.num_click(i)

        # handles symbol input
        for s in self.ops:
            if event.char == s:
                self.sym_click(s)

        # handles decimal input
        if event.char == ".":
            self.num_click(".")

        # handles equals input
        if event.char == "=" or event.keysym == "Return":
            self.sym_click("=")

        # handles clear (AC) input
        if event.char == "c" or event.keysym == "Escape":
            self.sym_click("AC")
