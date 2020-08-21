import cx_Oracle
from tkinter import *
from tkinter import messagebox
import pandas as pd
con=cx_Oracle.connect('system/123@localhost/orcl')
root=Tk()
def submit(e1):
    c=con.cursor()
    k=e1.get()
    if(k==''):
        messagebox.showinfo('ERROR','name fiels is mandatory')
        first()
    else:
        l=[]
        l1=[]
        c.execute("select *from personals1 where name=(select name from records1 where name=('"+k+"'))")
        for i in c:
            l.append(list(i))
        c.execute("select *from crime1 where fir_id=(select fir_id from records1 where name=('"+k+"'))")
        for i in c:
            l1.append(list(i))
        if(l==[] or l1==[]):
            messagebox.showinfo('ERROR','no data found')
            first()
        else:
            p1=pd.DataFrame(l,columns=['\033[1m]'+'aadhar_no'+'\033[0m','\033[1m'+'hometown'+'033[0m','033[1m'+'name'+'033[0m'])
            p2=pd.DataFrame(l1,columns=['fir_id','date','category','sentence'])
            root1=Tk()
            t=Text(root1)
            t.insert('1.0',str(p1))
            t.insert(END,'\n\n\n')
            t.insert(END,str(p2))
            t.config(state=DISABLED)
            t.pack()
            first()
def first():
    l1=Label(root,text='name').grid(row=10,column=20)
    e1=Entry(root,bd=10)
    e1.grid(row=10,column=21)
    b1=Button(root,text='submit',command=lambda:submit(e1)).grid(row=15,column=20)
    b1=Button(root,text='exit',command=close).grid(row=15,column=25)
def close():
    if messagebox.askokcancel("Quit", "You want to quit now?"):
        root.destroy()
first()
root.mainloop()
    
