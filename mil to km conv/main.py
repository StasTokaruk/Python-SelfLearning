from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('Mil to Km Converter')

def conv(mil, label):
     label = Label(window, text=f'Result{int(mil)*1.6}')

mil1 = Entry(window)
mil1.grid(column=0, row=0, columnspan=2)
label = Label(window, text=f'Result')
label.grid(column=0, row=1, columnspan=2)
button = Button(window, text="Convert", command=lambda mil = mil1.get(): conv(mil, label))
button.grid(column=0, row=2, columnspan=2)

window.mainloop()