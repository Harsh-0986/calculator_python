import tkinter as tk

# For icons
import base64
import os

# Colours
LIGHT_GRAY = '#F5F5F5'
LABEL_COLOUR = '#25265E'
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFF"
LIGHT_BLUE = "#CCEDFF"

# Icon
b64_data = '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'
icon_data = base64.b64decode(b64_data)
tempfile = "icon.ico"
iconfile = open(tempfile, 'wb')
iconfile.write(icon_data)
iconfile.close()

# Font styles
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

class Calculator:

    # Initilization of the main windows
    def __init__(self):
        '''Creates the main window'''
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)

        # Icons
        # image = tk.PhotoImage(data=b64_data)
        self.window.wm_iconbitmap(tempfile)
        os.remove(tempfile)

        self.window.title("Calculator")

        # Creating the frames
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        # Creating the labels
        self.total_expression = ""
        self.current_expression = ""

        self.total_label, self.label = self.create_display_labels()

        # Configuring buttons frame to fill whole space
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        #Adding the digits buttons
        self.digits = {
             7: (1, 1), 8: (1, 2), 9: (1, 3),
             4: (2, 1), 5: (2, 2), 6: (2, 3),
             1: (3, 1), 2: (3, 2), 3: (3, 3),
             0: (4, 2), '.': (4, 1)
        }
        self.create_digits_button()

        # Adding operator buttons
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.create_operator_buttons()

        # Create special buttons
        self.create_special_buttons()

        # Bind keys
        self.bind_keys()

    def create_display_labels(self):
        '''Creates the display labels'''
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOUR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOUR, padx=24, font=LARGE_FONT_STYLE, borderwidth=0)
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_digits_button(self):
        '''Creates the digits buttons'''
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOUR, font=DIGIT_FONT_STYLE, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_display_frame(self):
        '''Creates the main display frame'''
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        '''Creates the buttons frame'''
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_operator_buttons(self):
        '''Creates the operators button'''
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1

    def create_clear_button(self):
        '''Creates clear button'''
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_equals_button(self):
        '''Creates equal button'''
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_special_buttons(self):
        '''Creates special buttons'''
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_square_root_button()

    def update_total_label(self):
        '''Updates the total label'''
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f" {symbol} ")
        self.total_label.config(text=expression)

    def update_label(self):
        '''Updates the current expression label'''
        self.label.config(text=self.current_expression[:11])

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        '''Appends the operator'''
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression=""
        self.update_total_label()
        self.update_label()

    def clear(self):
        '''Clears the labels'''
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def evaluate(self):
        '''Evaluates the expression'''
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "ERROR"
        finally:
            self.update_label()

    def create_square_button(self):
        '''Creates the square button'''
        button = tk.Button(self.buttons_frame, text='x\u00b2', bg=OFF_WHITE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def square(self):
        '''Gives the square of expression'''
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_root_button(self):
        '''Creates the square root button'''
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.square_root)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def square_root(self):
        '''Gives the square root of expression'''
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def bind_keys(self):
        '''Binds the keys of the keyboard to their respective function in calculator'''
        self.window.bind("<Return>", lambda event: self.evaluate())

        # Binding digits
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        # Binding operators
        for key in self.operations:
            self.window.bind(str(key), lambda event, operator=key: self.append_operator(operator))

    def run(self):
        '''Runs the calculator app'''
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()

