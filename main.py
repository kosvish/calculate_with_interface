import tkinter as tk
from math import sqrt
from numpy import square

# colors
OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
# fonts
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)


class Calculator:
    def __init__(self):
        # main window
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(False, False)
        self.window.title("Calculator")

        # meaning of expressions
        self.total_expression = ""
        self.current_expression = ""

        # variables for display
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for i in range(1, 5):
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {
            "/": "\u00F7",
            "*": "\u00D7",
            "-": "-",
            "+": "+",

        }
        self.create_digit_buttons()
        self.create_operator()
        self.create_clear_button()
        self.create_equal_button()


    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0,
                               command=lambda x=digit: self.add_expression(x)
                               )
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator(self):
        i = 0
        for oper, symbol in self.operations.items():
            operator = tk.Button(self.buttons_frame,
                                 text=str(symbol), bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                 borderwidth=0, command=lambda x=oper: self.append_operator(x)
                                 )
            operator.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_clear_button(self):
        clear_button = tk.Button(
            self.buttons_frame, text="C", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
            command=self.clear_expression
        )
        clear_button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_equal_button(self):
        equal_button = tk.Button(
            self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
            command=self.evaluate
        )
        equal_button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)


    def create_display_labels(self):
        total_label = tk.Label(
            self.display_frame, text=self.total_expression,
            anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24,
            font=SMALL_FONT_STYLE
        )
        total_label.pack(expand=True, fill="both")
        label = tk.Label(
            self.display_frame, text=self.current_expression,
            anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE
        )
        label.pack(expand=True, fill="both")
        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    # получаем результат выражения
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ''
        except ZeroDivisionError:
            self.current_expression = 'Error'
        finally:
            self.update_label()

    def clear_expression(self):
        self.total_expression = ''
        self.current_expression = ''
        self.update_label()
        self.update_total_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ''
        self.update_total_label()
        self.update_label()

    def add_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
