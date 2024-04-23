import tkinter
from tkinter import *
from tkinter import filedialog

nameoffile = None
def newFile():
    global nameoffile
    nameoffile = "Hewhomustnotbenamed"
    text.delete(0.0, END)

def saveFile():
    global nameoffile
    f=open(nameoffile, "w")
    data = text.get(0.0, END)
    f.write(data)
    f.close()
def saveAs():
    global nameoffile
    t = text.get(0.0, END)
    f = filedialog.asksaveasfile(mode = "w", defaultextension=".txt")
    try:
        f.write(t.rstrip())
    except:
        tkinter.messagebox.showerror(title="WTF", message="Imbecile")
def openFile():
    global nameoffile
    f = filedialog.askopenfile(mode = "r", defaultextension=".txt")
    nameoffile= f.name
    t=f.read()
    #t=text.get(0.0, END)
    text.delete(0.0, END)
    text.insert(0.0,t)

root = Tk()
root.title("Notepad--")
root.minsize(width = "500", height = "500")
root.maxsize(width = "1200", height = "1200")
root['bg']='black'
my_frame= Frame(root)
my_frame.pack()

scroll=Scrollbar(my_frame)
scroll.pack(side=RIGHT, fill=Y)

text = Text(my_frame, width = "500", height = "500", font=("Courier New", 20), background='black', fg="white",selectbackground="yellow", selectforeground="black", cursor="heart", insertbackground="white",undo=True, yscrollcommand=scroll.set)
text.pack()


menubar = Menu(root)
filemenu = Menu(menubar)

filemenu.add_command(label = "New", command = newFile)
filemenu.add_command(label = "Open", command = openFile)
filemenu.add_command(label = "Save", command = saveFile)
filemenu.add_command(label = "Save As", command = saveAs)
filemenu.add_command(label = "Exit", command = root.quit)

filemenu.add_separator()

menubar.add_cascade(label="Whatch'a wanna do?", menu= filemenu)
root.config(menu = menubar)
root.mainloop()