# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:01:48 2019

@author: Sudhish Kumar
"""

import tkinter as tk
from tkinter import filedialog

class FileBrowser(tk.Frame):
    FileInfo=""
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_browse_widget()

    def create_browse_widget(self):
        self.labelFrame=tk.LabelFrame(master=self, text="")

        self.labelTxt=tk.Label(self.labelFrame,
                       textvariable=self.FileInfo,
                       width=50, 
                       borderwidth=3, 
                       relief="sunken",
                       anchor='e')
        self.labelTxt.grid(column=0,row=1)
        
        self.browseBtn=tk.Button(self.labelFrame,
                            text="Browse...", 
                            command=self.getFile)
        
        self.browseBtn.grid(column=1,row=1)
        pass

    def getFile(self):
        self.FileInfo=filedialog.askopenfilename()
        print(self.FileInfo)
        self.labelTxt.configure(text=self.FileInfo)
        pass

class optionTypeList(tk.Frame):
    OPTION_LIST=["Option 1", "Option 2"]
    OPTION_VAL=OPTION_LIST[0]
    
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()

    def createOptionWidgets(self):
#        numVars=len(self.OPTION_LIST)
        self.OPTION_VAL=tk.StringVar()
        self.OPTION_VAL.set(self.OPTION_LIST[0])
        self.optMenu1=tk.OptionMenu(self, self.OPTION_VAL, *self.OPTION_LIST, command=self.func)
        self.optMenu1.grid()
    def func(self,value):
        print(value)
    



class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        #self.create_widgets()
        self.createInputForms()


    def createInputForms(self):
        self.labelFileFrame=tk.LabelFrame(master=self, text="Files...")
        self.labelFileFrame.grid(column=1,row=0)
        
        self.labelOptionsFrame=tk.LabelFrame(master=self,text="Options...")
        self.labelOptionsFrame.grid(column=0,row=0)

        self.File1=FileBrowser(self.labelFileFrame)
        self.File2=FileBrowser(self.labelFileFrame)
        self.File3=FileBrowser(self.labelFileFrame)

        self.File1.labelTxt.configure(text="Input the first File Name")
        self.File2.labelTxt.configure(text="Input the second File Name")
        self.File3.labelTxt.configure(text="Input the third File Name")
        
        self.File1.labelFrame.grid(column=0,row=0)
        self.File2.labelFrame.grid(column=0,row=1)
        self.File3.labelFrame.grid(column=0,row=2)
        
        self.TypeOptions=optionTypeList(self.labelOptionsFrame)
        self.TypeOptions.OPTION_LIST=["MAX", "MIN", "ALL"]
        self.TypeOptions.createOptionWidgets()
        
        pass

root = tk.Tk()
app = Application(master=root)
app.mainloop()


def hellw():
    print("Hello World")