# ------------------------------------------------------------------------------------------
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
# ------------------------------------------------------------------------------------------
# Oynani sozlash
root = Tk()
root.title("Bloknot") 
root.geometry("800x600")
root.iconbitmap('bloknot.ico')
root.resizable(False, False)
# ------------------------------------------------------------------------------------------
# funksiya-lar
def yangi_file():
    text_widget.delete(1.0, END)

def file_ochish():
    file_path = askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            contents = file.read()
        text_widget.delete(1.0, END)
        text_widget.insert(1.0, contents)

def file_saqlash():
    if not current_file:
        fileni_saqlash()
    else:
        with open(current_file, 'w') as file:
            file.write(text_widget.get(1.0, END))

def fileni_saqlash():
    file_path = asksaveasfilename()
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_widget.get(1.0, END))
        showinfo("Save As", "File muvaffaqiyatli saqlandi!!!")
        global current_file
        current_file = file_path

def undo():
    text_widget.edit_undo()

def redo():
    text_widget.edit_redo()

def cut():
    text_widget.event_generate("<<Cut>>")

def copy():
    text_widget.event_generate("<<Copy>>")

def paste():
    text_widget.event_generate("<<Paste>>")

def select_all():
    text_widget.tag_add("sel", "1.0", "end")

def word_wrap():
    if word_wrap_var.get() == 1:
        text_widget.config(wrap=WORD)
    else:
        text_widget.config(wrap=NONE)

def dastur_haqida():
    showinfo("About", "Bloknot v1.0")
# ------------------------------------------------------------------------------------------
# widget-lar
text_widget = ScrolledText(root, undo=True)
text_widget.pack(expand=True, fill='both')

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=yangi_file)
file_menu.add_command(label="Open", command=file_ochish)
file_menu.add_command(label="Save", command=file_saqlash)
file_menu.add_command(label="Save As", command=fileni_saqlash)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

format_menu = Menu(menu_bar, tearoff=0)
word_wrap_var = IntVar()
format_menu.add_checkbutton(label="Word Wrap", variable=word_wrap_var, command=word_wrap)
menu_bar.add_cascade(label="Format", menu=format_menu)

view_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=dastur_haqida)
menu_bar.add_cascade(label="Help", menu=help_menu)
# ------------------------------------------------------------------------------------------
root.config(menu=menu_bar)

current_file = None

root.mainloop()