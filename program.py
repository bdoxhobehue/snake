import tkinter as tk


top = tk.Tk()
tex = tk.Text(master=top)
tex.pack(side=tk.RIGHT)
bop = tk.Frame()
bop.pack(side=tk.LEFT)
for k in range(1,10):
    tv = 'Say {}'.format(k)
    b = tk.Button(bop, text=tv, command=cbc(k, tex))
    b.pack()

tk.Button(bop, text='Exit', command=top.destroy).pack()
top.mainloop()