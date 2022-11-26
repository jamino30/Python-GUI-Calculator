"""
A simple calculator app.

Designed and developed by Jai Amin
"""

from gui import CalculatorApp, tk

if __name__ == "__main__":
    root = tk.Tk()

    # configure window sizing
    width = 230
    height = 300
    cen_width = int(root.winfo_screenwidth() / 2 - (width / 2))
    cen_height = int(root.winfo_screenheight() / 2 - (height / 2))
    root.geometry(f"{width}x{height}+{cen_width}+{cen_height}")
    root.resizable(False, False)

    # misc. window attributes
    root.wm_title("Calculator")
    photo = tk.PhotoImage(file="logo.png")
    root.wm_iconphoto(False, photo)

    CalculatorApp(root)
    root.mainloop()
