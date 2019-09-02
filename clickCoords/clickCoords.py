#!/usr/bin/env python2

import Tkinter as tk
import ttk
from pymouse import PyMouse

def click():
	global entry_x, entry_y, mouse
	mouse.click(int(entry_x.get()), int(entry_y.get()))
	entry_x.delete(0, 'end')
	entry_y.delete(0, 'end')

p = tk.Tk()
p.attributes('-type', 'dialog')
p.wm_title("Coordinate clicker")

label = ttk.Label(p, text="loading...", font=("Roboto", 12))
label.configure(anchor="center")
label.pack(side="top", fill=tk.BOTH, pady=5)

frame = ttk.Frame(p)
frame.pack(fill="x", pady=5)
label_x = ttk.Label(frame, text="X:", font=("Roboto", 12)).grid(row=0, column=0)
entry_x = ttk.Entry(frame, width=4)
entry_x.grid(row=0, column=1)
label_y = ttk.Label(frame, text="Y:", font=("Roboto", 12)).grid(row=0, column=2)
entry_y = ttk.Entry(frame, width = 4)
entry_y.grid(row=0, column=3)
button_click = ttk.Button(frame, text="Click", command = click, width=5)
button_click.grid(row=0, column=4)

button = ttk.Button(p, text="Close", command = p.destroy)
button.pack(side="bottom")

class popup:
	def __init__(self, label, mouse):
		self.m = mouse
		self.l = label
		self.l.configure(text=self.m.position())
	def update(self):
		self.l.configure(text=self.m.position())
		self.l.after(50, self.update)


mouse = PyMouse()
popupmsg = popup(label, mouse)
popupmsg.update()
p.mainloop()
