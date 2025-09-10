from tkinter import *


# --- Functionality --- #
# 1. Miles to KM function:
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    kilometer_result_label.config(text=f'{km} km')


# --- Create the screen --- #
window = Tk()
window.title('Miles to Kilometers Converter')
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

# --- Create the Widgets --- #

# 1. Entry:
miles_input = Entry()
miles_input.grid(column=1, row=0)

# 2. Labels:
miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

equal_label = Label(text='Equal to')
equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text='0')
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text='km')
kilometer_label.grid(column=2, row=1)

# 3. Buttons:
calculate_button = Button(text='Calculate', command=miles_to_km)
calculate_button.grid(column=1, row=2)

# --- Keep the Screen Open --- #
window.mainloop()
