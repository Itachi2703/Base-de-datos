import tkinter
import random
win = tkinter.Tk()
win.geometry("400x300")
etiqueta = tkinter.Label(win, text = "Hola")
def runfoR():
	print("Hola buen dia")
	
boton1 = tkinter.Button(win, text = "myfunc", command = runfoR)
boton1.pack()
win.mainloop()