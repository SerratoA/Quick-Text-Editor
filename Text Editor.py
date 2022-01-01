#Python Program Created by Angel Serrato
#Program is a simple text editor within a GUI that allows for file selection and file saving 

from tkinter import Button, Grid, Label,Tk,Text,INSERT,TOP,LEFT,RIGHT,END,filedialog, Scale, HORIZONTAL, font
from tkinter.messagebox import showinfo

class TextEditor(Tk):
    def __init__(self, parent=None):
        Tk.__init__(self, parent)
        self.title('Makeshift Text Editor')
        self.geometry("800x600")
        self.make_widgets()
        self.contents="Text.txt"
        
    def path(self):
        showinfo(title='File selection',message='Please select a text file to read')
        self.contents=filedialog.askopenfilename(parent=self,initialdir="/",title='Select a file to be printed')
        try:
            infile=open(self.contents,'r')
            self.read=infile.read()
            infile.close
            self.text.delete(1.0,END)
        except Exception as e:
            print('Error', e)
        self.text.insert(INSERT,self.read)
        
    def overwrite(self):
        userT=self.text.get("1.0","end-1c")
        if len(userT)==0:
            showinfo(title='Empty Entry',message='Error. No Text Input.')
            return
        if userT==self.read:
             showinfo(title='No Change',message='There was no change in your entry')
             return
        try:
            outfile=open(self.contents,'w')
            outfile.write(userT)
            outfile.close()
        except Exception as e:
            print('Error', e)
        if self.contents!="Text.txt":
            showinfo(title='File overwrite', message='The contents of the file have been overwritten and the file can be found at ' + self.contents)
        else:
            showinfo(title='File Creation', message="The contents of the file have been created in a text file called 'Text'")
        
    def make_widgets(self):
        Grid.rowconfigure(self,0,weight=1)
        Grid.columnconfigure(self,0,weight=1)
        Grid.rowconfigure(self,1,weight=1)
        
        heading = Label(self,text="Welcome to Serrato's Quick Text Editor!", font="Cambria 30 bold", bg="#fffddb").grid(row=0,column=0,sticky="EW",pady=40)
        self.text=Text(self, font="Verdana 10")
        self.text.grid(row=1,column=0,sticky="NSEW", padx=(15,15))
        printFile = Button(self,text='Select File',font ="Cambria 12",fg="#280137", command=lambda:self.path()).grid(row=2,column=0,sticky="NS")
        saveFile = Button(self,text='Save Contents',font ="Cambria 12",fg="#280137", command=lambda:self.overwrite()).grid(row=3,column=0,sticky="NS", pady=10)

TextEditor().mainloop()




