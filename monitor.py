'''Pypdf2
from pypdf import PdfReader
reader = PdfReader("Testpd.pdf")
page = reader.pages[0]
print(page.extract_text())

# extract only text oriented up
print(page.extract_text(0))

# extract text oriented up and turned left
print(page.extract_text((0, 90)))

# extract text in a fixed width format that closely adheres to the rendered
# layout in the source pdf
print(page.extract_text(extraction_mode="layout"))

# extract text preserving horizontal positioning without excess vertical
# whitespace (removes blank and "whitespace only" lines)
print(page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False))

# adjust horizontal spacing
print(page.extract_text(extraction_mode="layout", layout_mode_scale_weight=1.0))

# exclude (default) or include (as shown below) text rotated w.r.t. the page
print(page.extract_text(extraction_mode="layout", layout_mode_strip_rotated=False))'''
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import mysql.connector as mc


'''
def save_file():
    file = filedialog.asksaveasfilename(
        filetypes=[("pdf file", ".pdf")],
    defaultextension=".pdf")
    save_pdf(file)

def save_pdf(my_path):
    b1=mc.connect(host="localhost",user="root",passwd="Fardeenk250!",database="Truckinfo",auth_plugin='mysql_native_password')
    c=b1.cursor()
    c.execute("insert into Truckprac(TripNo,Source,Destination) values('{}','{}','{}')".format(e1.get(),'bom','bho'))
    l=c.fetchall()
    k = canvas.Canvas(my_path,bottomup=0)

    r_set=c.execute("SELECT * from student where id= ")
    data_row=r_set.fetchone()
    #print(data_row[1])
    k.drawRightString(2*inch,2*inch,'source')
    k.drawRightString(4*inch,2*inch,data_row[1])
    k.drawRightString(2*inch,2.3*inch,'destination')
    k.drawRightString(4*inch,2.3*inch,data_row[2])
	
    k.showPage() # saves current page
    k.save() # stores the file and close  the canvas
    my_w.destroy() #Close the window
    # Keep the window open

my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window 
my_w.title('www.plus2net.com')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Save File',width=30,font=my_font1)  
l1.grid(row=1,column=1,columnspan=2)
global e1
e1=tk.Entry(my_w,width=6,bg='lightyellow',font=16)
e1.grid(row=2,column=1)

b1 = tk.Button(my_w, text='Save', width=20,command = lambda:save_file())
b1.grid(row=2,column=2) 
my_w.mainloop() 
'''
k = canvas.Canvas("Testpd.pdf",bottomup=0)
k.drawRightString(2*inch,2*inch,'source')
k.drawRightString(4*inch,2*inch,'Bhopal')
k.drawRightString(2*inch,2.3*inch,'destination')
k.drawRightString(4*inch,2.3*inch,'Mumbai')
k.showPage() # saves current page
k.save() # stores the file and close  the canvas
'''MY CHECKS
import mysql.connector as mc
b1=mc.connect(host="localhost",user="root",passwd="",database="sqlpro",auth_plugin='mysql_native_password')
c=b1.cursor()
c.execute("select * from student")
l=c.fetchall()
print(type(l))
if l[0][0] == 0:
    print("yes")
    print(l[0][1])
else:
    print("try again")
t1=tk.IntVar()
'''
'''
                 t2=tk.IntVar()
                t3=tk.IntVar()
                t4=tk.IntVar()
                t5=tk.IntVar()
                s1=tk.StringVar()
                s2=tk.StringVar()
                s3=tk.StringVar()

                e1=ttk.Entry(top1,width=30,textvariable=t1)
                e1.grid(row=2,column=2)
                e2=ttk.Entry(top1,width=30,textvariable=s1)
                e2.grid(row=3,column=2)
                e3=ttk.Entry(top1,width=30,textvariable=s2)
                e3.grid(row=4,column=2)
                e4=ttk.Entry(top1,width=30,textvariable=s3)
                e4.grid(row=5,column=2)
                e5=ttk.Entry(top1,width=30,textvariable=t2)
                e5.grid(row=6,column=2)
                e6=ttk.Entry(top1,width=30,textvariable=t3)
                e6.grid(row=7,column=2)
                e7=ttk.Entry(top1,width=30,textvariable=t4)
                e7.grid(row=8,column=2)
                e8=ttk.Entry(top1,width=30,textvariable=t5)
                e8.grid(row=9,column=2)
                s1.set("enter the expression")'''
'''
import pickle as p
def add():
    
    with open("","wb") as f:
        a=int(input("enter no of rows :"))
        for i in range(1,a+1):
            a1=str(input("enter bookno :"))
            a2=str(input("enter author :"))
            a3=str(input("enter bookwrote :"))
            l=[a1,a2,a3]
        p.dump(l,f)
def counter(n):
    with open(" ","rb") as f:
        a=p.load(f)
        for i in range(len(a)):
            if a[i]=='n':
                print("bookwrote is",a[i+1]) 

#add()
b=str(input("enter author name:"))

counter(b)


'''


'''
a=tk.Tk()
s1=tk.StringVar()
s2=tk.StringVar()
def khan():
    m=e2.get()
    c="khans"
    for i in m:
        if m==c:
            print("correct password")
            break
        else:
            print("wrong")
            a.destroy()
l1=ttk.Label(a,text='name ').grid(row=1,column=1)
l2=ttk.Label(a,text='password: ').grid(row=2,column=1)
e1=ttk.Entry(a,width=30,textvariable=s1)
e1.grid(row=1,column=2)
e2=ttk.Entry(a,width=30,textvariable=s2)
e2.grid(row=2,column=2)
ttk.Button(a,text='Quit',command=khan).grid(row=3,column=2)




a.mainloop()


 def khan6():
                b1=mc.connect(host="localhost",user="root",passwd="farhakhan2212",database="sqlpro",auth_plugin='mysql_native_password')
                c=b1.cursor()
                c.execute("select * from Truckinfo")
                l=c.fetchall()
                d1=e10.get()
                x=[]
                y=[]
                for i in range(0,len(l)):
                import matplotlib.pyplot as plt
                x.append(i)
                y.append(int(l[i][7]))
                plt.xlabel('TRIPNO.')
                plt.ylabel('PROFIT')
                plt.title('graph')
                plt.plot(x,y)

'''


       