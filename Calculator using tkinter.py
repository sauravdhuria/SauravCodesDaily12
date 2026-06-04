# calculator_final.py
import tkinter as tk

# Global variables to manage calculator state
display_var = None
first_num = None
operator = None

def button_click(number):
    """Appends the clicked number/decimal to the display."""
    current = display_var.get()
    if number == '.' and '.' in current:  # Prevent multiple decimals
        return
    display_var.set(current + str(number))

def button_clear():
    """Clears the display and resets state."""
    global first_num, operator
    display_var.set("")
    first_num = None
    operator = None

def button_operation(op):
    """Stores the first number and operator."""
    global first_num, operator
    try:
        first_num = float(display_var.get())
        operator = op
        display_var.set("")
    except ValueError:
        display_var.set("Error")
        first_num = None
        operator = None

def button_equals():
    """Performs the calculation."""
    global first_num, operator
    try:
        second_num = float(display_var.get())
        display_var.set("")

        if first_num is not None and operator is not None:
            if operator == '+':
                result = first_num + second_num
            elif operator == '-':
                result = first_num - second_num
            elif operator == '*':
                result = first_num * second_num
            elif operator == '/':
                if second_num == 0:
                    display_var.set("Error: Div by zero")
                    return
                result = first_num / second_num

            # Show as integer if no decimal part
            display_var.set(str(int(result)) if result == int(result) else str(result))
        else:
            display_var.set(str(int(second_num)) if second_num == int(second_num) else str(second_num))

    except ValueError:
        display_var.set("Error")
    except Exception as e:
        display_var.set(f"Error: {e}")
    finally:
        first_num = None
        operator = None

# --- Window Setup ---
root = tk.Tk()
root.title("Python Calculator (Final)")
root.geometry("300x400")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

# Display
display_var = tk.StringVar()
e = tk.Entry(root, width=35, borderwidth=5, font=('Arial', 16),
             justify='right', textvariable=display_var)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# --- Button Data ---
# Format: (text, row, col) or (text, row, col, type)
buttons_data = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/',  1, 3, 'operator'),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*',  2, 3, 'operator'),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-',  3, 3, 'operator'),
    ('0', 4, 0), ('.', 4, 1), ('+',  4, 2, 'operator_long'),  # spans 2
    ('C', 5, 0, 'clear'),     ('=',  5, 1, 'equals'),          # spans 3
]

button_font = ('Arial', 14)

for item_data in buttons_data:
    button_text = item_data[0]
    r            = item_data[1]
    c            = item_data[2]
    button_type  = item_data[3] if len(item_data) > 3 else 'number'

    if button_type == 'clear':
        command_func = button_clear
        column_span  = 1
    elif button_type == 'equals':
        command_func = button_equals
        column_span  = 3
    elif button_type == 'operator':
        command_func = lambda op=button_text: button_operation(op)
        column_span  = 1
    elif button_type == 'operator_long':
        command_func = lambda op=button_text: button_operation(op)
        column_span  = 2
    else:  # number or decimal
        command_func = lambda num=button_text: button_click(num)
        column_span  = 1

    btn = tk.Button(root, text=button_text, font=button_font,
                    padx=20, pady=20, command=command_func)
    btn.grid(row=r, column=c, columnspan=column_span,
             padx=5, pady=5, sticky="nsew")

root.mainloop()