import tkinter as tk
from tkinter import ttk
import back
class front_end:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry('350x350')
        self.root.title("Counselling Notifier")
        self.selection=tk.StringVar()

        #label
        # name=tk.Label(self.root,text="Name of Counselling board",font=('Helvetica', 8, 'bold'))
        # name.grid(row=1,column=0,pady=10,padx=5)
        select_lab=tk.Label(self.root,text="Select of Counselling board")
        select_lab.grid(row=2,column=0,pady=10,padx=5)
        #Entry widget
        # name_inp=tk.Entry(self.root,width=28,borderwidth=3)
        # name_inp.grid(row=1,column=1)

        self.combo=ttk.Combobox(self.root,width=26,textvariable=self.selection)
        self.combo["values"]=sorted(("JAC-Delhi","JOSSA","IP University"))
        # self.combo.bind("<<ComboboxSelected>>",self.ok_bfunc)
        self.combo.grid(row=2,column=1)
       

        #Button
        ok_b=tk.Button(self.root,text="Ok",width=7,borderwidth=3,command=self.ok_bfunc)
        ok_b.grid(row=3,column=1)
        self.root.mainloop()
    def ok_bfunc(self):
        back.write_sql(self.selection.get())