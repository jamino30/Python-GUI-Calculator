import tkinter as tk

from operations import Operations
from keys import Keys

# TODO: split into Tkinter GUI and backend classes


class CalculatorApp(tk.Frame, Operations, Keys):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        Operations.__init__(self)

        # grid configuration
        for i in range(4):
            master.columnconfigure(i, weight=1)
        for i in range(6):
            master.rowconfigure(i, weight=1)
        master.grid_rowconfigure(0, minsize=60)

        # implements key input
        master.bind("<Key>", self.key_pressed)

        # result display
        self.disp_size = 45
        self.font_fam = "Courier New"
        self.display = tk.Label(master, text=self.current, height=1, padx=10,
                                font=(self.font_fam, self.disp_size))
        self.display.grid(row=0, columnspan=4, sticky="se")

        # button styling
        butt_expand = "nsew"

        # first row buttons
        butt_ac = tk.Button(master, text="C", command=lambda: self.sym_click("AC"))
        butt_pm = tk.Button(master, text="±", command=lambda: self.sym_click("–"))
        butt_exp = tk.Button(master, text="%", command=lambda: self.sym_click("%"))
        butt_div = tk.Button(master, text="÷", command=lambda: self.sym_click("/"))

        # second row buttons
        butt_7 = tk.Button(master, text="7", command=lambda: self.num_click(7))
        butt_8 = tk.Button(master, text="8", command=lambda: self.num_click(8))
        butt_9 = tk.Button(master, text="9", command=lambda: self.num_click(9))
        butt_mul = tk.Button(master, text="x", command=lambda: self.sym_click("*"))

        # third row buttons
        butt_4 = tk.Button(master, text="4", command=lambda: self.num_click(4))
        butt_5 = tk.Button(master, text="5", command=lambda: self.num_click(5))
        butt_6 = tk.Button(master, text="6", command=lambda: self.num_click(6))
        butt_min = tk.Button(master, text="–", command=lambda: self.sym_click("-"))

        # fourth row buttons
        butt_1 = tk.Button(master, text="1", command=lambda: self.num_click(1))
        butt_2 = tk.Button(master, text="2", command=lambda: self.num_click(2))
        butt_3 = tk.Button(master, text="3", command=lambda: self.num_click(3))
        butt_pl = tk.Button(master, text="+", command=lambda: self.sym_click("+"))

        # fifth row buttons
        butt_0 = tk.Button(master, text="0", command=lambda: self.num_click(0))
        butt_dec = tk.Button(master, text=".", command=lambda: self.num_click("."))
        butt_eq = tk.Button(master, text="=", command=lambda: self.sym_click("="))

        # represents all buttons
        buttons = [[butt_ac, butt_pm, butt_exp, butt_div], [butt_7, butt_8, butt_9,
                   butt_mul], [butt_4, butt_5, butt_6, butt_min], [butt_1, butt_2,
                   butt_3, butt_pl], [butt_0, butt_dec, butt_eq]]

        # button grid layout and styling
        count = 1
        for row in buttons:
            for i, j in enumerate(row):
                j.grid(row=count, column=i, sticky=butt_expand)
                j.configure(font=(self.font_fam, 18, "bold"), highlightthickness=0,
                            borderwidth=0)
            count += 1

        # TODO: implement 5th row grid configuration above
        butt_0.grid(row=5, columnspan=2, sticky=butt_expand)
        butt_0.configure(font=(self.font_fam, 18, "bold"), highlightthickness=0,
                         borderwidth=0)
        grids5 = [butt_dec, butt_eq]
        for i, j in enumerate(grids5):
            j.grid(row=5, column=i + 2, sticky=butt_expand)
            j.configure(font=(self.font_fam, 18, "bold"), highlightthickness=0,
                        borderwidth=0)

    # resets display size
    def reset_disp(self):
        self.display["font"] = (self.font_fam, 45)

    # decreases display size
    def dec_disp(self):
        if self.display.winfo_reqwidth() > 210 and self.disp_size > 0:
            self.disp_size -= 5
            self.display["font"] = (self.font_fam, self.disp_size)
