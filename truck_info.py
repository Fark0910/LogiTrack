import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
import mysql.connector as mc
import os
import PIL as p
from PIL import Image,ImageTk,ImageEnhance
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
        

   
#print("1.)truckentry,2.)truckinfo")
#choice window


#ch=int(input("enter choice:")







def o2():
      def from_db():
        b1=mc.connect(host="localhost",user="root",passwd="(your passwd)",database="Truckinfo",auth_plugin='mysql_native_password')
        c=b1.cursor()
        d1=e11.get()
        c.execute("select * from Truckinfo  WHERE TripNo = %s",(d1,))
        l=c.fetchone()
       
        
        global t_l1,t_l2,t_l3,t_l4,t_l5,t_l6,t_l7
        t_l1=ttk.Label(f2,text=l[1],style='Test.TLabel')
        t_l1.place(x=220,y=150)
        t_l2=ttk.Label(f2,text=l[2],style='Test.TLabel')
        t_l2.place(x=220,y=200)
        t_l3=ttk.Label(f2,text=l[3],style='Test.TLabel')
        t_l3.place(x=220,y=250)
        t_l4=ttk.Label(f2,text=l[4],style='Test.TLabel')
        t_l4.place(x=220,y=300)
        t_l5=ttk.Label(f2,text=l[5],style='Test.TLabel')
        t_l5.place(x=220,y=350)
        t_l6=ttk.Label(f2,text=l[6],style='Test.TLabel')
        t_l6.place(x=220,y=400)
        t_l7=ttk.Label(f2,text=l[7],style='Test.TLabel')
        t_l7.place(x=220,y=450)
               
              
      def memo():
            file = filedialog.asksaveasfilename(
                filetypes=[("pdf file", ".pdf")],
            defaultextension=".pdf")
        
            b1=mc.connect(host="localhost",user="root",passwd="(your passwd)",database="Truckinfo",auth_plugin='mysql_native_password')
            c=b1.cursor()
            d1=e11.get()
            c.execute("select * from Truckinfo  WHERE TripNo = %s",(d1,))
            l=c.fetchall()
            #pdfmetrics.registerFont(TTFont('MANGAL', "C:/Users/Hp/Downloads/MANGAL/MANGAL.TTF"))  # Replace with the actual font file path
            k =Canvas(file,bottomup=0)
            k.drawRightString(2*inch,2*inch,'Source')
            k.drawRightString(4*inch,2*inch,l[1])
            k.drawRightString(2*inch,3*inch,'Destination')
            k.drawRightString(4*inch,3*inch,l[2])
            k.drawRightString(2*inch,4*inch,'Memo')
            k.drawRightString(4*inch,4*inch,l[3])
            k.drawRightString(2*inch,5*inch,'Investment')
            k.drawRightString(4*inch,5*inch,str(l[4]))
            k.drawRightString(2*inch,6*inch,'MoneyLeft')
            k.drawRightString(4*inch,6*inch,str(l[5]))
            k.drawRightString(2*inch,7*inch,'MoneyToDriver') 
           #drawRightStringworks only with string
            k.drawRightString(4*inch,7*inch,str(l[6]))
            k.drawRightString(2*inch,8*inch,'Profit')
            k.drawRightString(4*inch,8*inch,str(l[7]))
            k.showPage() # saves current page
            k.save()
             # stores the file and close  the canvas
            t_l1.destroy
            t_l2.destroy
            t_l3.destroy
            t_l4.destroy
            t_l5.destroy
            t_l6.destroy
            t_l7.destroy

      a=tk.Toplevel(w1)
      a.title("TRUCK INFO")
      a.geometry("800x700")
      pat_3=os.path.join("light color vector background for truck app window.png")
      image_5 = Image.open(pat_3)
      imk_5 = image_5.resize((1800, 900), Image.LANCZOS)
      enhancer_5 = ImageEnhance.Brightness(imk_5)
      bright_image_5 = enhancer_5.enhance(1.1)
      background_image_5= ImageTk.PhotoImage(bright_image_5,master=w1)
      canvas_5= tk.Canvas(a, width=1400, height=900) 
      canvas_5.pack(fill="both", expand=True)
  
      canvas_5.create_image(-100,-80, image=background_image_5, anchor="nw") # Add other widgets on top of the background
      canvas_5.background_image_5 = background_image_5   
      s_8 = ttk.Style()
      s_8.configure("fra.TFrame")
      global f2
      f2=ttk.Frame(a,width=600, height=540,style='fra.TFrame')
       
      f2.place(x=480,y=160)
      #styles
      #s=ttk.Style()
      #s.theme_use('default')
      
      #s.configure('My.TButton',font=('calibre',25,'bold'), background='violet')
      ttk.Label(f2,text='TRUCK INFORMATION',style='Test.TLabel').place(x=155,y=30)
      ttk.Label(f2,text=' ट्रप नम्बर लिखें',style='Test.TLabel').place(x=50,y=100)                                                                                                                                               #.grid(row=1,column=1)
      ttk.Label(f2,text='प्रस्थान बिंदु',style='Test.TLabel').place(x=50,y=150)                         #.grid(row=2,column=1)
      ttk.Label(f2,text='मंजिल',style='Test.TLabel').place(x=50,y=200)                          #grid(row=3,column=1)
      ttk.Label(f2,text='स्मृति पत्र मिला',style='Test.TLabel').place(x=50,y=250)                     #grid(row=4,column=1)
      ttk.Label(f2,text='पैसा लगाया गया',style='Test.TLabel').place(x=50,y=300)                     #.grid(row=5,column=1)
      ttk.Label(f2,text='पैसा बचा',style='Test.TLabel').place(x=50,y=350)                        #.grid(row=6,column=1)
      ttk.Label(f2,text='ड्राइवर को पैसा ',style='Test.TLabel').place(x=50,y=400)                    #.grid(row=7,column=1)
      ttk.Label(f2,text='लाभ',style='Test.TLabel').place(x=50,y=450)                         #.grid(row=8,column=1)
      t1=tk.IntVar()
      global e11
      e11=ttk.Entry(f2,width=25,textvariable=t1,font=('Roboto',18))
      e11.place(x=220,y=100) 
      b_3=ttk.Button(f2,text='Submit',command=from_db,style='w.TButton')
      b_3.place(x=180,y=500) 
      b_4=ttk.Button(f2,text='Go back',command=a.destroy,style='w.TButton')
      b_4.place(x=280,y=500)
      b_5=ttk.Button(f2,text='Memo',command=memo,style='w.TButton')
      b_5.place(x=380,y=500)          
    
def panda():
    import pandas
    a=pandas.read_csv('TRUCKDATABASE.csv',header= 0)
    print(a)
#def khan5():
    #with open()

#login window
def win2():
    def To_db():     

# Call the function (make sure e1, e2, etc. have valid `get()` methods)
            if (e3.get()==0 or e4.get()=="" or e5.get()=="" or e6.get()=="" or e7.get()==0):
                showwarning('Alert','सभी फ़ील्ड अनिवार्य हैं')
            else:
            
                a1=e3.get()
                a2=e4.get()
                a3=e5.get()
                a4=e6.get()
                a5=e7.get()
                a6=e8.get()
                a7=e9.get()
                a8=e10.get()
                b1=mc.connect(host="localhost",user="root",passwd="(your passwd)",database="Truckinfo",auth_plugin='mysql_native_password')
                c=b1.cursor()
                c.execute("insert into Truckinfo(TripNo,Source,Destination,Memo,Investment,MoneyLeft,MoneyToDriver,Profit) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(a1,a2,a3,a4,a5,a6,a7,a8))
                c.execute("select * from Truckinfo")
                
                l=c.fetchall()
                print(l)
                
                import csv
                #d=[ i for i in l]
                
                with open('TRUCKDATABASE','a') as f:
                    r=csv.writer(f)
                    r.writerow(['TripNo','Source','Destination','Memo','Investment','MoneyLeft','MoneyToDriver','Profit'])
                    r.writerow([a1,a2,a3,a4,a5,a6,a7,a8])
        
    
    
    
                #f.write(str(l))'''
                b1.commit()
                e3.delete(0, tk.END)
                e4.delete(0, tk.END)
                e5.delete(0, tk.END)
                e6.delete(0, tk.END)
                e7.delete(0, tk.END)
                e8.delete(0, tk.END)
                e9.delete(0, tk.END)
                e10.delete(0, tk.END)
            
    def o1():  

            a=tk.Toplevel(w1)
            a.title("TRUCK ENTRY")
            a.geometry("800x700")
            pat_3=os.path.join("light color vector background for truck app window.png")
            image_5 = Image.open(pat_3)
            imk_5 = image_5.resize((1800, 900), Image.LANCZOS)
            enhancer_5 = ImageEnhance.Brightness(imk_5)
            bright_image_5 = enhancer_5.enhance(1.1)
            background_image_5= ImageTk.PhotoImage(bright_image_5,master=w1)
            canvas_5= tk.Canvas(a, width=1400, height=900) 
            canvas_5.pack(fill="both", expand=True)
        
            canvas_5.create_image(-100,-80, image=background_image_5, anchor="nw") # Add other widgets on top of the background
            canvas_5.background_image_5 = background_image_5   
            s_8 = ttk.Style()
            s_8.configure("fra.TFrame")
            f2=ttk.Frame(a,width=600, height=540,style='fra.TFrame')
             
            f2.place(x=480,y=160)
            #styles
            #s=ttk.Style()
            #s.theme_use('default')
            
            #s.configure('My.TButton',font=('calibre',25,'bold'), background='violet')
            ttk.Label(f2,text='FILL ENTRY INFORMATION',style='Test.TLabel').place(x=155,y=30)
            ttk.Label(f2,text=' ट्रप नम्बर ',style='Test.TLabel').place(x=50,y=100)
                                                                                                                                                           #.grid(row=1,column=1)
            ttk.Label(f2,text='प्रस्थान बिंदु',style='Test.TLabel').place(x=50,y=150)                         #.grid(row=2,column=1)
            ttk.Label(f2,text='मंजिल',style='Test.TLabel').place(x=50,y=200)                          #grid(row=3,column=1)
            ttk.Label(f2,text='स्मृति पत्र मिला',style='Test.TLabel').place(x=50,y=250)                     #grid(row=4,column=1)
            ttk.Label(f2,text='पैसा लगाया गया',style='Test.TLabel').place(x=50,y=300)                     #.grid(row=5,column=1)
            ttk.Label(f2,text='पैसा बचा',style='Test.TLabel').place(x=50,y=350)                        #.grid(row=6,column=1)
            ttk.Label(f2,text='ड्राइवर को पैसा ',style='Test.TLabel').place(x=50,y=400)                    #.grid(row=7,column=1)
            ttk.Label(f2,text='लाभ',style='Test.TLabel').place(x=50,y=450)                         #.grid(row=8,column=1)
            t1=tk.IntVar()
            t2=tk.IntVar()
            t3=tk.IntVar()
            t4=tk.IntVar()
            t5=tk.IntVar()
            s1=tk.StringVar()
            s2=tk.StringVar()
            s3=tk.StringVar()
            global e3,e4,e5,e6,e7,e8,e9,e10
            e3=ttk.Entry(f2,width=25,textvariable=t1,font=('Roboto',18))
            e3.place(x=220,y=100) 
            e4=ttk.Entry(f2,width=25,textvariable=s1,font=('Roboto',18))
            e4.place(x=220,y=150)
            e5=ttk.Entry(f2,width=25,textvariable=s2,font=('Roboto',18))
            e5.place(x=220,y=200)
            e6=ttk.Entry(f2,width=25,textvariable=s3,font=('Roboto',18))
            e6.place(x=220,y=250)
            e7=ttk.Entry(f2,width=25,textvariable=t2,font=('Roboto',18))
            e7.place(x=220,y=300)
            e8=ttk.Entry(f2,width=25,textvariable=t3,font=('Roboto',18))
            e8.place(x=220,y=350)
            e9=ttk.Entry(f2,width=25,textvariable=t4,font=('Roboto',18))
            e9.place(x=220,y=400)
            e10=ttk.Entry(f2,width=25,textvariable=t5,font=('Roboto',18))
            e10.place(x=220,y=450)
            b_3=ttk.Button(f2,text='Submit',command=To_db,style='w.TButton')
            b_3.place(x=180,y=500) 
            b_4=ttk.Button(f2,text='Go back',command=a.destroy,style='w.TButton')
            b_4.place(x=280,y=500) 
            a.mainloop()
 
   
    global w2,s
    b1=mc.connect(host="localhost",user="root",passwd="(your passwd)",database="Truckinfo",auth_plugin='mysql_native_password')
    c=b1.cursor()
    k1=e1.get()
    k2=e2.get()
    print(e1.get())
    
    print(e2.get())
    print(k1)
    print(e1.get().lower())
    c.execute("select * from registeruser WHERE username=%s AND password=%s",(k1.lower(),k2.lower(),))
 
    l=c.fetchone()
   
    print(l)
    #print(s_l2)
   # print(s_l2[0])
   # print(e1.get())
   # print(e2.get())
   # print(e1.get().lower())
   # print (e2.get().lower())
    
    if k1.lower()==l[0] and k2.lower()==l[1]:
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)

        showinfo('Directing','पास्वर्ड सही है आगे जाने के लिए ok पर क्लिक करे|')
       
        global w1
        w1=tk.Toplevel(w2)
        w1.configure(bg='pink')
        w1.title("CHOICE WINDOW")
        w1.geometry("1500x900")
      
        
        #main window
        #for image adding which can be in any format we prefer to use pillow module we may use Photoimage of tkinter but with it we can only open png type
        import PIL as p
        from PIL import Image,ImageTk
        
        #showinfo("welcome","welcome fardeen khan in your truck directory.Here you can perform many tasks related to truck.click ok to do so")
        
        showinfo("welcome","ट्रक इन्फ़र्मेशन डिरेक्टरी में आपका स्वागत है यहाँ आप ट्रक का हर काम आसानी से कर सकतें है| धन्याबाद !!! ")
        #photo adding
        pat_3=os.path.join("aesthetic background for a truck info-keeping app with light colors.png")
        image_5 = Image.open(pat_3)
        imk_5 = image_5.resize((1800, 900), Image.LANCZOS)
        enhancer_5 = ImageEnhance.Brightness(imk_5)
        bright_image_5 = enhancer_5.enhance(1.12)
        background_image_5= ImageTk.PhotoImage(bright_image_5,master=w1)
        canvas_5= tk.Canvas(w1, width=1400, height=900) 
        canvas_5.pack(fill="both", expand=True)
    
        canvas_5.create_image(-100,-80, image=background_image_5, anchor="nw") # Add other widgets on top of the background
        canvas_5.background_image_5 = background_image_5   
        
        
        image_log_5= Image.open("white background with curved edges.png")
        imk_log_5 = image_log_5.resize((1800, 900), Image.LANCZOS)
        enhancer_7=ImageEnhance.Brightness(imk_log_5)
        bright_image_7 = enhancer_7.enhance(1.5)
        
        canvas_7= tk.Canvas(canvas_5,width=670, height=400) 
        canvas_7.pack(fill="both", expand=False)
        canvas_7.place(x=470,y=200)
        background_image_7 = ImageTk.PhotoImage(bright_image_7,master=w1)
        canvas_7.create_image(470,200,image=background_image_7)
        canvas_7.background_image_7 = background_image_7
        img_path = "trucker-removebg-preview.png"
        try:
            i = Image.open(img_path)
            k = i.resize((390, 140), Image.LANCZOS)  
            l = ImageTk.PhotoImage(k,master=w1)  
        except Exception as e:
            print(f"Error loading image: {e}")
            exit()  
        hm=l
        z=ttk.Label(canvas_7,image=hm)
        z.place(x=140,y=100)              #relative to canvas_6(relative positioning)
        z.image=hm
        
        canvas_7.create_text(200,290, text="ट्रक एंट्री ",font=('Roboto',20,'bold'))
        canvas_7.create_text(200,340,text="ट्रक इन्फ़र्मेशन",font=('Roboto',20,'bold'))
        canvas_7.create_text(340,50, text="WELCOME",font=('Roboto',22,'bold'))
        s_4=ttk.Style()
        s_4.theme_use('default')
                                # to avoid garbage collection problem
        s_4.configure('w.TButton',font=('Roboto',12,'bold'))
        s_4.map('w.TButton', foreground = [('active', '!disabled', 'white')],
                        background = [('active', 'light blue')])
        #truck image
        
         #for button font button do not work directly thus we apply this method
         #i like to interact with ttk that's all
        #s=ttk.Style()
        #s.theme_use('default')
        #s.configure('Test.TLabel', background= 'light blue')
        #s.configure('w.TButton',font=('calibre',25,'bold'), background='violet')
        #ttk.Label(w1,text='1)ट्रक एंट्री करें ',font=('calibre',30,'bold'),style='Test.TLabel',borderwidth=2,relief='solid').place(x=500,y=394)
        #ttk.Label(w1,text=' 2)ट्रक की इन्फ़र्मेशन पाने के लिए यहाँ क्लिक करें ',font=('calibre',30,'bold'),style='Test.TLabel',borderwidth=2,relief='solid').place(x=500,y=435)#background='light bluestyle.configure('W.TButton', font =
        #tk.Label(w1,text='WELCOME',font=('chalkboard SE',35,'italic'),background='pink',borderwidth=3,relief='solid').place(x=670,y=130)                                                                                                               #('calibri', 10, 'bold', 'underline'),foreground = 'red'            
        b_1= ttk.Button(canvas_7,text='Click here',command=o1,style='w.TButton')
        b_1.place(x=370,y=270)
        b_2=ttk.Button(canvas_7,text='click here',command=o2,style='w.TButton')
        b_2.place(x=370,y=320)       
        b_3=ttk.Button(canvas_7,text='Quit',command=w1.destroy,style='w.TButton')
        b_3.place(x=265,y=360)       
         #ttk.Label(w1,text='3)VIEW TABULUR FILE').            #grid(row=3,column=1)
         #ttk.Button(w1,text='click here',command=khan4).      #grid(row=3,column=3)
         #ttk.Button(w1,text='click here',command=khan5).grid(row=4,column=3)
         #ttk.Label(w1,text='view text file').grid(row=3,column=1)
        

   
#fuctions
        w1.mainloop()
        
    else:
        showwarning('Alert','कृपिया सही पास्वर्ड या यूज़र्नेम लिखें ')
def win3():
    def reg_db():
          
          b1=mc.connect(host="localhost",user="root",passwd="(your passwd)",database="Truckinfo",auth_plugin='mysql_native_password')
          c=b1.cursor()
          c.execute("insert into registeruser(username,password) values('{}','{}')".format(e1.get().lower(),e2.get().lower()))
          c.execute("select * from registeruser")
          
          l=c.fetchall()
          print(l)
          
          import csv
          #d=[ i for i in l]
          
          with open('Regdatabase','a') as f:
              r=csv.writer(f)
              r.writerow(['username','password'])
              r.writerow([e1.get(),e2.get()])
          b1.commit()
          e1.delete(0, tk.END)
          e2.delete(0, tk.END)
          
          top1.mainloop()
    global w2,s
    top1=tk.Toplevel(w2)                                                                                
    top1.title('Registration')
    top1.geometry('800x700')
    pat_2=os.path.join("bg_truck_new.png")
    image_4 = Image.open(pat_2)
    imk_4 = image_4.resize((1800, 900), Image.LANCZOS)
    enhancer_4 = ImageEnhance.Brightness(imk_4)
    bright_image_4 = enhancer_4.enhance(1)
    background_image_4= ImageTk.PhotoImage(bright_image_4,master=top1)
    canvas_4= tk.Canvas(top1, width=1400, height=900) 
    canvas_4.pack(fill="both", expand=True)

    canvas_4.create_image(-100,-80, image=background_image_4, anchor="nw") # Add other widgets on top of the background
    canvas_4.background_image_4 = background_image_4   
    #s_4=ttk.Style()
    #s_4.theme_use('default')
    #                        # to avoid garbage collection problem
    #s_4.configure('w.TButton',font=('Roboto',25,'bold'))
    #s_4.map('w.TButton', foreground = [('active', '!disabled', 'green')],
                       #  background = [('active', 'black')])
    image_log_4= Image.open("white background with curved edges.png")
    imk_log_4 = image_log_4.resize((1800, 900), Image.LANCZOS)
    enhancer_6=ImageEnhance.Brightness(imk_log_4)
    bright_image_6 = enhancer_6.enhance(1.5)
    
    canvas_6= tk.Canvas(canvas_4,width=670, height=400) 
    canvas_6.pack(fill="both", expand=False)
    canvas_6.place(x=470,y=200)
    background_image_6 = ImageTk.PhotoImage(bright_image_6,master=top1)
    canvas_6.create_image(470,200,image=background_image_6)
    canvas_6.background_image_6 = background_image_6         #if you remove it here your image will be 
                                                             #garbage collected and nothing will be seen   
    
    
    canvas_6.create_text(150,149, text="अपना  नाम  लिखें ",font=('Roboto',20,'bold'))
    canvas_6.create_text(150,208,text="लॉगिन  पास्वर्ड  लिखें",font=('Roboto',18,'bold'))
    canvas_6.create_text(308,60, text="REGISTER HERE",font=('Roboto',22,'bold'))
    s1=tk.StringVar
    s2=tk.StringVar
    global e1 ,e2
    e1=tk.Entry(top1,width=30,textvariable=s1,font=('Roboto',16),borderwidth=1,relief='solid')
    e1.place(x=765,y=328,height=34)
    #pack(side='left')
    
    e2=tk.Entry(top1,width=28,textvariable=s2,font=('Roboto',16),borderwidth=1,relief='solid')
    e2.place(x=765,y=388,height=34)
    
    
    ttk.Button(top1,text='Submit',command=reg_db,style='My.TButton').place(x=720,y=480)
    
    


                
        
        
'''loGin form improvement'''    
import PIL as p
from PIL import Image,ImageTk,ImageEnhance 
w2=tk.Tk()
w2.configure(bg='pink')
w2.title("Login Form")
w2.geometry("1400x900")                                                              
pat=os.path.join("bg_truck_new.png")
image = Image.open(pat)
imk = image.resize((1800, 900), Image.LANCZOS)
enhancer = ImageEnhance.Brightness(imk)
bright_image = enhancer.enhance(1)
background_image = ImageTk.PhotoImage(bright_image,master=w2)
canvas = tk.Canvas(w2, width=1400, height=900) 
canvas.pack(fill="both", expand=True)
canvas.create_image(-100,-80, image=background_image, anchor="nw") # Add other widgets on top of the background
canvas.background_image = background_image
#trying to add bitmaps
#img=tk.Image('photo',file='untitled folder')
#p=Image.open("login.jpg")
#p2=p.resize((390,90),Image.ANTIALIAS)         #TRIED all method of adding bitmap it's looks tough 
#p3=ImageTk.PhotoImage(p2)
#w2.iconphoto(True,img)
#w2.geometry("700x600")

'''w2.iconbitmap(r')
#imge on bACKGROUND
#i2=Image.open("lilac.jpg")
#k2=i2.resize((1500,800),Image.ANTIALIAS) 
l2=ImageTk.PhotoImage(k2)
tk.Label(w2,image=l2).pack()
#image of truck
i=Image.open("login2.png")
k=i.resize((390,90),Image.ANTIALIAS) 
l=ImageTk.PhotoImage(k)
f=tk.Frame(w2,background='pink')
f.place(x=430,y=300)#place(x=500,y=500)
tk.Label(w2,image=l,background='pink',borderwidth=3,relief='sunken').place(x=570,y=240)#pack(side='top')'''
#style of button and labels
s=ttk.Style()
s.theme_use('default')
s.configure('Test.TLabel',fill='black',font=('Roboto',18,'bold'))
s.configure('My.TButton',font=('Roboto',18,'bold'))
s.map('My.TButton', foreground = [('active', '!disabled', 'white')],
                     background = [('active', 'light blue')])
image_log= Image.open("white background with curved edges.png")
imk_log = image_log.resize((1800, 900), Image.LANCZOS)
enhancer_2=ImageEnhance.Brightness(imk_log)
bright_image = enhancer_2.enhance(1.5)

canvas_2= tk.Canvas(canvas,width=670, height=400) 
canvas_2.pack(fill="both", expand=False)
canvas_2.place(x=470,y=200)
background_image_2 = ImageTk.PhotoImage(bright_image,master=w2)
canvas_2.create_image(470,200,image=background_image_2)


canvas_2.create_text(150,149, text="अपना  नाम  लिखें ",font=('Roboto',20,'bold'))
canvas_2.create_text(150,208,text="लॉगिन  पास्वर्ड  लिखें",font=('Roboto',18,'bold'))
canvas_2.create_text(308,60, text="LOGIN HERE",font=('Roboto',22,'bold'))

#ttk.Label(w2,text='अपना  नाम  लिखें ',font=('Roboto',22,'bold'),style='Test.TLabel').place(x=500,y=394) #style='Test.TLabel',relief='solid' borderwidth=None
#ttk.Label(w2,text='लॉगिन  पास्वर्ड  लिखें ',font=('Roboto',22,'bold'),borderwidth=None).place(x=500,y=435)  #old method
#tk.Label(w2,text='LOGIN HERE',font=('Roboto',25,'italic'),background='pink',borderwidth=3,relief='solid').place(x=670,y=150)#style='Test.TLabel'
s1=tk.StringVar
s2=tk.StringVar
global e1,e2
e1=tk.Entry(w2,width=30,textvariable=s1,font=('Roboto',16),borderwidth=1,relief='solid')
e1.place(x=765,y=328,height=34)
#pack(side='left')

e2=tk.Entry(w2,width=28,textvariable=s2,font=('Roboto',16,'bold'),borderwidth=1,relief='solid',show="*")
e2.place(x=765,y=388,height=34)



ttk.Button(w2,text='Submit',command=win2,style='My.TButton').place(x=620,y=480)
ttk.Button(w2,text='Register',command=win3,style='My.TButton').place(x=760,y=480)    
w2.mainloop()          #pack(side='bottom')


#main window
#for image adding which can be in any format we prefer to use pillow module we may use Photoimage of tkinter but with it we can only open png typ\e
#import PIL as p
#from PIL import Image,ImageTk
#w1=tk.Tk()
#w1.configure(bg='pink')
#w1.title("CHOICE WINDOW")
#w1.geometry("700x600")
##photo adding
#file_path = os.path.join("Desktop""WORKS_web_py", "truck.jpg")
#i=Image.open("C:/Users/Hp/Desktop/WORKS_web_py/truck.jpg")#("Desktop/WORKS_web_py/truck.jpg")
#k=i.resize((390,90),Image.LANCZOS) 
#k.show()
#l=ImageTk.PhotoImage(k)


#for button font button do not work directly thus we apply this method
#i like to interact with ttk that's all
#s=ttk.Style()
#s.theme_use('default')
#s.configure('Test.TLabel', background= 'light blue')
#s.configure('w.TButton',font=('calibre',25,'bold'))
#ttk.Label(w1,text='1)ट्रक एंट्री करें ',font=('calibre',30,'bold'),style='Test.TLabel').place(x=530,y=300)
#ttk.Label(w1,text=' 2)ट्रक की इन्फ़र्मेशन पाने के लिए यहाँ क्लिक करें ',font=('calibre',30,'bold'),style='Test.TLabel').place(x=530,y=340)#background='light bluestyle.configure('W.TButton', font =
#                                                                                                                        #('calibri', 10, 'bold', 'underline'),foreground = 'red'            
#ttk.Button(w1,text='Click here',command=o1,style='w.TButton').place(x=1100,y=300)
#ttk.Button(w1,text='click here',command=o2,style='w.TButton').place(x=1100,y=340)       
#ttk.Button(w1,text='Quit',command=w1.destroy,style='w.TButton').place(x=700,y=390)       
#ttk.Label(w1,text='3)VIEW TABULUR FILE').            #grid(row=3,column=1)
#ttk.Button(w1,text='click here',command=khan4).      #grid(row=3,column=3)
#ttk.Button(w1,text='click here',command=khan5).grid(row=4,column=3)
#ttk.Label(w1,text='view text file').grid(row=3,column=1)
#w1.mainloop()
#plotter
