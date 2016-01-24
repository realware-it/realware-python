from Tkinter import *
root = Tk()

var1 = StringVar()
var2 = StringVar()

opt1 = OptionMenu(root, var1, 'A', 'B', 'C')   
opt2 = OptionMenu(root, var2, 'A', 'B', 'C')   

opt1.pack(fill=X)
opt2.pack(fill=X)

var1.set('A')
var2.set('B')

def state(): 
   print var1.get(), var2.get()

Button(root, command=state, text='state').pack()

root.mainloop()
