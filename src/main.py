"""
Basic calculator app with custom GUI display:
- Unary Operations (+/-, %)
- Binary Operations (+, -, *, /)
- Keyboard inputs

Note: Utilizes eval() safely and prevents user
from issuing dangerous commands/functions.

MIT License
Copyright (c) 2022 Jai Amin
"""

from gui import CalculatorApp, tk

if __name__ == "__main__":
    root = tk.Tk()

    # configure constant window sizing
    width = 230
    height = 300
    cen_width = int(root.winfo_screenwidth() / 2 - (width / 2))
    cen_height = int(root.winfo_screenheight() / 2 - (height / 2))
    root.geometry(f"{width}x{height}+{cen_width}+{cen_height}")
    root.resizable(False, False)

    # misc. window attributes
    root.wm_title("Calculator")
    root.configure(bg="#2e2e2e")

    CalculatorApp(root)
    root.mainloop()
